from functools import total_ordering


class ServoDrive:
    def __init__(self, model, power):
        self.model = model
        self.power = power

    def __str__(self):
        return f'ServoDrive(model={self.model}, power={self.power})'

    def __repr__(self):
        return f'ServoDrive(model={self.model!r}, power={self.power!r})'
    

class SpinnableServoDrive(ServoDrive):
    def __init__(self, model, power, max_speed, direction):
        super().__init__(model, power)
        self.max_speed = max_speed
        self.direction = direction

    def __str__(self):
        return f'SpinnableServoDrive(model={self.model}, power={self.power}, max_speed={self.max_speed}, direction={self.direction})'

    def __repr__(self):
        return f'SpinnableServoDrive(model={self.model!r}, power={self.power!r}, max_speed={self.max_speed!r}, direction={self.direction!r})'

@total_ordering # определили 1 оператор сравнения < и автоматически аннотация генерирует остальные сравн. операторы
class SynchronousServoDrive(SpinnableServoDrive):
    def __init__(self, model, power, max_speed, direction, synchronization_time):
        super().__init__(model, power, max_speed, direction)
        self.synchronization_time = synchronization_time

    def __str__(self):
        return f'SynchronousServoDrive(model={self.model},\
            power={self.power},\
            synchronization_time={self.synchronization_time}),\
            max_speed={self.max_speed},\
            direction={self.direction}'

    def __repr__(self):
        return f'SynchronousServoDrive(model={self.model!r},\
            power={self.power!r},\
            synchronization_time={self.synchronization_time!r}),\
            max_speed={self.max_speed!r},\
            direction={self.direction!r}'
    
    def __eq__(self, other):
        if not isinstance(other, SynchronousServoDrive):
            return False
        return self.power == other.power

    def __lt__(self, other):
        if not isinstance(other, SynchronousServoDrive):
            return NotImplemented
        return self.power < other.power
    
class AsynchronousServoDrive(SpinnableServoDrive):
    def __init__(self, model, power, max_speed, direction, async_jobs):
        super().__init__(model, power, max_speed, direction)
        self.async_jobs = async_jobs

    def __str__(self):
        return f'SynchronousServoDrive(model={self.model},\
            power={self.power},\
            async_jobs={self.async_jobs}),\
            max_speed={self.max_speed},\
            direction={self.direction}'

    def __repr__(self):
        return f'SynchronousServoDrive(model={self.model!r},\
            power={self.power!r},\
            async_jobs={self.async_jobs!r}),\
            max_speed={self.max_speed!r},\
            direction={self.direction!r}'


servo = ServoDrive('Servo 1000', 1000)
syncServo1000 = SynchronousServoDrive('Sync Servo 1000', 1000, 1500, 1, 10)
syncServo2000 = SynchronousServoDrive('Sync Servo 2000', 2000, 1500, 1, 10)
asyncServo = AsynchronousServoDrive('Async Servo 1000', 1000, 1500, -1, 15)

print(asyncServo)
print('syncServo1000 < syncServo2000: ', syncServo1000 < syncServo2000)
print('syncServo1000 > syncServo2000: ', syncServo1000 > syncServo2000)
print('syncServo1000 <= syncServo2000: ', syncServo1000 <= syncServo2000)
print('syncServo1000 >= syncServo2000: ', syncServo1000 >= syncServo2000)
print('syncServo1000 = syncServo2000: ', syncServo1000 == syncServo2000)