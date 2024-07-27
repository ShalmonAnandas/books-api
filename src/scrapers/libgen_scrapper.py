import requests
from bs4 import BeautifulSoup

def get_libgen_rs_fiction_scraper(query: str) -> list:
    r = requests.get(f"https://libgen.gs/index.php?req={query}&columns%5B%5D=t&columns%5B%5D=a&topics%5B%5D=l&topics%5B%5D=f&res=100&covers=on")

    soup = BeautifulSoup(r.content, 'html.parser')

    results = []

    table = soup.find("table", class_="table table-striped")
    tbody = table.find("tbody")
    rows = tbody.find_all("tr")

    for row in rows:
        # Extracting image source
        img_tag = row.find('td').find('img')
        img_src = img_tag['src'] if img_tag else None

        # Extracting title
        title_tag = row.find('a', title=True)
        title = title_tag['title'].split("<br>")[1] if title_tag else None

        # Extracting author
        author_tag = row.find_all('td')[2]
        author = author_tag.text.strip() if author_tag else None

        # Extracting release date
        release_date_tag = row.find_all('td')[4].find('nobr')
        release_date = release_date_tag.text.strip() if release_date_tag else None

        # Extracting language
        language_tag = row.find_all('td')[5]
        language = language_tag.text.strip() if language_tag else None

        # Extracting URL
        url_tag = row.find('a', href=True, title="libgen.is")
        url = url_tag['href'] if url_tag else None

        # Create JSON object
        json_obj = {
            "author": author,
            "title": title,
            "poster": f"https://libgen.gs{str(img_src).replace("_small", "")}",
            # "id": title_href.split("/")[2],
            "language": language,
            "release_date": release_date,
            "download_links": url
        }
        
        # Add to list
        results.append(json_obj)

    return results
    
def get_download_links(mirror: str):
    MIRROR_SOURCES = ["GET", "Cloudflare", "IPFS.io", "Infura"]

    page = requests.get(mirror)
    soup = BeautifulSoup(page.text, "html.parser")
    links = soup.find_all("a", string=MIRROR_SOURCES)
    download_links = {link.string: link["href"] for link in links}
    return download_links