from typing import List
from fastapi import APIRouter,Depends,status,HTTPException, Response

from oauth2 import get_current_user
import schemas, database, models
from sqlalchemy.orm import Session
from repository import blog

router = APIRouter(
    prefix="/blog",
    tags=['Blogs']
)


get_db = database.get_db

# Create Blog
@router.post('/', status_code=status.HTTP_201_CREATED,)
def create(request: schemas.Blog, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    return blog.create(request, db)


# get all blogs
@router.get('/',response_model=List[schemas.ShowAllBlog])
def all(db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    return blog.get_all(db)

# get perticular blogs
@router.get('/{id}', status_code=200)
def show(id:int, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    return blog.show(id,db)


#Delete particular blog  
@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id:int, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    return blog.destroy(id,db)
      

# Update particular blog 
@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id:int, request: schemas.Blog, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    return blog.update(id,request, db)

