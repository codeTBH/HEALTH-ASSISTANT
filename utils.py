import numpy as np
def calculate_risk_percent(probability):
    percentage = 1/(1 + np.exp(-probability[0])) * 100
    return round(percentage, 2)

def determine_risk_level(percentage):
    if percentage <40:
        return "Low"
    elif percentage < 70:
        return "Medium"
    else:
        return "High"