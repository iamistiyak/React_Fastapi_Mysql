from fastapi import APIRouter, HTTPException
import database, schemas, models
from sqlalchemy.orm import Session
from fastapi import APIRouter,Depends,status
from repository import user
from typing import List
router = APIRouter(
    prefix="/user",
    tags=['Users']
)

get_db = database.get_db

# Create User 
@router.post('/', response_model=schemas.ShowUsers)
def create_user(request: schemas.User,db: Session = Depends(get_db)):
    return user.create(request,db)  

# Get particular user
@router.get('/{id}',response_model=schemas.ShowUsers)
def get_user(id:int,db: Session = Depends(get_db)):
    return user.show(id,db)

# Get all users
@router.get('/',response_model=List[schemas.ShowUsers])
def get_user(db: Session = Depends(get_db)):
    return user.showAll(db)

# Delete particular user
@router.delete('/{id}')
def delete_user(id:int,db: Session = Depends(get_db)):
    return user.deleteUser(id,db)