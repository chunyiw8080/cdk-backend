from sqlalchemy.orm import Session
from datetime import datetime
from app.models import CDKey

def verify_and_use_cdk(db: Session, user_id: int, cdk: str) -> bool:
    record = db.query(CDKey).filter(CDKey.cdk == cdk).first()

    # 1. 不存在
    if not record:
        return False

    # 2. 已被使用
    if record.used:
        return False

    # 3. 更新状态
    record.used = True
    record.used_by = user_id
    record.used_at = datetime.utcnow()

    db.commit()
    return True
