FROM python:3.11.7

# Das Basis-Verzeichnis für den Code im Container festlegen
WORKDIR /app

# Die Dateien 'pyproject.toml' und 'poetry.lock' (falls vorhanden) in das Verzeichnis '/app' kopieren
COPY ./pyproject.toml ./poetry.lock* /app/

# Poetry installieren und das Erstellen von virtuellen Umgebungen deaktivieren
RUN pip install poetry && poetry config virtualenvs.create false

# Abhängigkeiten installieren, ohne das Projekt selbst zu installieren
RUN poetry install --no-root --no-dev

# Den gesamten Projektcode in das Verzeichnis '/app' kopieren
COPY ./verteilte_systeme_dhbw/backend/sql_app .

# Die Umgebungsvariablen (optional) aus einer .env Datei setzen
# ENV USER=youruser
# ENV PASSWORD=yourpassword

# Den Uvicorn-Server starten
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
# CMD ["uvicorn", "app.main:app", "--reload"]