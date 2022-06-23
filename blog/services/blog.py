from sqlalchemy.orm import Session
from .. import model
from fastapi import status, HTTPException


def getAll(db: Session):
    blogs = db.query(model.Blog).all()
    return blogs


def create(db, request):
    new_blog = model.Blog(title=request.title, body=request.body, user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


def getBlog(db: Session, id):
    blog = db.query(model.Blog).filter(model.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Details of {id} not available')
    return blog


def updateblog(db: Session, id, request):
    blog = db.query(model.Blog).filter(model.Blog.id == id)
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'details of id {id} not found')
    blog.update({'body': request.body, 'title': request.title})
    db.commit()
    return {'updated'}


def deleteBlog(id, db: Session):
    blog = db.query(model.Blog).filter(model.Blog.id ==
                                       id).delete(synchronize_session=False)
    db.commit()
    return{'Data removed Successfully'}
