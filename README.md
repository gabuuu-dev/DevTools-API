<h1 align="center">DevTools API</h1>

<p align="center">A free, open-source utility API for developers. No authentication required.</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white" alt="FastAPI" />

---


### What is this?

DevTools API is a collection of small, useful endpoints for everyday developer tasks — generating passwords, UUIDs, slugs, and more. It is designed to be simple enough for beginners to use and understand.

### Installation

Clone the repository and set up a virtual environment:

```bash
git clone https://github.com/your-username/devtools-api
cd devtools-api
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

### Project structure

```
devtools-api/
├── main.py              # Entry point — starts the app
├── requirements.txt     # Project dependencies
├── .gitignore           # Files excluded from Git
└── README.md
```

### Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.