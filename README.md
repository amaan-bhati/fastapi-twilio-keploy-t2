# FastAPI Twilio SMS service

A small FastAPI app with one endpoint, `POST /send-sms/`, that sends an SMS through the Twilio API.

## Setup

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
```

Put your Twilio credentials in `.env` (`TWILIO_ACCOUNT_SID`, `TWILIO_AUTH_TOKEN`, `TWILIO_NUMBER`).

## Run

```bash
.venv/bin/python -m uvicorn main:app --port 8000
```

## Tests

```bash
.venv/bin/python -m pytest -v
```

The tests call the real Twilio API.
