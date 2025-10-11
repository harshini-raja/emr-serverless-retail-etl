# EMR Serverless Retail ETL — cents-per-run batch analytics on AWS

> Cost-optimized batch retail pipeline on AWS: **S3 → EMR Serverless (Spark) → Snowflake**, orchestrated by **Airflow on EC2**. Partitioned Parquet, DQ gates, and autosuspend/idle timeouts to keep runs in cents.

![Social preview banner placeholder](./screenshots/banner.png)

## Architecture (Mermaid)
```mermaid
flowchart LR
  A[Instacart S3 Raw Data] --> B[EMR Serverless Spark Job]
  B --> C[S3 Curated Parquet Partitions]
  C --> D[Snowflake External Stage]
  D --> E[Snowflake Tables via COPY INTO]
  E --> G[Amazon QuickSight Dashboards]
  subgraph Orchestration
  F[Airflow on EC2]
  end
  F -. schedules and triggers .-> B
  F -. copy tasks .-> E
