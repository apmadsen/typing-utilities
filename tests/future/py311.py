# pyright: basic
import sys

if sys.version_info >= (3, 11):
    from typing import Any, TypeVar, TypeVarTuple, Unpack, Generic
    from pytest import raises as assert_raises, fixture

    from typingutils import get_generic_parameters, get_generic_arguments, get_type_name, issubclass_typing
    from typingutils.internal import get_types_from_typevar

    class TestPython311:

        def test_typevar_tuples(self):

            Ts = TypeVarTuple("Ts")

            class Class1(Generic[Unpack[Ts]]):
                pass

            assert get_types_from_typevar(Ts) == tuple[type[Any], ...]

            assert get_type_name(Ts) == "*Ts"

            inst = Class1[int, str, bool]

            assert get_generic_parameters(Class1) == (Ts,)
            assert get_generic_arguments(inst) == (int, str, bool)


        def test_is_subclass_with_typevar_tuples(self):
            T = TypeVar("T", bound=str)
            T2 = TypeVar("T2", bound=int)
            T3 = TypeVar("T3")
            Ts = TypeVarTuple("Ts")

            class Class1(Generic[Unpack[Ts]]):
                pass

            class Class2(Generic[T, Unpack[Ts]]):
                pass

            class Class3(Generic[T, Unpack[Ts], T2]):
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
