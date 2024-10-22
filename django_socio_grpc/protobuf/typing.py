from __future__ import annotations

from enum import Enum
from typing import TYPE_CHECKING

try:
    from typing_extensions import NotRequired, TypedDict
except ImportError:
    from typing import Optional as NotRequired
    from typing import TypedDict

if TYPE_CHECKING:
    from .proto_classes import ProtoEnum


class FieldCardinality(str, Enum):
    """
    Enum to use for the ``cardinality`` dictionnary key for grpc_action ``request`` and ``response``
    """

    NONE = ""
    OPTIONAL = "optional"
    REPEATED = "repeated"
    # TODO: ONEOF = "oneof"
    # TODO: MAP = "map"


class FieldDict(TypedDict):
    """
    Typed dict to help format ``request`` and ``response`` params of grpc_action decorator.
    """

    name: str
    type: str | ProtoEnum
    cardinality: NotRequired[FieldCardinality]  # noqa: UP007
    comment: NotRequired[str | list[str]]  # noqa: UP007
