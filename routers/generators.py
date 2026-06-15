from fastapi import APIRouter
import string
import secrets
import uuid
import random
import unicodedata

router = APIRouter(prefix="/generators", tags=["Generators"])

# Collection of simple utility generator endpoints
@router.get("/")
async def generators():
    return {"endpoints": ["password", "uuid", "slug", "color"]}

# Password generator endpoint
@router.get("/password")
async def passwordGen(long: int, useCharacters: bool):
    if useCharacters:
        char_pool = string.ascii_letters + string.digits + string.punctuation
    else:
        char_pool = string.digits + string.ascii_letters

    password = "".join(secrets.choice(char_pool) for _ in range(long))

    return {"password":password}

# UUID generator endpoint
@router.get("/uuid")
async def uuidGen(useHex: bool):
    if useHex is False:
        genUUID = uuid.uuid4()
    else:
        genUUID = uuid.uuid4().hex

    return {"uuid":f"{str(genUUID)}"}

# Slug conversion endpoint
@router.get("/slug")
async def slugGen(text: str):
    normalized = unicodedata.normalize("NFKD", text)
    clean = "".join(c for c in normalized if not unicodedata.combining(c))
    slug = clean.lower().replace(" ", "-")
    return {"slug": slug}

# Random color generator endpoint
@router.get("/color")
async def colorGen():
    return {"color":f"#{random.randint(0, 0xFFFFFF):06x}"}
