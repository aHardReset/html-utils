from bs4 import BeautifulSoup

def get_title(soup: BeautifulSoup):
    # return the title of the page of empty string if not found
    title = soup.find("title")
    return title.string if title else None

def get_meta_name(soup: BeautifulSoup):
    # finds the meta tag and returns the content of the name attribute or empty string if not found
    meta_name = soup.find("meta", {"name": "description"})
    return meta_name["content"] if meta_name else None

def get_favicon_url(soup: BeautifulSoup):
    # finds the favicon url or empty string if not found
    favicon_url = soup.find("link", {"rel": "icon"})
    return favicon_url["href"] if favicon_url else None

def get_first_h1_in_body(soup: BeautifulSoup):
    # finds the first h1 in the body or empty string if not found
    first_h1 = soup.find("body").find("h1")
    return first_h1.string if first_h1 else None
