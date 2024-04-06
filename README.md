# Distributed Systems Project 
Containing the parts
- [Frontend](verteilte_systeme_dhbw/frontend/README.md)
- [Backend](verteilte_systeme_dhbw/backend-rqlite/README.md)

## Frontend
The frontend is a simple console application that allows the user to interact with the backend. 

## Backend
The backend is a REST API as a distributed system written with [FastAPI](https://fastapi.tiangolo.com//) and [Nats](https://nats.io/) that allows the user to interact with the backend.
The backend is also responsible for the communication with the database. 
The database is a distributed [rqlite](https://rqlite.io/) database.