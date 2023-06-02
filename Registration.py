
class Registration:
    def __init__(self, plate, entryTime):
        self.plate = plate
        self.entryTime = entryTime
        self.exitTime = None
        self.active = True

    def setExitTime(self, exitTime):
        self.exitTime = exitTime
        self.active = False

    def toDict(self):
        exitTime = "Veiculo ainda na vaga" if self.active else self.exitTime
        return {
            'plate': self.plate,
            'entryTime': self.entryTime,
            'exitTime': exitTime
        }

    def __str__(self):
        exitTime = "Veiculo ainda na vaga" if self.active else self.exitTime
        return f"Placa: {self.plate}, Horário de entrada: {self.entryTime}, Saída: {exitTime}"
