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
   
    return f"Habibi Welcome To Hell"


@app.get("/reset/{secret}")
async def reset(secret: str):
    if secret != "sca":
        return "Wrong secret"
    reset_factory()


numbers = [1, 2, 3, 34]
number = 3
contact_types = ["phone", "email", "address"]
contact_type = "phone, email, address"
