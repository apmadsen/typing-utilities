[![Test](https://github.com/apmadsen/typing-utilities/actions/workflows/python-test.yml/badge.svg)](https://github.com/apmadsen/typing-utilities/actions/workflows/python-test.yml)
[![Coverage](https://github.com/apmadsen/typing-utilities/actions/workflows/python-test-coverage.yml/badge.svg)](https://github.com/apmadsen/typing-utilities/actions/workflows/python-test-coverage.yml)
[![Stable Version](https://img.shields.io/pypi/v/typing-utilities?label=stable&sort=semver&color=blue)](https://github.com/apmadsen/typing-utilities/releases)
![Pre-release Version](https://img.shields.io/github/v/release/apmadsen/typing-utilities?label=pre-release&include_prereleases&sort=semver&color=blue)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/typing-utilities)
[![PyPI Downloads](https://static.pepy.tech/badge/typing-utilities/week)](https://pepy.tech/projects/typing-utilities)

# Typing Utilities

Utilities for working with complex types and generics in Python — with a focus on validation, correctness, and clarity.

## 🚀 Why this exists

Python’s type system has become significantly more powerful with the introduction of type hints and generics.

However, working with types at runtime still has challenges:

- Complex generics are difficult to validate
- Type relationships are not always easy to reason about
- Runtime behavior and static typing don’t always align
- Built-in utilities are limited for advanced scenarios

👉 This library provides tools to **bridge the gap between static typing and runtime validation**.


## ✨ Features

- 🧠 Validation of complex types and generics
- 🔍 Inspection of type relationships
- ⚖️ More predictable handling of type constraints
- 🧩 Utilities for working with advanced typing patterns
- ⚡ Lightweight and focused API


## 📦 Use cases

This library is useful when working with:

- Type-heavy systems
- Framework or library development
- Validation layers
- Data processing systems
- Dynamic architectures relying on type hints

👉 Especially valuable when type correctness matters beyond static analysis.


## 🏗 Design philosophy

This project is built around a few core principles:

### 1. Runtime awareness of types
Type hints shouldn’t just exist for linters —
they should be usable and enforceable at runtime where needed.

### 2. Simplicity over completeness
The goal is not to cover every edge case in Python’s typing system,
but to provide practical utilities for real-world problems.

### 3. Complement, not replace
This library works alongside Python’s built-in `typing` module,
extending it rather than abstracting it away.


## 🔗 What this enables

By introducing stronger type utilities at runtime, you can:

- Validate data and inputs more reliably
- Build safer abstraction layers
- Reduce subtle bugs caused by incorrect type assumptions
- Align runtime behavior with type annotations

👉 This is particularly useful in systems where correctness is critical.


## ⚖️ Trade-offs

| Focus ✅ | Not a goal ❌ |
|---------|--------------|
| Practical type validation | Full typing system reimplementation |
| Lightweight utilities | Heavy abstraction layers |
| Real-world usefulness | Covering every typing edge case |

👉 The library prioritizes **clarity and usefulness over completeness**.


## 🧠 Context

This project fits into a broader effort to improve:

- Runtime abstractions
- Developer tooling
- Type-driven design in Python

It is particularly complementary to:

- Dependency injection systems
- Reflection/introspection tools
- Validation frameworks


## 🎯 When to use

Use this library if you:

- Work with complex or nested types
- Need runtime validation of generics
- Build systems where type correctness matters
- Want better guarantees beyond static analysis


## 🚫 When not to use

This library may not be necessary if:

- Your type usage is simple
- Static type checking (e.g. mypy/pyright) is sufficient
- Runtime validation is not required


## 🔗 Related projects

Part of a broader focus on:

- Clean architecture
- Runtime introspection
- Structured Python systems

👉 https://github.com/apmadsen


## 🤝 Contributing

Feedback and contributions are welcome!


## Example:

```python
from typing import Generic, TypeVar
from typingutils import issubclass_typing, isinstance_typing

T = TypeVar('T')

class Class1(Generic[T]):
    pass

class_type1 = Class1[str]
class_type2 = Class1[int]

issubclass_typing(class_type1, class_type2) # => False

# next line will fail
issubclass(class_type1, class_type2) # => TypeErrorr: Subscripted generics cannot be used with class and instance checks

class_inst1 = class_type1()
class_inst2 = class_type2()

isinstance_typing(class_inst1, class_type1) # => True
isinstance_typing(class_inst1, class_type2) # => False
isinstance_typing(class_inst2, class_type2) # => True
isinstance_typing(class_inst2, class_type1) # => False

# next line will fail
isinstance(class_inst1, class_type1) # => TypeError: Subscripted generics cannot be used with class and instance checks
```

## Full documentation

[Go to documentation](https://github.com/apmadsen/typing-utilities/blob/main/docs/documentation.md)
