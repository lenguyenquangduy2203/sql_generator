from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional


class Value(ABC):
    def __init__(self, value: Any = None):
        self.value = value

    @abstractmethod
    def to_sql(self) -> str:
        pass


class Condition(ABC):
    @abstractmethod
    def to_sql(self) -> str:
        pass


class SQNModel(ABC):
    def __init__(
        self,
        selections: Optional[Dict[str, List[str]]] = None,
        conditions: Optional[Condition] = None,
    ):
        self.selections = selections or {}
        self.conditions = conditions

    @abstractmethod
    def to_sql(self) -> str:
        pass
