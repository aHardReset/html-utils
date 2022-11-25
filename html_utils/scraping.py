import requests
from bs4 import BeautifulSoup

HTML_PARSER = "html.parser"

def do_get_request(url: str) -> requests.Response:
    response = requests.get(url)
    return response

def get_soup_for_html(html_payload: str or bytes, html_parser: str = HTML_PARSER) -> BeautifulSoup:
    return BeautifulSoup(html_payload, html_parser)