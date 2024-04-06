import requests
import json

# Note: Run this script only once.
# Do not run with "current file", only run this script out of README.md in the backend-rqlite folder.

url_execute = 'http://localhost:4001/db/execute'

headers = {'Content-Type': 'application/json'}

# SQL-Datei einlesen
file_path = 'db-model/sql/db-verteilteSysteme.sql'
with open(file_path, 'r') as file:
    sql_commands = file.read().split(';')  # Annahme, dass jede SQL-Anweisung durch ein Semikolon getrennt ist

sql_commands = [cmd.strip() for cmd in sql_commands if cmd.strip()]

# Umwandlung der SQL-Anweisungen in das erforderliche JSON-Format
params_post = json.dumps(sql_commands).encode('utf-8')

response = requests.post(url_execute, headers=headers, data=params_post)

# Antwort ausgeben
print(response.status_code)
print(response.json())
