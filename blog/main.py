from fastapi import FastAPI
from . import model
from .database import engine
from .router import blog, user, auth

app = FastAPI()

model.Base.metadata.create_all(engine)

app.include_router(blog.router)
app.include_router(user.router)
app.include_router(auth.router)
