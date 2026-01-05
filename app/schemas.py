from pydantic import BaseModel

class CDKRequest(BaseModel):
    user_id: int
    cdk: str
