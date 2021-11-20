from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any


class BaseSpecification:
    @abstractmethod
    def is_satisfied(self, obj: Any) -> bool:
        raise NotImplementedError()

    def and_(self, other: "BaseSpecification") -> "AndSpecification":
        return AndSpecification(self, other)

    def or_(self, other: "BaseSpecification") -> "OrSpecification":
        return OrSpecification(self, other)


@dataclass(frozen=True)
class AndSpecification(BaseSpecification):
    first: BaseSpecification
    second: BaseSpecification

    def is_satisfied(self, obj: Any) -> bool:
        return self.first.is_satisfied(obj) and self.second.is_satisfied(obj)


@dataclass(frozen=True)
class OrSpecification(BaseSpecification):
    first: BaseSpecification
    second: BaseSpecification

    def is_satisfied(self, obj: Any) -> bool:
        return self.first.is_satisfied(obj) or self.second.is_satisfied(obj)
