class ServoDrive:
    def __init__(self, model, power):
        self.model = model
        self.power = power

    def __str__(self):
        return f'ServoDrive(model={self.model}, power={self.power})'

    def __repr__(self):
        return f'ServoDrive(model={self.model!r}, power={self.power!r})'
    

class SynchronousServoDrive(ServoDrive):
    def __init__(self, model, power, synchronization_time):
        super().__init__(model, power)
        self.synchronization_time = synchronization_time

    def __str__(self):
        return f'SynchronousServoDrive(model={self.model}, power={self.power}, synchronization_time={self.synchronization_time})'

    def __repr__(self):
        return f'SynchronousServoDrive(model={self.model!r}, power={self.power!r}, synchronization_time={self.synchronization_time!r})'
    
class AsynchronousServoDrive(ServoDrive):
    def __init__(self, model, power, async_jobs):
        super().__init__(model, power)
        self.async_jobs = async_jobs

    def __str__(self):
        return f'AsynchronousServoDrive(model={self.model}, power={self.power}, async_jobs={self.async_jobs})'

    def __repr__(self):
        return f'SynchronousServoDrive(model={self.model!r}, power={self.power!r}, async_jobs={self.async_jobs!r})'


servo = ServoDrive('Servo 1000', 1000)
syncServo = SynchronousServoDrive('Sync Servo 1000', 1000, 10)
asyncServo = AsynchronousServoDrive('Aync Servo 1000', 1000, 150)

print(asyncServo)