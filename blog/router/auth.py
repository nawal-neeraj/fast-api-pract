from fastapi import APIRouter, Depends, HTTPException, status
from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from ..hashing import Hash
from .. import token


from .. import schema, database, model

get_db = database.get_db

router = APIRouter(
    tags=['User Authentication']
)


@router.post('/login')
def loginfun(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(model.User).filter(
        model.User.email == request.username).first()
    # print(user)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f'Username not found')
    if not Hash.varify(request.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail=f'incorrect password')

    access_token = token.create_access_token(
        data={"sub": user.email}
    )
    return {"access_token": access_token, "token_type": "bearer"}
