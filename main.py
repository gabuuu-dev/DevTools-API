from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import generators, validators

app = FastAPI(title="DevTools", version="0.2.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Welcome to DevTools by @g4bu.dev"}

app.include_router(generators.router)
app.include_router(validators.router)