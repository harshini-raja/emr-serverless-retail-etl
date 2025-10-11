# Architecture

## Diagram
```mermaid
flowchart TB
subgraph Ingest
RAW[S3 raw: instacart/raw/...]
end
EMR[EMR Serverless (Spark 7.x)]
CURATED[S3 curated: partitioned Parquet]
STAGE[(Snowflake External Stage)]
TBL[(Snowflake Tables)]
AF[Airflow on EC2]

RAW --> EMR --> CURATED --> STAGE --> TBL
AF -. Schedules/Monitors .-> EMR
AF -. COPY tasks .-> TBL
