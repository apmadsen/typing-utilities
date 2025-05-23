# pyright: basic
from __future__ import annotations
from typing import Any, TypeVar, Iterable, cast
from dataclasses import dataclass

from typingutils.core.types import get_generic_parameters, construct_generic_type
from typingutils.core.instances import get_generic_origin
from typingutils.core.attributes import GENERIC_CONSTRUCTOR, NAME, GENERIC_CONSTRUCTOR

@dataclass
class IsSubclassTestcase:
    base: type[Any]
    comparison: type[Any]
    expected_equality: bool

    base_is_subscripted_generic: bool
    base_is_generic_type: bool

    comparison_is_subscripted_generic: bool
    comparison_is_generic_type: bool

def create_testcases_for_issubclass() -> Iterable[IsSubclassTestcase]:

    from tests.generic_types import generic_types, non_generic_types
    from tests.generic_classes import BaseClass, DerivedClass, DerivedClass1

    yield IsSubclassTestcase(BaseClass, DerivedClass, True, False, False, False, False)
    yield IsSubclassTestcase(BaseClass, DerivedClass1, True, False, False, False, False)
    yield IsSubclassTestcase(DerivedClass, DerivedClass1, True, False, False, False, False)
    yield IsSubclassTestcase(DerivedClass, BaseClass, False, False, False, False, False)
    yield IsSubclassTestcase(DerivedClass1, DerivedClass, False, False, False, False, False)
    yield IsSubclassTestcase(DerivedClass1, BaseClass, False, False, False, False, False)

    typevars: tuple[type[Any], ...] = ( str, int, float, bool )

    for cls in generic_types:
        for type1 in typevars:
            origin = get_generic_origin(cls)

            if origin is type:
                # Type's origin is type which is not generic per se because it lacks the __class_getitem__ function
                continue

            generic_parameters = tuple(
                TypeVar(cast(str, getattr(typevar, NAME)), bound = type_) # pyright: ignore[reportGeneralTypeIssues, reportInvalidTypeForm]
                for typevar, type_ in zip(get_generic_parameters(cls), typevars)
            )
            generic_type = getattr(origin, GENERIC_CONSTRUCTOR)(generic_parameters)
            generic_cls = construct_generic_type(origin, type1)

            for type2 in typevars:
                if type2 != type1:
                    generic_cls1 = construct_generic_type(origin, type2)
                    yield IsSubclassTestcase(generic_cls, generic_cls1, False, True, False, True, False)

            yield IsSubclassTestcase(origin, generic_cls, True, False, False, True, False)
            yield IsSubclassTestcase(cls, generic_cls, False, False, True, True, False)
            yield IsSubclassTestcase(generic_type, generic_cls, False, False, True, True, False)
            yield IsSubclassTestcase(generic_cls, generic_type, False, True, True, False, True)
            yield IsSubclassTestcase(generic_cls, cls, False, True, False, False, True)
            yield IsSubclassTestcase(generic_type, cls, False, False, True, False, True)


