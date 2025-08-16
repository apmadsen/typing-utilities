[Documentation](/docs/documentation.md) >
 [v0.1](/docs/0.1/version.md) >
  [typingutils](/docs/0.1/typingutils/module.md) >
   is_literal

# is_literal(obj: _Any_) -> _bool_

The `is_literal` function checks whenter or not object is an literal.


## Parameters

- obj `Any`: The object to check.

### Example:
```python
is_literal(Literal[1,2,3]) # => True
is_literal(Literal[1,"b",True]) # => True
```