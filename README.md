# emr-serverless-retail-etl
Built a batch ETL pipeline using AWS S3, EMR Serverless (Spark), Snowflake, and Airflow on EC2. Ingested Instacart data to S3, transformed CSV to partitioned Parquet, and loaded curated data into Snowflake via external stage and COPY INTO. Added DQ checks, idle timeout tuning, and cost optimization for cents-per-run execution.
