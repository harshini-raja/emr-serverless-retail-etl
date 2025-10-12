from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("instacart-dims-seed").getOrCreate()

raw = "s3://instacart-raw-harshini-20251002/instacart/raw"
cur = "s3://instacart-curated-harshini-20251002/instacart/curated"

spark.read.option("header","true").csv(f"{raw}/products/products.csv") \
    .write.mode("overwrite").parquet(f"{cur}/dim_product/dt=seed/")
spark.read.option("header","true").csv(f"{raw}/aisles/aisles.csv") \
    .write.mode("overwrite").parquet(f"{cur}/dim_aisle/dt=seed/")
spark.read.option("header","true").csv(f"{raw}/departments/departments.csv") \
    .write.mode("overwrite").parquet(f"{cur}/dim_department/dt=seed/")

spark.stop()
