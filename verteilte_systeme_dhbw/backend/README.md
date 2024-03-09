# Backend for the distributed systems project at DHBW Stuttgart

## Setup - Development without Docker
1. Install Python 3.11.7
2. Install [Poetry](https://python-poetry.org/)
3. Install dependencies with poetry
```bash 
poetry install
```
4. Install [rqlite](https://rqlite.io/)
   - Download the latest release from the [rqlite](https://rqlite.io/docs/install-rqlite/) website
   - Extract the archive and navigate to the extracted folder. Past the folder in the desired location, e.g. `C:\Program Files\rqlite\rqlite-latest-win64`
5. Add folder to environment variable `Path` (e.g. `C:\Program Files\rqlite\rqlite-latest-win64`)
6. Start node with `rqlited -node-id {node id} -http-addr {adress:port} -raft-addr {adress:port} {path to db}`
   - node-id: This can be any string, as long as it’s unique in the (cluster
   - http-addr: This is the address and port I’m going to use for the HTTP interface, which is also used by the rqlite command-line client, etc.
   - raft-addr: This is the address and port that other nodes will connect to for intra - cluster traffic.
   - C:\Users\Timo\AppData\Local\Programs\rqlite\db: This directory will hold the database and state information.
```bash
rqlited -node-id 1 -http-addr 127.0.0.1:4001 -raft-addr 127.0.0.1:4002 ./db-rqlite
```
6. _Optional:_ Start further nodes with `rqlited -node-id {node id} -http-addr {adress:port} -raft-addr {adress:port} {path to db}`
7. _Optional:_ Connect to the cluster via shell to execute SQL commands:
```bash
rqlite -H 127.0.0.1 -p 4001
```
**Warning:** Do not touch the database if you are not sure what you are doing. This can lead to data corruption and loss of data. 
9. _Setup:_ Create the database schema and insert data with file `verteilte_systeme_dhbw/backend/db-model/db-setup.py`. Run the file only out of this README.md file, not out of the `verteilte_systeme_dhbw/backend/db-model` folder.
```bash
python db-model/db-setup.py
```
11. _Optional:_ Test rqlite database
```bash
rqlite -H 127.0.0.1 -p 4001
```
Then enter in the shell:
```sql
SELECT question FROM questions
```
10. Run the backend with uvicorn
```bash
uvicorn sql_app.main:app --reload
```

## Setup - Development with Docker

**not working!!!**

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