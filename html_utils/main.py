from typing import Optional

import requests
from bs4 import BeautifulSoup
from fastapi import FastAPI
from fastapi import status
from pydantic import BaseModel
from pydantic import HttpUrl
from utils import get_favicon_url
from utils import get_first_h1_in_body
from utils import get_meta_name
from utils import get_title

app = FastAPI()
HTML_PARSER = "html.parser"

# models


class HTMLBaseInfo(BaseModel):
    title: Optional[str]
    metaName: Optional[str]
    faviconUrl: Optional[str]
    firstH1: Optional[str]


# routes


@app.get(
    path="/v1/get-html-base-info",
    summary="""Get HTML base info that includes title,
        meta name, favicon url and first h1""",
    description="""Get HTML base info that includes title,
        meta name, favicon url and first h1""",
    tags=["html", "scraping"],
    status_code=status.HTTP_200_OK,
    response_model=HTMLBaseInfo,
)
def get_html_base_info(url: HttpUrl):
    """Get HTML base info from a web page that includes
    title, meta name, favicon url and first h1

    Args:
        url (HttpUrl): the url of the web page

    Returns:
        HTMLBaseInfo: the base info of the web page
    """

    content = requests.get(url).content
    soup = BeautifulSoup(content, HTML_PARSER)
    new_base_info = HTMLBaseInfo(
        title=get_title(soup),
        metaName=get_meta_name(soup),
        faviconUrl=get_favicon_url(soup),
        firstH1=get_first_h1_in_body(soup),
    )
    return new_base_info
