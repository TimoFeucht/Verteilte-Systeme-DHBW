# Backend for the distributed systems project _Lernsystem_ at DHBW Stuttgart with MongoDB

## Start backend locally
If you want to run the backend locally for development or testing, execute this command.
Make sure you are in the folder `verteilte_systeme_dhbw/backend-mongodb` when executing this command.
```bash
python -m uvicorn mongodb_app.main:app --reload
```
The backend is now accessible at the URL [http://127.0.0.1:8000/](http://127.0.0.1:8000/).
You can have a look at the REST API at [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).

## Start backend on Raspberry Pi
The backend on the Raspberry Pi is started via a service ([lernsysteme.service](lernsystem.service)) and should therefor start and run automatically.
You can check the status of the service with the following command in the terminal on the Raspberry Pi:
```bash
sudo systemctl status lernsysteme
```
If the backend doesn't start, you can start the backend via uvicorn or run the file [start_backend.py](start_backend.py).
If you want to start the backend via uvicorn on the Raspberry Pi, please use the following command:
```bash
python -m uvicorn mongodb_app.main:app --reload --host=0.0.0.0 --port=9000
```
Make sure you are in the folder `verteilte_systeme_dhbw/backend-mongodb` when executing this command.