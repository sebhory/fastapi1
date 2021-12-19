from typing import List, Optional

from pydantic import BaseModel




class ItemBase(BaseModel):

    title: str

    description: Optional[str] = None




class ItemCreate(ItemBase):

    pass



class Item(ItemBase):
    id: int
    # owner_id: int

    class Config:
        orm_mode = True



class UserBase(BaseModel):
    name : str
    email: str




class UserCreate(UserBase):

    hashed_password : str



class User(UserBase):
    id: int
    is_active: bool
    items: List[Item] = []

    class Config:
        orm_mode = True



class AssocUserItem(BaseModel):
    user_id : int
    item_id : int

    class Config:
        orm_mode = True