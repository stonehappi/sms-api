from fastapi import Request
from fastapi.responses import JSONResponse
from core.startup import startup, reset_factory
from modules.routes import set_route

app = startup()


@app.middleware("http")
async def errors_handling(request: Request, call_next):
    try:
        return await call_next(request)
    except Exception as exc:
        return JSONResponse(status_code=500, content={"message": str(exc)})


set_route(app)


@app.get("/")
async def welcome():
    return f"Welcome to SCA"


@app.get("/reset/{secret}")
async def reset(secret: str):
    if secret != "sca":
        return "Wrong secret"
    reset_factory()
    return "Factory reset"
