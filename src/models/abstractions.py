from abc import ABC, abstractmethod


class SQNModel(ABC):
    
    @abstractmethod
    def to_sql(self) -> str:
        pass

class Condition(SQNModel):

    @abstractmethod
    def to_sql(self) -> str:
        pass

class Value(SQNModel):

    @abstractmethod
    def to_sql(self) -> str:
        pass
