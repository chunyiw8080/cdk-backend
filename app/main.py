from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db import SessionLocal
from app.schemas import CDKRequest
from app.crud import verify_and_use_cdk

app = FastAPI()

# 依赖注入数据库 Session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.post("/cdk/verify")
def verify_cdk(
    req: CDKRequest,
    db: Session = Depends(get_db)
):
    print(req)
    success = verify_and_use_cdk(db, req.user_id, req.cdk)

    if not success:
        raise HTTPException(
            status_code=400,
            detail="CDK 无效或已被使用"
        )

    return {
        "success": True,
        "message": "CDK 激活成功"
    }

