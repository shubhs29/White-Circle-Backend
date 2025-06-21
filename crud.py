from sqlalchemy.orm import Session
from models import Inquiry
from schemas import InquiryCreate

def create_inquiry(db: Session, inquiry: InquiryCreate):
    db_inquiry = Inquiry(**inquiry.dict())
    db.add(db_inquiry)
    db.commit()
    db.refresh(db_inquiry)
    return db_inquiry
