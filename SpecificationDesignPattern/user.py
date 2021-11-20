from typing import Any

from SpecificationDesignPattern.specifications.base_specification import BaseSpecification


class User:
    def __init__(self, super_user=False):
        self.super_user = super_user


class UserSpecification(BaseSpecification):
    def is_satisfied(self, obj: Any) -> bool:
        return isinstance(obj, User)


class SuperUserSpecification(BaseSpecification):
    def is_satisfied(self, obj: Any) -> bool:
        return getattr(obj, 'super_user', False)