import requests
import json
from bs4 import BeautifulSoup

def get_libgen_rs_fiction_scraper(query: str, criteria: str, page: int = 1, responseList: list = []):
    request = query.replace(" ", "+")
    # print(f"https://libgen.rs/fiction/?q={request}&criteria={criteria}&language=English&page={page}")
    r = requests.get(f"https://libgen.rs/fiction/?q={request}&criteria={criteria}&language=English&page={page}")

    soup = BeautifulSoup(r.content, 'html.parser')

    # Find all <tr> elements within <tbody>
    total_pages = int(soup.find('span', class_="page_selector").text.strip().split("/")[1].strip()) if soup.find('span', "page_selector") else 1
    tbody = soup.find('tbody')
    rows = tbody.find_all('tr')

    # Iterate through each row
    for row in rows:
        # Extract author
        author_td = row.find('td')
        authors = author_td.find_all('a') if author_td else []
        author_list = [author.text.strip() for author in authors]
        author = ", ".join(author_list) if author_list else None
        
        # Extract title and title href
        title_td = row.find_all('td')[2]
        title_a = title_td.find('a') if title_td else None
        title = title_a.text.strip() if title_a else None
        title_href = title_a['href'] if title_a else None
        
        # Extract language
        language_td = row.find_all('td')[3]
        language = language_td.text.strip() if language_td else None
        
        # Extract mirrors
        mirrors_td = row.find_all('td')[5]
        mirrors = mirrors_td.find_all('a') if mirrors_td else []
        mirror_1 = mirrors[0]['href'] if len(mirrors) > 0 else None

        
        
        # Create JSON object
        json_obj = {
            'author': author,
            'title': title,
            "id": title_href.split("/")[2],
            'language': language,
            'download_links': mirror_1
        }
        
        # Add to list
        responseList.append(json_obj)

    if page < total_pages:
        return get_libgen_rs_fiction_scraper(query, criteria, page + 1, responseList)
    else:
        return responseList
    
def get_download_links(mirror: str):
    MIRROR_SOURCES = ["GET", "Cloudflare", "IPFS.io", "Infura"]

    page = requests.get(mirror)
    soup = BeautifulSoup(page.text, "html.parser")
    links = soup.find_all("a", string=MIRROR_SOURCES)
    download_links = {link.string: link["href"] for link in links}
    return download_links