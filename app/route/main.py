from fastapi import FastAPI

from app.route import useroute, bookdataroutes, authentication

from app.database import engine, Base


Base.metadata.create_all(bind=engine) 
# Base.metadata.drop_all(bind=engine)


app = FastAPI()

app.include_router(authentication.router)

app.include_router(useroute.router)

app.include_router(bookdataroutes.router)
