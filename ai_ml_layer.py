# ai_ml_layer.py

def classify_incident(description):
    """
    Classifies the incident based on description
    """

    text = description.lower()

    if "fight" in text or "harassment" in text or "threat" in text:
        return "Security Issue"

    elif "light" in text or "electricity" in text or "road" in text:
        return "Infrastructure Issue"

    elif "water" in text or "clean" in text or "garbage" in text:
        return "Health & Hygiene Issue"

    elif "fire" in text or "accident" in text:
        return "Emergency Issue"

    else:
        return "General Safety Issue"



def preventive_suggestion(category):
    """
    Provides preventive measures based on incident category
    """

    if category == "Security Issue":
        return "Increase security monitoring and conduct safety awareness programs."

    elif category == "Infrastructure Issue":
        return "Repair damaged facilities and perform regular maintenance checks."

    elif category == "Health & Hygiene Issue":
        return "Improve cleanliness, sanitation and waste management."

    elif category == "Emergency Issue":
        return "Take immediate action and inform emergency response teams."

    else:
        return "Analyze the issue and take suitable preventive action."