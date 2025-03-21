from abc import ABC, abstractmethod

class Query(ABC):
    @abstractmethod
    def to_str(self) -> str:
        pass
