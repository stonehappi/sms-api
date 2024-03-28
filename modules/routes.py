from fastapi import FastAPI


def set_route(app: FastAPI):
    from modules.Position.Controller import router as position_router 

    app.include_router(position_router)

    from modules.Phone.Controller import router as phone_router 

    app.include_router(phone_router)

    from modules.Contact.controller import router as contact_router 

    app.include_router(contact_router)

    from modules.Email.Controller import router as Email_router 

    app.include_router(Email_router)

    from modules.Company.Controller import router as company_router 

    app.include_router(company_router)

    from modules.Student.Controller import router as Student_router
    app.include_router(Student_router)