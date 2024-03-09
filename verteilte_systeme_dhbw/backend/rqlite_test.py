import json

import requests

# 1. Run rqlite with the following command:
# cd C:\Users\Timo\AppData\Local\Programs\rqlite\rqlite-latest-win64
# ./rqlited -node-id 1 -http-addr 127.0.0.1:4001 -raft-addr 127.0.0.1:4002 C:\Users\Timo\AppData\Local\Programs\rqlite\db-verteilteSysteme

# or easier after adding rqlite to path-variables:
# rqlited -node-id 1 -http-addr 127.0.0.1:4001 -raft-addr 127.0.0.1:4002 C:\Users\Timo\AppData\Local\Programs\rqlite\db-verteilteSysteme

# Optional: Specify the path to the database file (C:\Users\Timo\AppData\Local\Programs\rqlite\db-verteilteSysteme), the node id (-node-id 1) and the addresses (-http-addr and -raft-addr).
# - node-id: This can be any string, as long as it’s unique in the (cluster
# - http-addr: This is the address and port I’m going to use for the HTTP interface, which is also used by the rqlite command-line client, etc.
# - raft-addr: This is the address and port that other nodes will connect to for intra - cluster traffic.
# - C:\Users\Timo\AppData\Local\Programs\rqlite\db: This directory will hold the database and state inforamtion.

# Optional: Use rqlite shell
# a) make sure rqlite is in path-variables (Test with rqlite --version)
# b) connect to node with `rqlite -H 127.0.0.1 -p 4001`
# c) execute SQL commands

# 2. Run the following code to create a new planet and get all planets:

url_execute = 'http://127.0.0.1:4001/db/execute'
url_query = 'http://127.0.0.1:4001/db/query'

params_get = {
    'q': 'SELECT * FROM questions;',
}

headers = {'Content-Type': 'application/json'}
# params_post = json.dumps([
#     """INSERT INTO planets (from_sun, name) VALUES (5, "Earth");"""
# ])
#
# # create a new planet
# response = requests.post(url_execute, headers=headers, data=params_post)
# print(response.status_code)
# print(response.json())

# get all planets
response = requests.get(url_query, headers=headers, params=params_get)
print(response.status_code)
print(response.json())
