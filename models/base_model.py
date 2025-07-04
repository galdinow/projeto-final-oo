from abc import ABC, abstractmethod
class BaseModel(ABC):
    @abstractmethod
    def to_dict():
        pass