from typing import Union
from fastapi import FastAPI
from libgen_api import LibgenSearch
import uvicorn

# API MODELS
from dtos.book_result_model import Book
from dtos.query_model import QueryModel

app = FastAPI()

# LIBGEN SEARCH INIT
libgen = LibgenSearch()


@app.get("/")
async def root():
    return {"message" : "Welcome to Books API"}


@app.post("/book")
async def getsearchResults(query: QueryModel):
    return searchBook(query.search_query, False)


@app.post("/author")
async def getSearchResultsByAuthor(query: QueryModel):
    results = searchBook(query.search_query, True)
    return results


@app.post("/links")
async def getDownloadLinks(item: Book):
    return getDownload(item)


async def searchBook(searchTerm: str, isSearchAuthor: bool):
    if isSearchAuthor:
        results = libgen.search_author(searchTerm.replace("%20", " "))
    else:
        results = libgen.search_title(searchTerm.replace("%20", " "))
    tempList = []
    for result in results:
        lowercase_data = {k.lower(): v for k, v in result.items()}
        tempList.append(lowercase_data)
    return tempList


async def getDownload(downloadLink: Book):
    return libgen.resolve_download_links(downloadLink.to_dict())