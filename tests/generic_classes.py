# pyright: basic
from __future__ import annotations
from typing import TypeVar, Generic, Mapping, Iterator

T = TypeVar('T')
Tstr = TypeVar('Tstr', bound=str)
T1 = TypeVar('T1')
T2 = TypeVar('T2')
Tkey = TypeVar('Tkey')
Tvalue = TypeVar('Tvalue')

class NormalClass():
    pass

class GenericClass1(Generic[T]):
    pass
class GenericSubClass1(GenericClass1[T]):
    pass

class GenericClass4(Mapping[Tkey, Tvalue]):
    def __getitem__(self, k: Tkey) -> Tvalue:
        raise NotImplementedError()
    def __iter__(self) -> Iterator[Tvalue]: # pyright: ignore[reportIncompatibleMethodOverride]
        raise NotImplementedError()
    def __len__(self) -> int:
        raise NotImplementedError()

class SelfReferencingClass1:
    def method(self, txt: str) -> SelfReferencingClass1:
        return self

class ParentClass():
    class ChildClass(): pass

class BaseClass(): ...

class DerivedClass(BaseClass): ...

class DerivedClass1(DerivedClass): ...

class DerivedClass2(ParentClass, BaseClass): ...