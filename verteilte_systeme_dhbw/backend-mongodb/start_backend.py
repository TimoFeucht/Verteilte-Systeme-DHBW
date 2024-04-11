#!/usr/bin/python3

import uvicorn

if __name__ == "__main__":
    # use host="0.0.0.0" for Raspberry Pi
    # use host="127.0.0.1" for local development
    uvicorn.run("mongodb_app.main:app", host="0.0.0.0", port=9000, reload=True)
