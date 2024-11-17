class ServoDrive:
    def __init__(self, model, power):
        self.model = model
        self.power = power

    def __str__(self):
        return f'ServoDrive(model={self.model}, power={self.power})'

    def __repr__(self):
        return f'ServoDrive(model={self.model!r}, power={self.power!r})'
    

