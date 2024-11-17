from abc import ABC, abstractmethod


# абстрактыный класс звена манипулятора
class Joint(ABC):
    def __init__(self, length=0):
        self.length = length  

    @abstractmethod
    def get_position_change(self, base_angle):
        pass

    def __repr__(self):
        return f"{self.__class__.__name__}(length={self.length})"