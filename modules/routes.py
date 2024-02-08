from fastapi import FastAPI


def set_route(app: FastAPI):
    from modules.user.controller import router as user_router

    app.include_router(user_router)

    from modules.teacher.controller import router as teacher_router

    app.include_router(teacher_router)

    from modules.position.Controller import router as Position_router

    app.include_router(Position_router)