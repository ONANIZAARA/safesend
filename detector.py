from keywords import ALL_KEYWORDS
from models import ReportedNumber
from database import SessionLocal

def analyze_message(message: str):
    message = message.lower()
    found_keywords = []

    for keyword in ALL_KEYWORDS:
        if keyword in message:
            found_keywords.append(keyword)

    risk_score = min(len(found_keywords) / 5, 1.0)
    return found_keywords, round(risk_score, 2)

def is_number_reported(phone: str):
    db = SessionLocal()
    result = db.query(ReportedNumber).filter(
        ReportedNumber.phone == phone
    ).first()
    db.close()
    return result is not None

def calculate_risk_level(risk_score: float):
    if risk_score >= 0.5:
        return "HIGH RISK", "Do NOT respond or send money. This is likely a scam."
    elif risk_score > 0:
        return "SUSPICIOUS", "Be careful. Verify before taking any action."
    else:
        return "SAFE", "No scam indicators found."