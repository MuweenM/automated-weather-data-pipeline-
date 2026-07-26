# Weather Data Project

This project collects weather data, stores it in PostgreSQL, orchestrates the pipeline with Airflow, transforms the data with dbt, and visualizes it with Apache Superset.

## What you need
Before you start, install the following on your PC:

- Docker Desktop (Windows/macOS) or Docker Engine with Docker Compose v2 (Linux)
- Git
- A Weatherstack API key (free tier is enough)

Optional but useful:
- Python 3.10+ for local debugging
- VS Code

## 1. Clone the repository
Open a terminal and run:

```bash
git clone <your-repository-url>
cd weather-data-project
```

Important:
- Keep the folder name as weather-data-project.
- The Airflow DAG expects the default Docker network name weather-data-project_my-network.
- If you clone it under a different folder name, update the network name in airflow/dags/orchestrator.py.

## 2. Create the environment file
Create a file named .env in the project root:

```bash
WEATHERSTACK_API_KEY=your_weatherstack_api_key_here
```

You can also review and adjust the default service settings in docker/.env if you need different ports.

## 3. Start the containers
From the project root, run:

```bash
docker compose up -d
```

This will start:
- PostgreSQL on port 5000
- Airflow on port 8000
- Superset on port 8088
- Redis for Superset
- dbt container for transformations

To check that everything is running:

```bash
docker compose ps
```

If you want to see logs:

```bash
docker compose logs -f af
```

## 4. Access the services
After the containers start, open these URLs in your browser:

- Airflow UI: http://localhost:8000
- Superset UI: http://localhost:8088

### Default credentials
- Superset login:
  - Username: admin
  - Password: admin

### Database connection details
- Host: localhost
- Port: 5000
- Database: db
- Username: db_user
- Password: db_password

## 5. Run the weather data ingestion
The ingestion script reads data from Weatherstack and inserts it into the PostgreSQL database.

Run it manually with:

```bash
docker compose exec af python /opt/airflow/api-request/insert_records.py
```

This creates or fills the table dev.raw_weather_data.

## 6. Run the dbt transformation
The dbt container is configured to run the dbt project automatically when the stack starts. If you want to run it again manually:

```bash
docker compose run --rm dbt
```

## 7. Use the Airflow DAG
The DAG named weather-api-dbt-orchestrator is available in Airflow.

It performs the following steps:
1. Ingests weather data
2. Runs the dbt transformation job

You can trigger it from the Airflow UI.

## 8. Useful commands
Stop everything:

```bash
docker compose down
```

Stop everything and remove volumes:

```bash
docker compose down -v
```

Rebuild containers after changes:

```bash
docker compose up -d --build
```

## 9. Troubleshooting
If something does not work, check the following:

- Docker is not running: start Docker Desktop or the Docker service.
- Docker Compose is not found: install the Docker Compose plugin.
- Airflow cannot reach Docker: ensure Docker daemon is running and your user has permission to access /var/run/docker.sock.
- Database connection errors: wait a few minutes for PostgreSQL to finish initializing.
- Missing weather data: make sure WEATHERSTACK_API_KEY is present in the .env file.
- Airflow network errors: keep the project folder named weather-data-project or update the network name in airflow/dags/orchestrator.py.

## Project structure
- api-request/: ingestion scripts
- airflow/: Airflow DAGs
- dbt/: dbt project and models
- docker/: Superset and container bootstrap scripts
- postgres/: database initialization scripts

