<h1 align="center">DevTools API</h1>

<p align="center">A free, open-source utility API for developers. No authentication required.</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white" alt="FastAPI" />
  <img src="https://img.shields.io/github/actions/workflow/status/gabuuu-dev/DevTools-API/tests.yml?style=for-the-badge&label=tests" alt="Tests" />
</p>

---

### What is this?

DevTools API is a collection of small, useful endpoints for everyday developer tasks — generating passwords, UUIDs, slugs, and more. It is designed to be simple enough for beginners to use and understand.

### Installation

Clone the repository and set up a virtual environment:

```bash
git clone https://github.com/gabuuu-dev/DevTools-API.git
cd DevTools-API
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### Running the API

```bash
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`.
Interactive documentation (Swagger UI) is available at `http://localhost:8000/docs`.

### Running the tests

This project uses [pytest](https://docs.pytest.org/) to automatically test every endpoint.

Install the extra dependencies needed for testing:

```bash
pip install -r requirements-dev.txt
```

Then run the test suite:

```bash
pytest
```

Add `-v` to see each individual test and its result:

```bash
pytest -v
```

---

### Endpoints

#### Generators

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/generators/password` | Generates a secure random password |
| GET | `/generators/uuid` | Generates a UUID v4 |
| GET | `/generators/slug` | Converts text to a URL-friendly slug |
| GET | `/generators/color` | Generates a random HEX color |

#### Password generator parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `long` | integer | Yes | Length of the password |
| `useCharacters` | boolean | Yes | Include special characters (`true` / `false`) |

Example:

```
GET /generators/password?long=16&useCharacters=true
```

```json
{
  "password": "aB3$kL9!mZ2#qR7@"
}
```

#### UUID generator parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `useHex` | boolean | Yes | Return UUID without hyphens (`true` / `false`) |

Example:

```
GET /generators/uuid?useHex=false
```

```json
{
  "uuid": "550e8400-e29b-41d4-a716-446655440000"
}
```

#### Slug generator parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `text` | string | Yes | Text to convert |

Example:

```
GET /generators/slug?text=Hello World
```

```json
{
  "slug": "hello-world"
}
```

#### Color generator

No parameters needed.

```
GET /generators/color
```

```json
{
  "color": "#a3f2c1"
}
```

---

#### Validators

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/validators/email` | Checks whether a string is a valid email address |
| POST | `/validators/url` | Checks whether a string is a valid URL |
| POST | `/validators/json` | Checks whether a string is valid JSON |
| POST | `/validators/credit-card` | Checks whether a number is a valid credit card number (Luhn algorithm) |
| GET | `/validators/ip/{ip}` | Checks whether a string is a valid IP address (IPv4 or IPv6) |

#### Email validator parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `email` | string | Yes | The email address to check |

Example:

```
POST /validators/email?email=test@example.com
```

```json
{
  "valid": true
}
```

#### URL validator parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `url` | string | Yes | The URL to check |

Example:

```
POST /validators/url?url=https://github.com
```

```json
{
  "valid": true
}
```

#### JSON validator parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `data` | string | Yes | The text to check |

Example:

```
POST /validators/json?data={"name": "Carlos"}
```

```json
{
  "valid": true,
  "parsed": {
    "name": "Carlos"
  }
}
```

If the text is not valid JSON, the response includes an `error` field explaining what went wrong instead of `parsed`.

#### Credit card validator parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `cc_number` | string | Yes | The card number to check. Spaces and dashes are allowed |

Example:

```
POST /validators/credit-card?cc_number=4532015112830366
```

```json
{
  "valid": true
}
```

#### IP validator parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `ip` | string | Yes | The IP address to check (part of the URL path) |

Example:

```
GET /validators/ip/192.168.1.1
```

```json
{
  "valid": true,
  "version": 4,
  "is_private": true
}
```

---

### Project structure

```
devtools-api/
├── .github/
│   └── workflows/
│       └── tests.yml               # Runs the test suite automatically on every push
├── main.py                          # Entry point — starts the app
├── routers/
│   ├── __init__.py
│   ├── generators.py                # Password, UUID, slug and color endpoints
│   └── validators.py                # Email, URL, JSON, credit card and IP endpoints
├── tests/
│   ├── __init__.py
│   ├── conftest.py                  # Shared test client used by every test file
│   ├── test_generators.py
│   └── test_validators.py
├── requirements.txt                 # Dependencies needed to run the API
├── requirements-dev.txt             # Extra dependencies needed to run the tests
├── .gitignore                       # Files excluded from Git
└── README.md
```

### Continuous Integration

Every time code is pushed to this repository, GitHub Actions automatically installs the dependencies and runs the full test suite. You can see the result of each run in the **Actions** tab of the repository, and the badge at the top of this README always shows whether the latest run passed.

### Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.