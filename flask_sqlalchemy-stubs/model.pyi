from ._compat import to_str as to_str
from sqlalchemy.ext.declarative import DeclarativeMeta
from typing import Any

def should_set_tablename(cls): ...

camelcase_re: Any

def camel_to_snake_case(name: Any): ...

class NameMetaMixin:
    def __init__(cls, name: Any, bases: Any, d: Any) -> None: ...
    def __table_cls__(cls, *args: Any, **kwargs: Any): ...

class BindMetaMixin:
    def __init__(cls, name: Any, bases: Any, d: Any) -> None: ...

class DefaultMeta(NameMetaMixin, BindMetaMixin, DeclarativeMeta): ...

class Model:
    query_class: Any = ...
    query: Any = ...