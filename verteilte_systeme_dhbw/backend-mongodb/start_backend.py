#!/usr/bin/python3
import uvicorn
import subprocess
from dotenv import dotenv_values

config = dotenv_values(".env")

# if __name__ == "__main__":
#     # use host="0.0.0.0" for Raspberry Pi
#     # use host="127.0.0.1" for local development
#     uvicorn.run("mongodb_app.main:app", host="127.0.0.1", port=9000, reload=True)

if __name__ == "__main__":
    ip = config["IP"]
    uvicorn.run("mongodb_app.main:app", host=ip, port=9999, reload=True)
