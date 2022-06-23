from fastapi import APIRouter, Depends, status, Response, HTTPException
from typing import List
from sqlalchemy.orm import Session
from .. import schema, database, model, outh2
from ..services import blog
from .. import schema

router = APIRouter(
    prefix="/blog",
    tags=['blog']
)
get_db = database.get_db
get_current_user = outh2.get_current_user


@router.get('/', response_model=List[schema.ShowBlog])
def all(db: Session = Depends(get_db), get_current_user: schema.User = Depends(get_current_user)):
    return blog.getAll(db)


@router.post('/', status_code=status.HTTP_201_CREATED)
# Schema.blog is schema's class call
def create(request: schema.Blog, db: Session = Depends(get_db)):
    return blog.create(db, request)


@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=schema.ShowBlog)
def get(id, response: Response, db: Session = Depends(get_db)):
    return blog.getBlog(db, id)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
async def update(id, request: schema.Blog, db: Session = Depends(get_db)):
    return blog.updateblog(db, id, request)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete(id, response: Response, db: Session = Depends(get_db)):
    # for updating db we need to commit
    return blog.deleteBlog(id, db)
