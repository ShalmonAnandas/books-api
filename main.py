from typing import Union
from fastapi import FastAPI
from libgen_api import LibgenSearch
import uvicorn

# API MODELS
from models.book_result_model import Book
from models.query_model import QueryModel

app = FastAPI()

# LIBGEN SEARCH INIT
libgen = LibgenSearch()


@app.get("/")
def read_root():
    return "Welcome to Books API"


@app.post("/book")
def getsearchResults(query: QueryModel):
    return searchBook(query.search_query, False)


@app.post("/author")
def getSearchResultsByAuthor(query: QueryModel):
    results = searchBook(query.search_query, True)
    return results


@app.post("/links")
def getDownloadLinks(item: Book):
    return getDownload(item)


def searchBook(searchTerm: str, isSearchAuthor: bool):
    if isSearchAuthor:
        results = libgen.search_author(searchTerm.replace("%20", " "))
    else:
        results = libgen.search_title(searchTerm.replace("%20", " "))
    tempList = []
    for result in results:
        lowercase_data = {k.lower(): v for k, v in result.items()}
        tempList.append(lowercase_data)
    return tempList


def getDownload(downloadLink: Book):
    return libgen.resolve_download_links(downloadLink.to_dict())


if __name__ == "__main__":
    uvicorn.run(app)
