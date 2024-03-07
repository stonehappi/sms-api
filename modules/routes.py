from fastapi import FastAPI


def set_route(app: FastAPI):
    from modules.Company.Controller import router as Company_router
    app.include_router(Company_router)
    from modules.Contact.Controller import router as Contact_router
    app.include_router(Contact_router)
    from modules.Position.Controller import router as Position_router
    app.include_router(Position_router)
    from modules.Email.Controller import router as Email_router
    app.include_router(Email_router)
    from modules.Phone.Controller import router as Phone_router
    app.include_router(Phone_router)
