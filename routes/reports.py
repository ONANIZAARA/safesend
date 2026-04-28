from fastapi import APIRouter
from models import ScamReport
from database import SessionLocal

router = APIRouter()

@router.get("/all-scam-reports")
def all_scam_reports():
    db = SessionLocal()
    reports = db.query(ScamReport).all()
    db.close()
    return [
        {
            "phone":       r.phone,
            "message":     r.message,
            "risk_score":  r.risk_score,
            "reported_at": str(r.reported_at)
        }
        for r in reports
    ]

@router.get("/scam-stats")
def scam_stats():
    db = SessionLocal()
    total        = db.query(ScamReport).count()
    high_risk    = db.query(ScamReport).filter(ScamReport.risk_score >= "0.5").count()
    suspicious   = db.query(ScamReport).filter(ScamReport.risk_score > "0.0").count()
    safe         = db.query(ScamReport).filter(ScamReport.risk_score == "0.0").count()
    db.close()
    return {
        "total_checks":    total,
        "high_risk":       high_risk,
        "suspicious":      suspicious,
        "safe":            safe
    }