from typing import Any, TypeVar, Type, cast
from pydantic import BaseModel


T = TypeVar("T")


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


class QueryModel(BaseModel):
    search_query: str
    criteria: str

    @staticmethod
    def from_dict(obj: Any) -> 'QueryModel':
        assert isinstance(obj, dict)
        search_query = from_str(obj.get("search_query"))
        criteria = from_str(obj.get("criteria"))
        return QueryModel(search_query, criteria)

    def to_dict(self) -> dict:
        result: dict = {}
        result["search_query"] = from_str(self.search_query)
        result["criteria"] = from_str(self.criteria)
        return result


def query_model_from_dict(s: Any) -> QueryModel:
    return QueryModel.from_dict(s)


def query_model_to_dict(x: QueryModel) -> Any:
    return to_class(QueryModel, x)
