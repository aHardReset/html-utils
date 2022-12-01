from html_utils import main, utils

from fastapi.testclient import TestClient
from bs4 import BeautifulSoup


def get_mocked_payload():
    with open("tests/html_snapshots/pydantic.html") as f:
        content = f.read()
    return content


client = TestClient(main.app)


# create a test class
class TestHtmlBaseInfo:

    def test_get_html_base_info_utils(self):
        """
        Test the functions in utils.py with a pre defined html payload
        """

        soup = soup = BeautifulSoup(get_mocked_payload(), main.HTML_PARSER)

        assert '../../favicon.png' == utils.get_favicon_url(soup)
        assert 'Models' in utils.get_title(soup)
        assert 'Data validation' in utils.get_meta_name(soup)
        assert 'Models' == utils.get_first_h1_in_body(soup)

    def test_get_html_base_info(self, monkeypatch):
        """
        Test the html_get_base_info function with a pre defined html payload
        """
        api_request_url = (
            "/v1/get-html-base-info?"
            + "url=https://pydantic-docs.helpmanual.io/usage/models/"
        )
        monkeypatch.setattr(
            utils,
            "get_web_page_content",
            lambda url: get_mocked_payload()
        )
        html_info = client.get(api_request_url)
        html_info = html_info.json()
        assert '../../favicon.png' == html_info.get('faviconUrl')
        assert 'Models' in html_info.get('title')
        assert 'Data validation' in html_info.get('metaName')
        assert 'Models' == html_info.get('firstH1')
