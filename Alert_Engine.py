def generate_alert(density, detections):

    alerts = []

    if density["density"] == "HIGH":
        alerts.append("High crowd density detected")

    if "knife" in detections or "gun" in detections:
        alerts.append("Possible weapon detected")

    if "backpack" in detections and density["density"] == "HIGH":
        alerts.append("Suspicious unattended bag")

    return alerts