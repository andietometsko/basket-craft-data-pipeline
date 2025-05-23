This project builds a complete end-to-end ELT pipeline for analyzing website session data from Basket Craft. Using Python scripts, data is extracted from an AWS RDS MySQL database and loaded into a raw layer in Postgres. GitHub Actions automates the data extraction and loading process every 15 minutes. dbt is used to transform raw data into staging and warehouse and marts models, including a daily fact table that calculates repeat session metrics by UTM source. The final dataset is visualized in Looker Studio with interactive charts, enabling stakeholders to explore session trends and engagement by traffic source. All code, transformations, and deployment workflows are version-controlled using Git and GitHub.

![Data Pipeline](pipeline-diagram.jpeg)

Dashboard: [https://lookerstudio.google.com/reporting/6092817c-1511-479b-9efa-6d9bfb59e5a4]
