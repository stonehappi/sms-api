from fastapi import FastAPI


def set_route(app: FastAPI):
    from modules.user.controller import router as user_router

    app.include_router(user_router)

    from modules.teacher.controller import router as teacher_router

    app.include_router(teacher_router)

    from modules.building.controller import router as building_router

    app.include_router(building_router)
