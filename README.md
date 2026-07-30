# 🌦️ Automated Weather Data Pipeline

An end-to-end **weather data engineering pipeline** that collects weather data from the Weatherstack API, stores it in PostgreSQL, orchestrates workflows using Apache Airflow, transforms data with dbt, and visualizes insights using Apache Superset.

This project demonstrates a modern data engineering workflow:



---

# 🚀 Project Overview

The pipeline performs the following operations:

1. Extracts weather data from the Weatherstack API
2. Loads raw weather records into PostgreSQL
3. Automates pipeline execution using Apache Airflow
4. Transforms raw data into analytics-ready datasets using dbt
5. Creates dashboards and visualizations using Apache Superset

The entire platform runs locally using Docker Compose.

---

# ✨ Features

- ✅ Automated weather data ingestion
- ✅ PostgreSQL data storage
- ✅ Apache Airflow workflow orchestration
- ✅ dbt data transformation layer
- ✅ Apache Superset visualization
- ✅ Dockerized environment
- ✅ Reproducible local deployment
- ✅ Modular data engineering architecture

---

# 🏗️ Architecture

```
                    Weatherstack API
                          |
                          |
                          v
                      Ingestion 
                          |
                          |
                          v
                    transformation                         
                          |
                          |
                          v
                  Apache Superset
                Analytics & Dashboards
```

---

# 🛠️ Technology Stack

| Technology |
|------------|
| Python | 
| Weatherstack API |
| PostgreSQL |
| Apache Airflow |
| dbt | 
| Apache Superset | 
| Docker Compose | 


---

# 📋 Prerequisites

Before starting, install the following:

## Required

- Docker Desktop (Windows/macOS)
- Docker Engine + Docker Compose v2 (Linux)
- Git
- Weatherstack API key


## Optional but Useful

- WSL2 (Windows users who prefer a Linux-based development environment)
- Python 3.10+ for local debugging
- Visual Studio Code
- VS Code Remote - WSL extension

# 📥 Installation

## 1. Clone the Repository

```bash
git clone https://github.com/MuweenM/automated-weather-data-pipeline-.git

cd weather-data-project
```

## Important

Keep the project folder name:

```
weather-data-project
```

The Airflow DAG expects the default Docker network:

```
weather-data-project_my-network
```

If you clone the repository using another folder name, update the network name inside:

```
airflow/dags/orchestrator.py
```

---

# 2. Configure Environment Variables

Create a `.env` file in the project root:

```env
WEATHERSTACK_API_KEY=your_weatherstack_api_key_here
```

You can modify default service configurations inside:

```
docker/.env
```

---

# 3. Start the Containers

Run:

```bash
docker compose up -d
```

This starts the following services:

| Service | Port |
|---------|------|
| PostgreSQL | 5000 |
| Airflow | 8000 |
| Superset | 8088 |
| Redis | Internal |
| dbt | Container |

Check running services:

```bash
docker compose ps
```

View logs:

```bash
docker compose logs -f af
```

---

# 🌐 Access Applications

After the containers are running:

| Application | URL |
|-------------|-----|
| Airflow UI | http://localhost:8000 |
| Superset UI | http://localhost:8088 |

---

# 🔑 Default Credentials

## Superset Login

```
Username: admin
Password: admin
```

---

# 🗄️ Database Configuration

PostgreSQL connection details:

```
Host: localhost
Port: 5000
Database: db
Username: db_user
Password: db_password
```

Raw weather table:

```
dev.raw_weather_data
```

---

# 🌦️ Running Weather Data Ingestion

The ingestion script retrieves weather information from Weatherstack and inserts it into PostgreSQL.

Run manually:

```bash
docker compose exec af python /opt/airflow/api-request/insert_records.py
```

After execution, weather records will be stored in:

```
dev.raw_weather_data
```

---

# 🔄 Running dbt Transformations

dbt handles:

- Data cleaning
- Data modeling
- Transformation logic
- Analytics-ready datasets

---

# ⚙️ Airflow Pipeline

The main Airflow DAG:

```
weather-api-dbt-orchestrator
```

Pipeline workflow:

```
Extract Weather Data
          |
          v
Load Data Into PostgreSQL
          |
          v
Run dbt Transformation
```

The DAG can be triggered manually from the Airflow web interface.

---

# 📂 Project Structure

```
weather-data-project/

├── api-request/
│   └── Weather API ingestion scripts
│
├── airflow/
│   └── Airflow DAG definitions
│
├── dbt/
│   └── dbt models 
│
├── docker/
│   └── Docker configurations
│
├── postgres/
│   └── Database initialization scripts
│
├── docker-compose.yml
└── .env
```

---

# 🧰 Useful Commands

## Stop containers

```bash
docker compose down
```

## Stop containers and remove volumes

```bash
docker compose down -v
```

## Rebuild containers

```bash
docker compose up -d --build
```

## View logs

```bash
docker compose logs -f
```

---

# 🐛 Troubleshooting

## Docker is not running

Make sure:

- Docker Desktop is running
- Docker Engine service is active

---

## Docker Compose not found

Verify installation:

```bash
docker compose version
```

Install Docker Compose v2 if unavailable.

---

## Airflow cannot access Docker

Check:

- Docker daemon is running
- User permissions allow Docker socket access

Linux users may need access to:

```
/var/run/docker.sock
```

---

## Database connection errors

PostgreSQL may require a few minutes to initialize.

Check logs:

```bash
docker compose logs postgres
```

---

## Missing weather data

Check:

1. `.env` file exists
2. Weatherstack API key is valid
3. Ingestion script completed successfully

---

## Airflow network errors

Ensure the project folder is named:

```
weather-data-project
```

Otherwise update the network configuration:

```
airflow/dags/orchestrator.py
```



# 👨‍💻 Author

**Muween M**

Data Engineering project demonstrating:

- ETL pipeline development
- Workflow orchestration
- Data transformation
- Analytics engineering
- Containerized infrastructure

---

# ⭐ Support

If you find this project useful, consider giving it a ⭐ on GitHub.
