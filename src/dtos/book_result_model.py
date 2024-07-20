from typing import Any, TypeVar, Type, cast
from pydantic import BaseModel


T = TypeVar("T")


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


class Book(BaseModel):
    id: int
    author: str
    title: str
    publisher: str
    year: int
    pages: Any
    language: str
    size: str
    extension: str
    mirror_1: str
    mirror_2: str
    mirror_3: str

    @staticmethod
    def from_dict(obj: Any) -> "Book":
        assert isinstance(obj, dict)
        id = int(from_str(obj.get("id")))
        author = from_str(obj.get("author"))
        title = from_str(obj.get("title"))
        publisher = from_str(obj.get("publisher"))
        year = int(from_str(obj.get("year")))
        pages = int(from_str(obj.get("pages")))
        language = from_str(obj.get("language"))
        size = from_str(obj.get("size"))
        extension = from_str(obj.get("extension"))
        mirror_1 = from_str(obj.get("mirror_1"))
        mirror_2 = from_str(obj.get("mirror_2"))
        mirror_3 = from_str(obj.get("mirror_3"))
        return Book(
            id,
            author,
            title,
            publisher,
            year,
            pages,
            language,
            size,
            extension,
            mirror_1,
            mirror_2,
            mirror_3,
        )

    def to_dict(self) -> dict:
        result: dict = {}
        result["ID"] = from_str(str(self.id))
        result["Author"] = from_str(self.author)
        result["Title"] = from_str(self.title)
        result["Publisher"] = from_str(self.publisher)
        result["Year"] = from_str(str(self.year))
        result["Pages"] = from_str(str(self.pages))
        result["Language"] = from_str(self.language)
        result["Size"] = from_str(self.size)
        result["Extension"] = from_str(self.extension)
        result["Mirror_1"] = from_str(self.mirror_1)
        result["Mirror_2"] = from_str(self.mirror_2)
        result["Mirror_3"] = from_str(self.mirror_3)
        return result


def book_from_dict(s: Any) -> Book:
    return Book.from_dict(s)


def book_to_dict(x: Book) -> Any:
    return to_class(Book, x)
