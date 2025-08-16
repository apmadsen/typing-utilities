# pyright: basic
# ruff: noqa
import sys

if sys.version_info >= (3, 12):
    from typing import Any, TypeVar, cast
    from pytest import raises as assert_raises, fixture
    from typingutils import get_generic_parameters, get_generic_arguments, get_type_name, is_generic_type, is_subscripted_generic_type, is_generic_function, issubclass_typing, AnyFunction, TypeArgs
    from typingutils.internal import get_original_class, get_types_from_typevar, get_executing_function

    class TestPython312:

        def test_typevar_tuples(self):

            class Class1[*Ts]:
                pass

            typevar, *remaining = get_generic_parameters(Class1)

            assert typevar and not remaining
            assert get_types_from_typevar(typevar) == tuple[type[Any], ...]
            assert get_type_name(typevar) == "*Ts"

            inst = Class1[int, str, bool]

            assert get_generic_arguments(inst) == (int, str, bool)

        def test_is_subclass_with_typevar_tuples(self):

            class Class1[*Ts]:
                pass

            class Class2[T, *Ts]:
                pass

            class Class3[T, *Ts, T2]:
                pass

            for cls, base, expected in (
                (Class1[int, str], Class1[int, str], True),
                (Class1[int, bool], Class1[int, str], False),
                (Class2[str, int, float], Class2[str, int, float], True),
                (Class2[str, int, float], Class2[str, int, str], False),
                (Class2[str, int, float], Class2, True),
                (Class3[str, int, float, int], Class3[str, int, float, int], True),
                (Class3[str, int, float, int], Class3[str, int, str, int], False),
            ):

                result = issubclass_typing(cls, base)
                print(f"Testing issubclass_typing({get_type_name(cls)}, {get_type_name(base)}) ==> {result}")
                assert result == expected


        def test_get_executing_function(self):

            def generic_function[T](arg1: T, arg2: int) -> tuple[AnyFunction, TypeArgs] | None: # pyright: ignore[reportInvalidTypeVarUse]
                if fn := get_executing_function():
                    args = get_generic_parameters(fn)
                    return fn, args

            result = generic_function(1,2)

            assert result

            fn, args = result

            assert fn is generic_function
            assert args
            assert isinstance(args[0], TypeVar)

        def test_generic_class_without_typevars(self):
            # generics without typevars is a new feature in python 3.12

            class GenericClass[T]:
                def __init__(self):
                    self.cls = get_original_class(self)
                    self.args = get_generic_arguments(self)

            typevar, *remaining = get_generic_parameters(GenericClass)
            assert typevar and not remaining
            parmtypes = get_types_from_typevar(cast(TypeVar, typevar))
            assert parmtypes == type[Any]

            assert is_generic_type(GenericClass)
            assert not is_subscripted_generic_type(GenericClass)

            cls1 = GenericClass[str]

            assert not is_generic_type(cls1)
            assert is_subscripted_generic_type(cls1)

            inst = cls1()

            assert inst.args == (str,)
            assert inst.cls == cls1


            class GenericClass1[T: int]:
                def __init__(self):
                    self.cls = get_original_class(self)
                    self.args = get_generic_arguments(self)

            typevar, *remaining = get_generic_parameters(GenericClass1)
            assert typevar and not remaining
            parmtypes = get_types_from_typevar(cast(TypeVar, typevar))
            assert parmtypes == int

            class GenericClass2[T: int|str]:
                def __init__(self):
                    self.cls = get_original_class(self)
                    self.args = get_generic_arguments(self)

            typevar, *remaining = get_generic_parameters(GenericClass2)
            assert typevar and not remaining
            parmtypes = get_types_from_typevar(cast(TypeVar, typevar))
            assert parmtypes == int|str


        def test_generic_function_without_typevars(self):
            # generics without typevars is a new feature in python 3.12

            def normal_function(): pass


            def test_function[T: int](arg1: T, arg2: int) -> T:
                ...

            assert not is_generic_function(normal_function)
            assert is_generic_function(test_function)

            typevar, *remaining = get_generic_parameters(test_function)

            assert typevar and not remaining
            assert isinstance(typevar, TypeVar)
            assert getattr(typevar, "__name__") == "T"

            parmtypes = get_types_from_typevar(cast(TypeVar, typevar))
            assert parmtypes == int
