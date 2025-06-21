from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
from database import SessionLocal, engine, Base
import models, schemas, crud

Base.metadata.create_all(bind=engine)

app = FastAPI()

# Allow frontend access (React)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# DB Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/inquiry", response_model=schemas.InquiryOut)
def submit_inquiry(inquiry: schemas.InquiryCreate, db: Session = Depends(get_db)):
    try:
        return crud.create_inquiry(db=db, inquiry=inquiry)
    except Exception as e:
        print("🚨 INTERNAL SERVER ERROR:", e)
        raise HTTPException(status_code=500, detail=str(e))
