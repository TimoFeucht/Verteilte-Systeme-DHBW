# Distributed Systems Project: *Verteiltes Lernsystem mit adaptiver Schwierigkeitsanpassung*
This project is for the module *Verteilte Systeme* of the [DHBW Stuttgart](https://www.dhbw-stuttgart.de/).
The project is called *Verteiltes Lernsystem mit adaptiver Schwierigkeitsanpassung*.

This project contains: 
- [Frontend](verteilte_systeme_dhbw/frontend/README.md)
- [Backend with rqlite](verteilte_systeme_dhbw/backend-rqlite/README.md)
- [Backend with MongoDB](verteilte_systeme_dhbw/backend-mongodb/README.md)

## Frontend
The frontend is a simple console application that allows the user to interact with the backend. 

## Backend
The backend is a REST API written with [FastAPI](https://fastapi.tiangolo.com//) and is responsible for the communication with the database (rqlite or MongoDB). 
The database is a distributed [rqlite](https://rqlite.io/) database or a [MongoDB](https://www.mongodb.com/) cluster.

**Important:** The finished project will be running with MonoDB, rqlite is just for testing purposes during the development.

****

# Setting up the project
## Backend
The backend on the Raspberry Pi is started via a service ([lernsysteme.service](verteilte_systeme_dhbw/backend-mongodb/lernsystem.service)) and should therefor start and run automatically.
The login credentials for the MongoDB-Cluster are already saved on the Raspberry Pi.

If the backend doesn't start or you want to run the backend locally, follow the steps in the README for the [Backend with MongoDB](verteilte_systeme_dhbw/backend-mongodb/README.md).

If clone this project, create your own cluster with [MongoDB Atlas](https://www.mongodb.com/atlas/database) and past the login-credentials into a file named `.env` located in `verteilte_systeme_dhbw/backend-mongodb/`.
Set the following variables to your own login credentials:
````
MONGODB_URL=mongodb+srv://[username:password@]host[/[defaultauthdb][?options]]
MONGODB_NAME=[db_name]
````

## Frontend
**TODO: Write steps**