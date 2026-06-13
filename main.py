from fastapi import FastAPI
import string
import secrets
import uuid
import random
import unicodedata

app = FastAPI(title="DevTools API", version="0.1.0")

@app.get("/")
async def root():
    return {"message":"Welcome to DevTools API by @g4bu.dev"}

# Collection of simple utility generator endpoints
@app.get("/generators")
async def generators():
    return {"endpoints": ["password", "uuid", "slug", "color"]}

# Password generator endpoint
@app.get("/generators/password")
async def passwordGen(long: int, useCharacters: bool):
    if useCharacters:
        char_pool = string.ascii_letters + string.digits + string.punctuation
    else:
        char_pool = string.digits + string.ascii_letters

    password = "".join(secrets.choice(char_pool) for _ in range(long))

    return {"password":password}

# UUID generator endpoint
@app.get("/generators/uuid")
async def uuidGen(useHex: bool):
    if useHex is False:
        genUUID = uuid.uuid4()
    else:
        genUUID = uuid.uuid4().hex

    return {"uuid":f"{str(genUUID)}"}

# Slug conversion endpoint
@app.get("/generators/slug")
async def slugGen(text: str):
    normalized = unicodedata.normalize("NFKD", text)
    clean = "".join(c for c in normalized if not unicodedata.combining(c))
    slug = clean.lower().replace(" ", "-")
    return {"slug": slug}

# Random color generator endpoint
@app.get("/generators/color")
async def colorGen():
    return {"color":f"#{random.randint(0, 0xFFFFFF):06x}"}