CREATE OR REPLACE STAGE curated_stage
  URL='s3://instacart-curated-<your-name>-<date>/instacart/curated/'
  STORAGE_INTEGRATION = s3_instacart_integration;

LIST @curated_stage;  -- should work once the AWS role is created
