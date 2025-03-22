class HealthData:
    def __init__(self, name, age, bmi, bp):
        self.name = name
        self.age = float(age)
        self.bmi = float(bmi)
        self.bp = float(bp)

    def health_status(self):
        if self.bmi < 25 and self.bp < 120:
            return "Healthy"
        elif (25 <= self.bmi < 30) or (120 <= self.bp < 140):
            return "At risk"
        else:
            return "Unhealthy"

# Creating patient objects
patient1 = HealthData("Aden", 28, 24, 118)
patient2 = HealthData("Mohamed", 30, 29, 129)
patient3 = HealthData("Yussuf", 33, 35, 145)

# Printing results
print(f"{patient1.name}: {patient1.health_status()}")
print(f"{patient2.name}: {patient2.health_status()}")
print(f"{patient3.name}: {patient3.health_status()}")
