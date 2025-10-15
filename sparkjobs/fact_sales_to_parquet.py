# fact_sales_to_parquet.py
from pyspark.sql import SparkSession, functions as F
import sys, datetime

# ---- config ----
RAW_BUCKET = "instacart-raw-harshini-20251002"
CURATED_BUCKET = "instacart-curated-harshini-20251002"
RAW_BASE = f"s3://{RAW_BUCKET}/instacart/raw"
CURATED_BASE = f"s3://{CURATED_BUCKET}/instacart/curated"

# ---- pick partition date ----
def get_dt(argv):
    if len(argv) > 1:
        # validate YYYY-MM-DD
        try:
            datetime.datetime.strptime(argv[1], "%Y-%m-%d")
            return argv[1]
        except ValueError:
            raise SystemExit(f"Bad dt '{argv[1]}'. Use YYYY-MM-DD (e.g., 2025-10-07).")
    return datetime.date.today().isoformat()

DT = get_dt(sys.argv)
target = f"{CURATED_BASE}/fact_sales/dt={DT}/"

# ---- start Spark ----
spark = (SparkSession.builder
         .appName(f"instacart-fact-sales-{DT}")
         .getOrCreate())
spark.sparkContext.setLogLevel("WARN")

print(f"[INFO] Building fact_sales for dt={DT}")
print(f"[INFO] RAW_BASE     = {RAW_BASE}")
print(f"[INFO] CURATED_BASE = {CURATED_BASE}")
print(f"[INFO] Target path  = {target}")

# ---- read raw big CSVs ----
orders = (spark.read
    .option("header", "true")
    .option("inferSchema", "true")   # consider explicit schema later for speed
    .csv(f"{RAW_BASE}/orders/*.csv"))

prior = (spark.read
    .option("header", "true")
    .option("inferSchema", "true")
    .csv(f"{RAW_BASE}/order_products_prior/*.csv"))

train = (spark.read
    .option("header", "true")
    .option("inferSchema", "true")
    .csv(f"{RAW_BASE}/order_products_train/*.csv"))

op = prior.unionByName(train)

# ---- read product dim from curated parquet (seed) ----
prod = spark.read.parquet(f"{CURATED_BASE}/dim_product/dt=seed/")
prod_keys = prod.select("product_id", "aisle_id", "department_id")

# ---- join to build fact ----
fact = (op.join(orders, "order_id")
          .join(prod_keys, "product_id", "left"))

# normalize types (safe casts)
casts = {
    "order_id": "int",
    "product_id": "int",
    "user_id": "int",
    "add_to_cart_order": "int",
    "reordered": "int",
    "order_number": "int",
    "order_dow": "int",
    "order_hour_of_day": "int",
    "days_since_prior_order": "int",
    "aisle_id": "int",
    "department_id": "int",
}
for c, t in casts.items():
    if c in fact.columns:
        fact = fact.withColumn(c, F.col(c).cast(t))

fact_out = fact.select(
    "order_id","product_id","user_id",
    "add_to_cart_order","reordered",
    "order_number","order_dow","order_hour_of_day","days_since_prior_order",
    "aisle_id","department_id"
)

# modest #files; tune later (aim ~128–256MB per file)
fact_out = fact_out.repartition(32)

print(f"[INFO] Row count (sampled) = {fact_out.count()}")

# ---- write parquet to curated (single-day partition) ----
(fact_out.write
    .mode("overwrite")
    .option("compression", "snappy")
    .parquet(target))

print(f"[INFO] Wrote dt={DT} to {target}")
spark.stop()
