from fastapi import FastAPI

# API MODELS
from src.dtos.query_model import QueryModel
from src.dtos.mirror_model import MirrorModel

# scapers
from src.scrapers.libgen_scrapper import get_libgen_rs_fiction_scraper, get_download_links

app = FastAPI()

@app.get("/")
async def root():
    return {"message" : "Welcome to Books API"}


@app.post("/book")
async def getsearchResults(query: QueryModel):
    return get_libgen_rs_fiction_scraper(query.search_query, query.criteria, 1, [])

@app.post("/dl")
async def get_book_download_links(mirror: MirrorModel):
    return get_download_links(mirror.mirror)
