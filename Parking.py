
class Parking:
    def __init__(self):
        self.vacancies = {}
        for i in range(1, 41):
            self.vacancies[f"Box {str(i)}"] = []
