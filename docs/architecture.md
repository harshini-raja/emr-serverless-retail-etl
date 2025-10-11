## Architecture

### Diagram
```mermaid
flowchart TB
  subgraph Ingest
    RAW[S3 Raw Data - Instacart Files]
  end

  EMR[EMR Serverless Spark Job]
  CURATED[S3 Curated Parquet Data]
  STAGE[Snowflake External Stage]
  TBL[Snowflake Tables]
  DASH[Amazon QuickSight Dashboards]
  AF[Airflow on EC2]

  RAW --> EMR --> CURATED --> STAGE --> TBL --> DASH
  AF -. schedules and monitors .-> EMR
  AF -. copy tasks .-> TBL
