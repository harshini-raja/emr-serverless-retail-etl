USE ROLE ACCOUNTADMIN;

-- 1) Create the integration (the IAM role does NOT need to exist yet)
CREATE OR REPLACE STORAGE INTEGRATION s3_instacart_integration
  TYPE = EXTERNAL_STAGE
  STORAGE_PROVIDER = S3
  ENABLED = TRUE
  STORAGE_AWS_ROLE_ARN = 'arn:aws:iam::058264291892:role/snowflake-s3-instacart-role'
  STORAGE_ALLOWED_LOCATIONS = ('s3://instacart-curated-harshini-20251002/');

-- 2) Get the two values you need to build the AWS trust policy
DESC INTEGRATION s3_instacart_integration;
-- copy: STORAGE_AWS_IAM_USER_ARN and STORAGE_AWS_EXTERNAL_ID

