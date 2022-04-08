from pydantic import BaseModel
from typing import Optional, List


class BlogBase(BaseModel):
    title: str
    body: str

class Blog(BlogBase):
    class Config():
          orm_mode = True 


# For response model
class ShowAllBlog(BaseModel):
      title: str
      body: str
      
      class Config():
          orm_mode = True 


class User(BaseModel):
    name: str
    password: str
    email: str
    class Config():
          orm_mode = True 
# For response model
class ShowUsers(BaseModel):
      name: str
      email: str
      password: str
    #   blogs:List[Blog]

      class Config():
          orm_mode = True 
          
class AuthenticUser(BaseModel):
    name: str
    email: str
    class Config():
          orm_mode = True 

# For response model
class ShowBlog(BaseModel):
      title: str
      body: str
      id: int
      creator: ShowUsers
      class Config():
          orm_mode = True           

# For login credentials
class Login(BaseModel):
    useremail: str
    password:str

# For JWT token
class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None
          