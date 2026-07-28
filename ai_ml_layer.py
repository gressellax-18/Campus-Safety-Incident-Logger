# ai_ml_layer.py

def classify_incident(description):
    """
    AI-based Incident Classification
    """

    text = description.lower()

    # ---------------- Security ----------------
    security = [
        "fight", "harassment", "ragging", "bully", "bullying",
        "threat", "violence", "assault", "attack"
    ]

    # ---------------- Theft ----------------
    theft = [
        "theft", "stolen", "steal", "missing",
        "bike", "bicycle", "laptop", "mobile",
        "wallet", "phone", "robbery"
    ]

    # ---------------- Medical ----------------
    medical = [
        "medical", "injury", "injured", "blood",
        "fainted", "unconscious", "ambulance",
        "hospital", "health"
    ]

    # ---------------- Fire ----------------
    fire = [
        "fire", "smoke", "burn", "short circuit",
        "explosion", "accident"
    ]

    # ---------------- Infrastructure ----------------
    infrastructure = [
        "light", "electricity", "road",
        "water leakage", "broken", "chair",
        "bench", "fan", "building", "ceiling"
    ]

    # ---------------- Hygiene ----------------
    hygiene = [
        "garbage", "dust", "dirty", "clean",
        "washroom", "toilet", "drainage",
        "mosquito", "smell"
    ]

    # ---------------- Suspicious ----------------
    suspicious = [
        "suspicious", "unknown", "stranger",
        "unauthorized", "intruder"
    ]

    if any(word in text for word in security):
        return "Security Issue"

    elif any(word in text for word in theft):
        return "Theft"

    elif any(word in text for word in medical):
        return "Medical Emergency"

    elif any(word in text for word in fire):
        return "Fire Emergency"

    elif any(word in text for word in infrastructure):
        return "Infrastructure Issue"

    elif any(word in text for word in hygiene):
        return "Health & Hygiene Issue"

    elif any(word in text for word in suspicious):
        return "Suspicious Activity"

    else:
        return "General Safety Issue"


def preventive_suggestion(category):
    """
    AI-generated Preventive Suggestions
    """

    suggestions = {

        "Security Issue":
        "Increase campus security, install CCTV cameras, conduct awareness programs, and report immediately to the security office.",

        "Theft":
        "Improve surveillance, secure personal belongings, increase patrols, and verify CCTV footage promptly.",

        "Medical Emergency":
        "Contact the campus medical team immediately, provide first aid if trained, and call emergency services when required.",

        "Fire Emergency":
        "Evacuate the area safely, activate the fire alarm, inform the fire department, and use fire extinguishers if safe to do so.",

        "Infrastructure Issue":
        "Repair damaged facilities quickly, perform routine inspections, and place warning signs until the issue is fixed.",

        "Health & Hygiene Issue":
        "Maintain cleanliness, improve waste management, sanitize affected areas, and inspect hygiene facilities regularly.",

        "Suspicious Activity":
        "Inform campus security immediately, monitor the area, avoid direct confrontation, and verify identities where appropriate.",

        "General Safety Issue":
        "Investigate the incident, document the details, and take appropriate preventive measures to improve campus safety."
    }

    return suggestions.get(
        category,
        "Take appropriate preventive action."
    )