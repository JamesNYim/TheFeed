from fast.api.middleware.cores import CORSMiddleware
import fastapi import Request

def add_middleware(app):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["http://localhost:3000"], #.env variable?
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
