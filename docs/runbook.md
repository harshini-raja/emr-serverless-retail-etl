```markdown
# Runbook (Day 1 → Day 3)

## Day 1 — S3 & Snowflake setup (no EMR spend yet)
1. Create S3 buckets: `instacart-raw-<you>`, `instacart-curated-<you>` (default encryption on).
2. Upload Instacart CSVs to `s3://instacart-raw-<you>/instacart/` under `orders/`, `order_products_prior/`, `order_products_train/`, `products/`, `aisles/`, `departments/`.
3. In Snowflake: create DB, schema, file formats, tables via `snowflake/ddl.sql`.
4. Create Storage Integration and External Stage per `snowflake/stage_integration.md`.
5. Verify with `LIST @CURATED_STAGE/` (will be empty until Day 2 output appears).

## Day 2 — EMR Serverless transform → S3 curated
1. Create EMR Serverless app (Spark 7.x). Set idle timeout (e.g., 5–10 min).
2. Submit a job using settings in `emr/job-config.md`.
3. Output to `s3://instacart-curated-<you>/fact_sales/dt=YYYY-MM-DD/` etc.
4. Capture screenshots of job metrics and S3 partitions.

## Day 3 — Airflow orchestration + Snowflake COPY
1. Configure Airflow Connections (`aws_default`, `snowflake_default`) per `airflow/connections.md`.
2. Deploy DAG `airflow/dags/retail_etl_dag.py` and trigger.
3. Inspect task graph → EMR job → Snowflake COPY steps.
4. Capture screenshots of successful runs & Snowflake COPY History.
