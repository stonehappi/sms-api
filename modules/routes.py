from fastapi import FastAPI


def set_route(app: FastAPI):
    from modules.Company.Controller import router as Company_router
    app.include_router(Company_router)