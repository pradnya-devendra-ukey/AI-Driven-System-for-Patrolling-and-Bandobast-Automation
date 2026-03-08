def crowd_density(detections):

    people = detections.count("person")

    if people < 20:
        level = "LOW"

    elif people < 50:
        level = "MEDIUM"

    else:
        level = "HIGH"

    return {
        "people_count": people,
        "density": level
    }