from fastapi import FastAPI


def set_route(app: FastAPI):
    from modules.Contact.controller import router as Contact_router
    app.include_router(Contact_router)

    from modules.Position.controller import router as Position_router
    app.include_router(Position_router)

    from modules.Company.controller import router as Company_router
    app.include_router(Company_router)

    from modules.Phone.controller import router as Phone_router
    app.include_router(Phone_router)

    from modules.Email.controller import router as Email_router
    app.include_router(Email_router)

    from modules.student.controller import router as Student_router
    app.include_router(Student_router)