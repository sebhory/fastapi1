from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from others import  models, schemas
from db import SessionLocal, engine, Base, get_db


# Base.metadata.drop_all(bind=engine)
# Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.post("/user/", response_model=schemas.User, tags=['user'])
async def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = models.User(name = user.name, email = user.email, hashed_password = user.hashed_password)
    db.add(db_user)
    db.commit()

    return db_user


# @app.get("/users/", response_model=schemas.User)
# async def get_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     return db.query(models.User).offset(skip).limit(limit).all()

@app.get("/user/", tags=['user'])
async def get_users(db: Session = Depends(get_db)):
    return db.query(models.User).all()




@app.post("/item/", response_model=schemas.Item, tags=['item'])
async def create_item(item: schemas.ItemCreate, db: Session = Depends(get_db)):
    db_item = models.Item(title= item.title, description = item.description)
    db.add(db_item)
    db.commit()

    return db_item


@app.get("/item/", tags=['item'])
async def get_items(db: Session = Depends(get_db)):
    return db.query(models.Item).all()



@app.post("/assoc/", tags=['Assoc'])
async def assoc_user_item(user_id: int, item_id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    item = db.query(models.Item).filter(models.Item.id == item_id).first()
    user.items.append(item)
    db.commit()
    return user


@app.get("/userinfo/", tags=['userinfo'])
async def get_user_item(id: int, db: Session = Depends(get_db)):
    user =  db.query(models.User).filter(models.User.id == id).first()
    return user.items