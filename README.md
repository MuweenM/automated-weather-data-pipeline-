# Weather Data Project

This project collects weather data, stores it in PostgreSQL, and uses Airflow and dbt for orchestration and transformation.

## Structure
- api-request/: scripts for fetching and inserting weather data
- airflow/: Airflow DAGs and configuration
- dbt/: dbt models and project files
- docker/: container setup for the services
- postgres/: database initialization scripts and local data volume

## Getting started
1. Clone the repository.
2. Start the services with Docker Compose.
3. Run the ingestion script to populate the database.

```bash
docker compose up -d
```
