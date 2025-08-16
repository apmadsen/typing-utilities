# pyright: basic
# ruff: noqa
from typing import (
    AbstractSet, Any, AsyncContextManager, AsyncGenerator, AsyncIterable, AsyncIterator,
    Awaitable, Callable, ChainMap, ContextManager, Counter, DefaultDict, Deque, Dict, FrozenSet,
    Generator, ItemsView, Iterable, Iterator, KeysView, List, Literal, Mapping, Match,
    MutableMapping, MutableSequence, MutableSet, NamedTuple, OrderedDict, Pattern, Set, Sequence,
    Tuple, Type, Union, ValuesView, Optional
)
from collections import abc, deque, defaultdict, OrderedDict, Counter, ChainMap
from re import Pattern as rx_Pattern, Match as rx_Match
from contextlib import AbstractContextManager, AbstractAsyncContextManager
from decimal import Decimal
from datetime import datetime, date, time
from types import UnionType

from builtins import tuple, type, list, dict, set, frozenset

from tests.generic_classes import T, T1, T2, Tstr, Tkey, Tvalue

non_generic_types: List[type] = [ str, int, bool, float, date, time, datetime, Decimal ]

generic_types: List[Any] = [
    tuple[T], list[T], dict[Tkey, Tvalue], set[T], frozenset[T], # pyright: ignore[reportGeneralTypeIssues]
    defaultdict[Tkey, Tvalue], OrderedDict[Tkey, Tvalue], deque[T], Counter[T], ChainMap[Tkey, Tvalue], # pyright: ignore[reportGeneralTypeIssues]
    abc.Collection[T], abc.Mapping[Tkey, Tvalue], abc.MutableMapping[Tkey, Tvalue], abc.Sequence[T], abc.MutableSequence[T], # pyright: ignore[reportGeneralTypeIssues]
    abc.MutableSet[T], abc.MappingView[Tkey, Tvalue], abc.KeysView[T], abc.ItemsView[Tkey, Tvalue], abc.ValuesView[T], # pyright: ignore[reportGeneralTypeIssues, reportInvalidTypeArguments]
    rx_Pattern[Tstr], rx_Match[Tstr], # pyright: ignore[reportGeneralTypeIssues]
    AbstractContextManager[T], AbstractAsyncContextManager[T], # pyright: ignore[reportGeneralTypeIssues]
    Tuple[T], List[T], Dict[Tkey, Tvalue], DefaultDict[Tkey, Tvalue], Set[T], FrozenSet[T], Deque[T], # pyright: ignore[reportGeneralTypeIssues]
    Type[T], Mapping[Tkey, Tvalue], Iterator[T], ContextManager[T], AsyncContextManager[T], Pattern[T], Match[T], # pyright: ignore[reportGeneralTypeIssues, reportInvalidTypeArguments]
    AbstractSet[T], Iterable[T], ItemsView[Tkey, Tvalue], KeysView[T], MutableMapping[Tkey, Tvalue], MutableSequence[T], # pyright: ignore[reportGeneralTypeIssues]
    MutableSet[T], Sequence[T], ValuesView[T], Generator[T, T1, T2], AsyncGenerator[T, T1], AsyncIterable[T], AsyncIterator[T], # pyright: ignore[reportGeneralTypeIssues]
    Awaitable[T] # pyright: ignore[reportGeneralTypeIssues]
]

unions: List[UnionType] = [
    Union[int, None],
    Union[str, int],
    int | None,
    str | int,
    Optional[str],
    Optional[Union[int, bool]]
]