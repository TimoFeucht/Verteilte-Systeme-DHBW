# Backend for the distributed systems project at DHBW Stuttgart

## Setup - Development without Docker
1. Install Python 3.11.7
2. Install Poetry
3. Install dependencies with poetry
```bash 
poetry install
```
4. Install PostgreSQL
5. Create a database called `verteilte_systeme_db`, a user called `test_user` with password `test_password_123` and give the user all privileges on the database
5. Run the backend with uvicorn
```bash
uvicorn sql_app.main:app --reload
```

## Setup - Development with Docker
1. Use stepts 1-6 from the "Setup - Development without Docker" section
2. Install Docker
3. Run the backend with docker-compose
```bash
docker-compose up --build
```
4. Build container
```bash
  docker build -t verteilte-systeme-backend .
```
5. Run container
```bash
docker run -p 8000:80 verteilte-systeme-backend
```