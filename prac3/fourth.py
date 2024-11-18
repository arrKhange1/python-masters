from abc import ABC, abstractmethod
import math


# абстрактный класс звена манипулятора
class Joint(ABC):
    def __init__(self, length=0):
        self.length = length  

    @abstractmethod
    def get_position_change(self, base_angle):
        pass

    def __repr__(self):
        return f"{self.__class__.__name__}(length={self.length!r})"
    

# вращательное звено
class RevoluteJoint(Joint):
    def __init__(self, length, angle=0):
        super().__init__(length)
        self.angle = angle  

    def rotate(self, delta_angle):
        self.angle += delta_angle

    def get_position_change(self, base_angle):
        total_angle = math.radians(base_angle + self.angle)
        dx = self.length * math.cos(total_angle)
        dy = self.length * math.sin(total_angle)
        return dx, dy

    def __repr__(self):
        return f"{self.__class__.__name__}(length={self.length!r}, angle={self.angle!r})"
    
# поступательное звено
class PrismaticJoint(Joint):
    def __init__(self, length, extension=0):
        super().__init__(length)
        self.extension = extension

    def extend(self, delta_extension):
        self.extension += delta_extension

    def get_position_change(self, base_angle):
        total_length = self.length + self.extension
        total_angle = math.radians(base_angle)
        dx = total_length * math.cos(total_angle)
        dy = total_length * math.sin(total_angle)
        return dx, dy

    def __repr__(self):
        return f"{self.__class__.__name__}(length={self.length!r}, extension={self.extension!r})"
    


class Manipulator:
    def __init__(self, joints):
        self.joints = joints

    # расчет конечного положения на оси x,y из-за поступ. и вращат. движений и конечного угла манипулятора
    def get_end_position(self):
        x, y = 0, 0
        current_angle = 0

        for joint in self.joints:
            dx, dy = joint.get_position_change(current_angle)
            x += dx
            y += dy

            if isinstance(joint, RevoluteJoint):
                current_angle += joint.angle

        return round(x, 2), round(y, 2)

    def __add__(self, deltas):
        for joint, delta in zip(self.joints, deltas):
            if isinstance(joint, RevoluteJoint):
                joint.rotate(delta)
            elif isinstance(joint, PrismaticJoint):
                joint.extend(delta)
        return self

    def __repr__(self):
        return f"{self.__class__.__name__}({self.joints})"


joints = [
        RevoluteJoint(length=10, angle=0),
        PrismaticJoint(length=5, extension=0),
        RevoluteJoint(length=8, angle=0),
        PrismaticJoint(length=3, extension=0),
    ]
manipulator = Manipulator(joints)

print("Начальное положение манипулятора:")
print(manipulator)
print("Конечная точка:", manipulator.get_end_position())

# Изменяем параметры звеньев
manipulator + [30, 2, -15, 1]

print("\nПосле изменений:")
print(manipulator)
print("Конечная точка:", manipulator.get_end_position())
