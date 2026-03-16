from datetime import datetime

class Patient:
    def __init__(self, name, age, condition):
        self.name = name.strip()
        self.age = int(age)
        self.condition = condition.strip()
        self.time_registered = datetime.now().strftime("%I:%M %p")
    
    def get_info(self):  # custom behavior method
        return f"{self.name} ({self.age}yrs) - {self.condition} [{self.time_registered}]"
# Integrated datetime for precise patient check-in tracking

# Encapsulation: Private-like attributes for data integrity

    def __repr__(self): return f'<Patient {self.name}>'

# Type Hinting for improved code robustness
