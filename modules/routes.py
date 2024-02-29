from fastapi import FastAPI


def set_route(app: FastAPI):
    from modules.Position.controller import router as position_router
    
    app.include_router(position_router)
