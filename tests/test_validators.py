import pytest

# Checks that the email validator accepts valid emails and rejects invalid ones.
@pytest.mark.parametrize("email, expected", [
    ("test@example.com", True),
    ("test@gmail.com", True),
    ("not-is-an-email", False),
    ("test@example", False),
])
def test_email_validator(client, email, expected):
    response = client.post("/validators/email", params={"email": email})
    assert response.json() == {"valid": expected}

# Checks that the URL validator accepts valid URLs and rejects invalid ones.
@pytest.mark.parametrize("url, expected", [
    ("https://github.com", True),
    ("http://localhost:8000", True),
    ("not-is-an-url", False),
])
def test_url_validator(client, url, expected):
    response = client.post("/validators/url", params={"url": url})
    assert response.json() == {"valid": expected}

# Checks that the credit card validator accepts valid card numbers, including spaced ones.
@pytest.mark.parametrize("cc_number, expected", [
    ("4532015112830366", True),       # valid test number
    ("4532 0151 1283 0366", True),    # test with spaces
    ("1234567812345678", False),
    ("abc123", False),
])
def test_credit_card_validator(client, cc_number, expected):
    response = client.post("/validators/credit-card", params={"cc_number": cc_number})
    assert response.json()["valid"] == expected

# Checks that the IP validator detects IPv4, IPv6, and invalid IPs.
@pytest.mark.parametrize("ip, expected_valid, expected_version", [
    ("192.168.1.1", True, 4),
    ("::1", True, 6),
    ("im-not-an-ip-address", False, None),
])
def test_ip_validator(client, ip, expected_valid, expected_version):
    response = client.get(f"/validators/ip/{ip}")
    data = response.json()
    assert data["valid"] == expected_valid
    if expected_valid:
        assert data["version"] == expected_version

# Checks that valid JSON is parsed correctly and returned as an object.
def test_json_validator_valid(client):
    response = client.post("/validators/json", params={"data": '{"name": "Carlos"}'})
    data = response.json()
    assert data["valid"] is True
    assert data["parsed"] == {"name": "Carlos"}

# Checks that invalid JSON is rejected and returns an error message.
def test_json_validator_invalid(client):
    response = client.post("/validators/json", params={"data": "{name: Carlos}"})
    data = response.json()
    assert data["valid"] is False
    assert "error" in data