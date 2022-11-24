
from utils import get_title, get_favicon_url, get_first_h1_in_body, get_meta_name
from scraping import do_get_request, get_soup_for_html

import uvicorn
from fastapi import FastAPI, status
from pydantic import BaseModel, HttpUrl

app = FastAPI()

# models

class HTMLBaseInfo(BaseModel):
    title: str | None
    metaName: str | None
    faviconUrl: str | None
    firstH1: str | None

# routes

@app.get(
    path="/v1/get-html-base-info",
    summary="Get HTML base info that includes title, meta name, favicon url and first h1",
    description="Get HTML base info that includes title, meta name, favicon url and first h1",
    tags=["html", "scraping"],
    status_code=status.HTTP_200_OK,
    response_model=HTMLBaseInfo,
)
def get_html_base_info(url: HttpUrl):
    response = do_get_request(url)
    soup = get_soup_for_html(response.content)
    new_base_info = HTMLBaseInfo(
        title=get_title(soup),
        metaName=get_meta_name(soup),
        faviconUrl=get_favicon_url(soup),
        firstH1=get_first_h1_in_body(soup),
    )
    return new_base_info

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
