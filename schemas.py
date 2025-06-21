from pydantic import BaseModel, EmailStr

class InquiryCreate(BaseModel):
    name: str
    email: EmailStr
    phone: str
    message: str

class InquiryOut(InquiryCreate):
    id: int

    model_config = {
        "from_attributes": True
    }
