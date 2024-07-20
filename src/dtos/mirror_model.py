from typing import Any, TypeVar, Type, cast
from pydantic import BaseModel


T = TypeVar("T")


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


class MirrorModel(BaseModel):
    mirror: str

    @staticmethod
    def from_dict(obj: Any) -> 'MirrorModel':
        assert isinstance(obj, dict)
        mirror = from_str(obj.get("mirror"))
        return MirrorModel(mirror)

    def to_dict(self) -> dict:
        result: dict = {}
        result["mirror"] = from_str(self.mirror)
        return result


def mirror_model_from_dict(s: Any) -> MirrorModel:
    return MirrorModel.from_dict(s)


def mirror_model_to_dict(x: MirrorModel) -> Any:
    return to_class(MirrorModel, x)
