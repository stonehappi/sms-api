from fastapi import FastAPI


def set_route(app: FastAPI):
    from modules.Phone.controller import router as phone_router
    app.include_router(phone_router)
    from modules.contact.controller import router as contact_router
    app.include_router(contact_router)
    from modules.company.controller import router as company_router
    app.include_router(company_router)
    from modules.position.controller import router as position_router
    app.include_router(position_router)
    from modules.email.controller import router as email_router
    app.include_router(email_router)
    
    
