from sqlalchemy.orm import Session
from .. import model
from ..hashing import Hash
from fastapi import status, HTTPException


def usercreate(db: Session, request):
    new_blog = model.User(
        name=request.name, email=request.email, password=Hash.bcrypt(request.password))
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


def getuser(id, db: Session):
    blog = db.query(model.User).filter(model.User.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'details of id {id} not found')
    return blog
