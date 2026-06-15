# Verifies that the password generator creates a password with the specified length
def test_password_length(client):
    response = client.get("/generators/password", params={"long": 16, "useCharacters": True})
    assert response.status_code == 200
    assert len(response.json()["password"]) == 16

# Checks that the password contains only alphanumeric characters when special characters are disabled
def test_password_without_special_characters(client):
    response = client.get("/generators/password", params={"long": 12, "useCharacters": False})
    password = response.json()["password"]
    assert all(c.isalnum() for c in password)

# Validates that a UUID with dashes has the correct length of 36 characters
def test_uuid_with_dashes(client):
    response = client.get("/generators/uuid", params={"useHex": False})
    assert len(response.json()["uuid"]) == 36

# Confirms that a hexadecimal UUID format has the correct length of 32 characters
def test_uuid_hex_format(client):
    response = client.get("/generators/uuid", params={"useHex": True})
    assert len(response.json()["uuid"]) == 32

# Tests that text is properly converted to a URL-friendly slug format
def test_slug_conversion(client):
    response = client.get("/generators/slug", params={"text": "Hello World"})
    assert response.json()["slug"] == "hello-world"

# Ensures the generated color is in valid hex format (#RRGGBB)
def test_color_format(client):
    response = client.get("/generators/color")
    color = response.json()["color"]
    assert color.startswith("#")
    assert len(color) == 7