from typing import Optional
from urllib import request
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


@app.get('/')
def index():
    return {'data': {
        'name': 'Blog list'
    }}


@app.get('/blog')
# fetch blog with id = id
def limitBlog(limit=10, published: bool = True, sort: Optional[str] = None):
    if published:
        return {'data': f'{limit} published blogs'}
    else:
        return {'data': f'{limit} all blogs from db'}


@app.get('/blog/unpublished')
# fetch blog with id = id
def unpublished():
    return {'data': 'Unpublished blog'}


@app.get('/blog/{id}')
# fetch blog with id = id
def getblog(id: int):
    return {'data': id}


@app.get('/blog/{id}/comments')
def getCommemts(id):
    return {'data': {'1', '2'}}


@app.get('/about')
def Notabout():
    return{'data': {
        'Des': 'FE'
    }}


# post request ======
class Blog(BaseModel):
    Title: str
    body: str
    published: Optional[bool]


@app.post('/addBlog')
def create_blog(request: Blog):
    return {'data': f"Blog is added:{request.Title}",
            'values': request
            }
