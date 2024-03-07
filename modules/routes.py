from fastapi import FastAPI

def set_route(app: FastAPI):
    from modules.Company.controller import router as company_router
    app.include_router(company_router)

    from modules.Position.controller import router as position_router
    app.include_router(position_router)

    from modules.Contact.controller import router as contact_router
    app.include_router(contact_router)


    from modules.Email.controller import router as email_router
    app.include_router(email_router)

    from modules.Phone.controller import router as phone_router
    app.include_router(phone_router)

    from modules.Student.controller import router as student_router
    app.include_router(student_router)




