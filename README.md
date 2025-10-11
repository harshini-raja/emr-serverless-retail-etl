# emr-serverless-retail-etl
Built a batch ETL pipeline using AWS S3, EMR Serverless (Spark), Snowflake, and Airflow on EC2. Ingested Instacart data to S3, transformed CSV to partitioned Parquet, and loaded curated data into Snowflake via external stage and COPY INTO. Added DQ checks, idle timeout tuning, and cost optimization for cents-per-run execution.

# EMR Serverless Retail ETL — cents-per-run batch analytics on AWS > Cost-optimized batch retail pipeline on AWS: **S3 → EMR Serverless (Spark) → Snowflake**, orchestrated by **Airflow on EC2**. Partitioned Parquet, DQ gates, and autosuspend/idle timeouts to keep runs in cents. ![Social preview banner placeholder](./screenshots/banner.png) ## Architecture (Mermaid)
mermaid
flowchart LR
A[Instacart dataset
(S3 raw)] --> B[EMR Serverless
Spark job]
B --> C[S3 curated
Parquet + partitions]
C --> D[Snowflake External Stage]
D --> E[COPY INTO
Snowflake tables]
subgraph Orchestration
F[Airflow on EC2]
end
F -. Schedules/Triggers .-> B
F -. COPY tasks .-> E"
