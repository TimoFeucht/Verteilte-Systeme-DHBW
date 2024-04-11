#!/usr/bin/python3

import uvicorn

if __name__ == "__main__":
    # use host="0.0.0.0" for Raspberry Pi
    # use host="127.0.0.1" for local development
    uvicorn.run("mongodb_app.main:app", host="0.0.0.0", port=9000, reload=True)


# #!/usr/bin/python3
#
# import uvicorn
# import subprocess
#
# if __name__ == "__main__":
#     # use host="0.0.0.0" for Raspberry Pi
#     # use host="127.0.0.1" for local development#
#     get_ip_command = "hostname -I | awk '{print $1}'"
#     host_ip = subprocess.check_output(get_ip_command, shell=True).decode().strip()
#     uvicorn_command = f"uvicorn mongodb_app.main:app --reload --port 9000 --host {host_ip}"
#
#     subprocess.run(uvicorn_command, shell=True, check=True)
