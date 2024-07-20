# Books API
Another simple libgen.rs scraper because every other one were kinda ass. Wrapped with Fastapi to make my life easier. 

## Search
###  URL: 
 ```http
POST http://localhost:8000/book
```

### Request: 
```javascript
{"search_query": "harry potter", "criteria":"title"} //Searched on the basis of title or authors
```
  
#### Response:
```javascript
[
  {
    "author": "MacNabb, Matt, ",
    "title": "A Secret History of Brands: The Dark and Twisted Beginnings of the Brand Names We Know and Love",
    "id": "E7767A85526FD26AC32A5B6DD8C3A7F7",
    "language": "English",
    "download_links": "http://library.lol/fiction/E7767A85526FD26AC32A5B6DD8C3A7F7"
  }
]
```

## Fetch Download Links
###  URL: 
 ```http
POST http://localhost:8000/dl
```

### Request: 
```
javascript
{"mirror": "http://library.lol/fiction/E7767A85526FD26AC32A5B6DD8C3A7F7"} // download_links from previous API
```
  
#### Response:
```javascript
{
  "GET": "https://download.library.lol/fiction/2083000/e7767a85526fd26ac32a5b6dd8c3a7f7.epub/MacNabb%2C%20Matt_%20%20-%20A%20Secret%20History%20of%20Brands_%20The%20Dark%20and%20Twisted%20Beginnings%20of%20the%20Brand%20Names%20We%20Know%20and%20Love.epub",
  "Cloudflare": "https://cloudflare-ipfs.com/ipfs/bafykbzacedukmx6r52i5q4jfa34i2gp7d63fjm5riawkj4u23awmfmxvv66wo?filename=MacNabb%2C%20Matt_%20%20-%20A%20Secret%20History%20of%20Brands_%20The%20Dark%20and%20Twisted%20Beginnings%20of%20the%20Brand%20Names%20We%20Know%20and%20Love.epub",
  "IPFS.io": "https://gateway.ipfs.io/ipfs/bafykbzacedukmx6r52i5q4jfa34i2gp7d63fjm5riawkj4u23awmfmxvv66wo?filename=MacNabb%2C%20Matt_%20%20-%20A%20Secret%20History%20of%20Brands_%20The%20Dark%20and%20Twisted%20Beginnings%20of%20the%20Brand%20Names%20We%20Know%20and%20Love.epub"
}
```
