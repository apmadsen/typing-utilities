# pyright: basic
from typing import Any, Iterable, TypeVar, cast
from dataclasses import dataclass
from types import UnionType

from typingutils.core.types import _is_special_generic_type, get_generic_parameters
from typingutils.core.attributes import NAME, GENERIC_CONSTRUCTOR


@dataclass
class TypesTestcase:
    cls: type[Any]
    is_generic: bool
    is_generic_type: bool

def create_testcases_for_types() -> Iterable[TypesTestcase]:
    created: set[type[Any] | UnionType] = set()

    from tests.testcase_generators.issubclass import create_testcases_for_issubclass
    from tests.generic_types import generic_types, non_generic_types, unions
    from tests.generic_classes import (
        NormalClass, GenericClass1, GenericSubClass1, GenericClass4,
        SelfReferencingClass1, ParentClass, BaseClass, DerivedClass, DerivedClass1
    )

    issubclass_testcases = list(create_testcases_for_issubclass())

    for cls in unions:
        if cls not in created:
            created.add(cls)
            yield TypesTestcase(cast(type, cls), True, not _is_special_generic_type(cls))

    for cls in generic_types:
        if cls not in created:
            created.add(cls)
            yield TypesTestcase(cls, False, True)

    for cls in non_generic_types:
        if cls not in created:
            created.add(cls)
            yield TypesTestcase(cls, False, False)

    for testcase in issubclass_testcases:
        if testcase.base not in created:
            created.add(testcase.base)
            yield TypesTestcase(testcase.base, testcase.base_is_subscripted_generic, testcase.base_is_generic_type)

        if testcase.comparison not in created:
            created.add(testcase.comparison)
            yield TypesTestcase(testcase.comparison, testcase.comparison_is_subscripted_generic, testcase.comparison_is_generic_type)

    for cls in (NormalClass, SelfReferencingClass1, ParentClass, BaseClass, DerivedClass, DerivedClass1 ):
        if cls not in created:
            created.add(cls)
            yield TypesTestcase(cls, False, False)

    for cls in (GenericClass1, GenericSubClass1, GenericClass4 ):
        if cls not in created:
            created.add(cls)
            yield TypesTestcase(cls, False, True)

            typevars: tuple[type[Any], ...] = ( str, int, float, bool )
            generic_parameters = tuple(
                TypeVar(cast(str, getattr(typevar, NAME)), bound = type_) # pyright: ignore[reportGeneralTypeIssues, reportInvalidTypeForm]
                for typevar, type_ in zip(get_generic_parameters(cls), typevars)
            )
            generic_type = getattr(cls, GENERIC_CONSTRUCTOR)(generic_parameters)

            yield TypesTestcase(generic_type, False, True)

