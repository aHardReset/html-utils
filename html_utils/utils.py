from bs4 import BeautifulSoup
import requests


def get_title(soup: BeautifulSoup) -> str or None:
    """ search the title tag of a web page

    Args:
        soup (BeautifulSoup): the soup object of the web page

    Returns:
        str or None: the title of the web page or None if not found
    """
    title = soup.find("title")
    if not title:
        return None
    return title.string


def get_meta_name(soup: BeautifulSoup) -> str or None:
    """ search the meta tag of a web page and returns the content of the
    name attribute

    Args:
        soup (BeautifulSoup): the soup object of the web page

    Returns:
        str or None: the content of the name attribute or None if not found
    """

    meta_name = soup.find("meta", {"name": "description"}) or {}
    return meta_name.get("content", None)


def get_favicon_url(soup: BeautifulSoup):
    """ search the favicon url of a web page

    Args:
        soup (BeautifulSoup): the soup object of the web page

    Returns:
        str or None: the favicon url of the web page or None if not found
    """

    favicon_url = soup.find("link", {"rel": "icon"}) or {}
    return favicon_url.get("href", None)


def get_first_h1_in_body(soup: BeautifulSoup):
    """ search the first h1 in the body of a web page

    Args:
        soup (BeautifulSoup): the soup object of the web page

    Returns:
        str or None: the first h1 in the body of the web page
        or None if not found
    """
    first_h1 = soup.find("body").find("h1")
    if not first_h1:
        return None
    return first_h1.string


def get_web_page_content(url: str) -> str:
    """ Given a url, do a get request and return the
    response content compatible with BeautifulSoup

    Args:
        url (str): the url of the web page

    Returns:
        str: the response content of the web page
    """
    response = requests.get(url)
    return response.content
