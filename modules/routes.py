from fastapi import FastAPI


def set_route(app: FastAPI):
    from modules.user.controller import router as user_router

    app.include_router(user_router)

    from modules.Department.controller import router as department_router

    app.include_router(department_router)
