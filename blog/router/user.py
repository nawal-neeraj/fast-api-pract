from fastapi import APIRouter, Depends, status, Response
from typing import List
from sqlalchemy.orm import Session
from .. import schema, database
from ..services import user
from .. import schema

router = APIRouter(
    tags=['user'],
    prefix="/user"
)
get_db = database.get_db

@router.post('/', response_model=schema.UserShow, tags=['user'])
def create_user(request: schema.User, db: Session = Depends(get_db)):
    return user.usercreate(db, request)


@router.get('/{id}', status_code=status.HTTP_404_NOT_FOUND, response_model=schema.UserShow, tags=['user'])
def getuser(id, response: Response, db: Session = Depends(get_db)):
    return user.getuser(id, db)
