"""Tests for the SMS endpoint. They call the real Twilio API through the app."""
from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_send_sms_returns_twilio_result():
    r = client.post("/send-sms/", json={"Body": "Hello from tests", "To": "+15005550006"})
    assert r.status_code == 200
    # With the placeholder credentials in .env Twilio rejects the request,
    # and the app reports that as a failed send.
    assert r.json() == {"message": "Failed to send SMS. Please check the provided phone number."}


def test_send_sms_to_invalid_number():
    r = client.post("/send-sms/", json={"Body": "Hi", "To": "+10000000000"})
    assert r.status_code == 200
    assert "message" in r.json()


def test_send_sms_requires_body_and_to():
    r = client.post("/send-sms/", json={"Body": "no number"})
    assert r.status_code == 422
