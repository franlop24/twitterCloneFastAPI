# Imports from Python
from datetime import date, datetime
from typing import Optional
from uuid import UUID

# Imports from Pydantic
from pydantic import BaseModel, EmailStr, Field

# Imports from FastAPI
from fastapi import FastAPI, status

app = FastAPI()

# Models
class UserBase(BaseModel):
    user_id: UUID = Field(...)
    email: EmailStr = Field(...)

class UserLogin(UserBase):
    password: str = Field(..., min_length=8, max_length=64)

class User(UserBase):
    first_name: str = Field(
                        ...,
                        min_length=1,
                        max_length=50                
                    )
    last_name: str = Field(
                        ...,
                        min_length=1,
                        max_length=50                
                    )
    birth_date: Optional[date] = Field(default=None)

class UserRegister(User, UserLogin):
    pass


class Tweet(BaseModel):
    tweet_id: UUID = Field(...)
    content: str = Field(
                        ..., 
                        min_length=1, 
                        max_length=256
                    )
    created_at: datetime = Field(default=datetime.now())
    updated_at: Optional[datetime] = Field(default=None)
    by: User = Field(...)

# Path Operations
## Users

### Register a User
@app.post(
            path="/signup",
            response_model=User,
            status_code=status.HTTP_201_CREATED,
            summary="Register a User",
            tags=["Users"]
        )
def signup():
    """
    Signup

    This Path Operation registar a user in the app

    Parameters:
    -   Request Body Parameter
        - user: UserRegister
    
    Returns a json with the basic user information
        - user_id: UUID
        - email: EmailStr
        - first_name: str
        - last_name: str
        - bith_date: str
    """    

### Login a User
@app.post(
            path="/login",
            response_model=User,
            status_code=status.HTTP_200_OK,
            summary="Login a User",
            tags=["Users"]
        )
def login():
    pass

### Show all Users
@app.get(
            path="/users",
            response_model=list[User],
            status_code=status.HTTP_200_OK,
            summary="Show all Users",
            tags=["Users"]
        )
def show_all_users():
    pass

### Show a User By ID
@app.get(
            path="/users/{user_id}",
            response_model=User,
            status_code=status.HTTP_200_OK,
            summary="Show a User",
            tags=["Users"]
        )
def show_a_user():
    pass

### Delete a User
@app.delete(
            path="/users/{user_id}/delete",
            status_code=status.HTTP_204_NO_CONTENT,
            summary="Delete a User",
            tags=["Users"]
        )
def delete_a_user():
    pass

### Update a User
@app.put(
            path="/users/{user_id}/update",
            response_model=User,
            status_code=status.HTTP_200_OK,
            summary="Update a User",
            tags=["Users"]
        )
def update_a_user():
    pass

## Tweets

### Show all Tweets
@app.get(
            path="/",
            response_model=list[Tweet],
            status_code=status.HTTP_200_OK,
            summary="Show all Tweets",
            tags=["Tweets"]
        )
def home():
    return {"Twitter API": "Working!"}

### Post Tweet
@app.post(
            path="/post",
            response_model=Tweet,
            status_code=status.HTTP_201_CREATED,
            summary="Post a Tweet",
            tags=["Tweets"]
        )
def post_tweet():
    pass

### Show a Tweet
@app.get(
            path="/tweet/{tweet_id}",
            response_model=Tweet,
            status_code=status.HTTP_200_OK,
            summary="Show a Tweet",
            tags=["Tweets"]
        )
def show_tweet():
    pass

### Delete a Tweet
@app.delete(
                path="/tweet/{tweet_id}/delete",
                status_code=status.HTTP_204_NO_CONTENT,
                summary="Delete a Tweet",
                tags=["Tweets"]
            )
def delete_tweet():
    pass

### Update a Tweet
@app.put(
            path="/tweet/{tweet_id}/update",
            response_model=Tweet,
            status_code=status.HTTP_200_OK,
            summary="Update a Tweet",
            tags=["Tweets"]
        )
def update_tweet():
    pass