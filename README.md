# 🚀 Modern Data Engineering Project with Snowflake, dbt, Airflow

### 📌 Overview
### This project demonstrates a modern Data Engineering pipeline using:

Snowflake as the cloud data warehouse   
dbt (Data Build Tool) for data modeling and transformation   
Apache Airflow for workflow orchestration with CeleryExecutor   
Docker for containerization and environment setup   
 
### The data consists of 4 CSV files:

orders.csv  
order_items.csv  
products.csv  
customers.csv  

#### These files are uploaded to a Snowflake stage named sales_stage, and then loaded into raw tables via COPY INTO. dbt is used to transform the raw data into structured models under staging and marts layers.

### ⚙️ Technologies Used
Tool	Role
Snowflake	Cloud data warehouse
dbt	Data transformation and modeling
Airflow	Workflow orchestration
Power BI	Dashboard and visualization
Docker	Containerization and environment setup
