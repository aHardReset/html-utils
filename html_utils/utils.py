from bs4 import BeautifulSoup
from bs4 import element


def get_title(soup: BeautifulSoup) -> (None | str):
    """search the title tag of a web page

    Args:
        soup (BeautifulSoup): the soup object of the web page

    Returns:
        str or None: the title of the web page or None if not found
    """
    title = soup.find("title")
    if type(title) is element.Tag:
        return title.string
    return None


def get_meta_name(soup: BeautifulSoup) -> (str | None):
    """search the meta tag of a web page and returns the content of the
    name attribute

    Args:
        soup (BeautifulSoup): the soup object of the web page

    Returns:
        str or None: the content of the name attribute or None if not found
    """

    meta_name = soup.find("meta", {"name": "description"}) or {}
    if type(meta_name) is element.Tag:
        content = meta_name.get("content", None)
        if content:
            return str(content)
    return None


def get_favicon_url(soup: BeautifulSoup) -> (str | None):
    """search the favicon url of a web page

    Args:
        soup (BeautifulSoup): the soup object of the web page

    Returns:
        str or None: the favicon url of the web page or None if not found
    """

    favicon = soup.find("link", {"rel": "icon"}) or {}
    if type(favicon) is element.Tag:
        favicon_url = favicon.get("href", None)
        if favicon_url:
            return str(favicon_url)
    return None


def get_first_h1_in_body(soup: BeautifulSoup) -> (str | None):
    """search the first h1 in the body of a web page

    Args:
        soup (BeautifulSoup): the soup object of the web page

    Returns:
        str or None: the first h1 in the body of the web page
        or None if not found
    """
    body = soup.find("body")
    if type(body) is element.Tag:
        h1 = body.find("h1")

        if type(h1) is element.Tag:
            return h1.string
    return None
