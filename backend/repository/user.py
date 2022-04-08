from sqlalchemy.orm import Session
import models, schemas
from fastapi import HTTPException,status
from hashing import Hash

# Create new user
def create(request: schemas.User,db:Session):
    new_user = models.User(name=request.name,email=request.email,password=Hash.dcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

# Show particular user
def show(id:int,db:Session):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with the id {id} is not available")
    return user

# Show all users   

def showAll(db:Session):
    user = db.query(models.User).all()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with the id {id} is not available")
    return user

def deleteUser(id:int,db:Session):
    user = db.query(models.User).filter(models.User.id == id)
    if not user.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with the id {id} is not available")

    user.delete(synchronize_session=False)
    db.commit()
    return "Delete successfully"   