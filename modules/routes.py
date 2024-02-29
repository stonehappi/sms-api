from fastapi import FastAPI


def set_route(app: FastAPI):
    from modules.user.controller import router as user_router

    app.include_router(user_router)

    from modules.teacher.controller import router as teacher_router

    app.include_router(teacher_router)
    
    from modules.staff.controller import router as staff_router

    app.include_router(staff_router)

    from modules.Company.controller import router as Company_router

    app.include_router(Company_router)
