[Documentation](/docs/documentation.md) >
 [v0.0](/docs/0.0/version.md) >
  [typingutils](/docs/0.0/typingutils/module.md) >
   resolve_annotation

# resolve_annotation(obj: _[AnyType](any_type.md) | Annotated[Any, "any"]_) -> _[AnyType](any_type.md)_

The `resolve_annotation` function resolves annotation into a type or type union, whether being an ordinary type, a Literal or an Annotated instance.

Supported annotations are Literal, Annotated, Required, NotRequired, ReadOnly, ClassVar and Final.

## Parameters

- obj `AnyType | Annotated[Any, "any"]`: The annotation to check.

### Example:
```python
resolve_annotation(Literal[1,"a",3]) -> int | str
resolve_annotation(Annotated[int, "an integer"]) -> int
```