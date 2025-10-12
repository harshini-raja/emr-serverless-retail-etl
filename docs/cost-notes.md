Cost Notes
- **EMR Serverless**: small Spark job ~\$0.10–\$0.30/run with minimal vCPU/GB-hours; set idle timeout to ~5–10 min.
- **S3**: pennies for storage; enable lifecycle rules for raw to infrequent access after 30 days.
- **Snowflake**: use `WH_XS` and `AUTO_SUSPEND = 60` seconds; runs take seconds → sub-cent costs per COPY.
- **EC2 (Airflow)**: t3.small or t3.micro; stop instance when not in use.

**Guardrails**: budget alerts, stop EC2 nightly, review EMR completed applications, disable auto-refreshing queries.
