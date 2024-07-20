from typing import Union
from fastapi import FastAPI
from libgen_api import LibgenSearch
import uvicorn

# API MODELS
from src.dtos.book_result_model import Book
from src.dtos.query_model import QueryModel

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


def searchBook(searchTerm: str, isSearchAuthor: bool):
    if isSearchAuthor:
        results =  libgen.search_author_filtered(searchTerm.replace("%20", " "), {"Language": "English"})
    else:
        results =  libgen.search_title_filtered(searchTerm.replace("%20", " "), {"Language": "English"})
    tempList = []
    for result in results:
        lowercase_data = {k.lower(): v for k, v in result.items()}
        download_links = libgen.resolve_download_links(result)
        lowercase_data["mirror_1"] = download_links["GET"]
        lowercase_data["mirror_2"] = download_links["Cloudflare"]
        lowercase_data["mirror_3"] = download_links["IPFS.io"]
        tempList.append(lowercase_data)
    return tempList