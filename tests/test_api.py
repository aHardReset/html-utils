import requests
from bs4 import BeautifulSoup
from fastapi.testclient import TestClient

from html_utils import main
from html_utils import utils


def get_mocked_payload():
    with open("tests/html_snapshots/pydantic.html") as f:
        content = f.read()
    return content


def get_mocked_empty_payload():
    with open("tests/html_snapshots/empty_but_valid_html.html") as f:
        content = f.read()
    return content


class MockedPayload:
    def __init__(self):
        self.content = get_mocked_payload()


client = TestClient(main.app)


class TestHtmlBaseInfo:
    """
    This class is used as a wrapper for the tests of the html base info view
    """

    def test_get_html_base_info_utils(self):
        """
        Test the functions in utils.py with a pre defined html payload
        """

        soup = BeautifulSoup(get_mocked_payload(), main.HTML_PARSER)

        assert "../../favicon.png" == utils.get_favicon_url(soup)

        title = utils.get_title(soup)
        assert title is not None
        assert "Models" in title

        meta_name = utils.get_meta_name(soup)
        assert meta_name is not None
        assert "Data validation" in meta_name
        assert "Models" == utils.get_first_h1_in_body(soup)

    def test_get_html_base_info(self, monkeypatch):
        """
        Test the html_get_base_info function with a pre defined html payload
        """
        api_request_url = (
            "/v1/get-html-base-info?"
            + "url=https://pydantic-docs.helpmanual.io/usage/models/"
        )
        monkeypatch.setattr(requests, "get", lambda url: MockedPayload())
        html_info = client.get(api_request_url)
        html_info = html_info.json()
        assert "../../favicon.png" == html_info.get("faviconUrl")
        assert "Models" in html_info.get("title")
        assert "Data validation" in html_info.get("metaName")
        assert "Models" == html_info.get("firstH1")

    def test_get_html_base_info_with_invalid_url(self):
        """
        Test the html_get_base_info function with an invalid url
        """
        api_request_url = (
            "/v1/get-html-base-info?" + "url=this-is-an-invalid-url-string"
        )
        html_info = client.get(api_request_url)
        assert html_info.status_code == 422


class TestUtilsForHtmlBaseInfo:
    """
    This class is used as a wrapper for the unit tests of the utils functions
    """

    def test_get_title(self):
        """
        Test the get_title function with
        a pre defined html payload with a title
        """
        soup = BeautifulSoup(get_mocked_payload(), main.HTML_PARSER)

        title = utils.get_title(soup)
        assert title is not None
        assert "Models" in title

    def test_get_favicon_url(self):
        """
        Test the get_favicon_url function with
        a pre defined html payload with a favicon
        """
        soup = BeautifulSoup(get_mocked_payload(), main.HTML_PARSER)
        assert "../../favicon.png" == utils.get_favicon_url(soup)

    def test_get_first_h1_in_body(self):
        """
        Test the get_first_h1_in_body function with
        a pre defined html payload with a h1 tag
        """
        soup = BeautifulSoup(get_mocked_payload(), main.HTML_PARSER)
        assert "Models" == utils.get_first_h1_in_body(soup)

    def test_get_meta_name(self):
        """
        Test the get_meta_name function with
        a pre defined html payload with
        a meta tag
        """
        soup = BeautifulSoup(get_mocked_payload(), main.HTML_PARSER)
        meta_name = utils.get_meta_name(soup)
        assert meta_name is not None
        assert "Data validation" in meta_name

    def test_get_title_with_no_title(self):
        """
        Test the get_title function with
        a pre defined html payload with no title
        """
        soup = BeautifulSoup(get_mocked_empty_payload(), main.HTML_PARSER)
        # could be a decompose but we will keep things cheaper
        # soup.title.decompose()
        assert utils.get_title(soup) is None

    def test_get_favicon_url_with_no_favicon(self):
        """
        Test the get_favicon_url function with
        a pre defined html payload with no favicon
        """
        soup = BeautifulSoup(get_mocked_empty_payload(), main.HTML_PARSER)
        assert utils.get_favicon_url(soup) is None

    def test_get_first_h1_in_body_with_no_h1(self):
        """
        Test the get_first_h1_in_body function with
        a pre defined html payload with no h1 tag
        """
        soup = BeautifulSoup(get_mocked_empty_payload(), main.HTML_PARSER)
        assert utils.get_first_h1_in_body(soup) is None

    def test_get_meta_name_with_no_meta(self):
        """
        Test the get_meta_name function with
        a pre defined html payload with no meta tag
        """
        soup = BeautifulSoup(get_mocked_empty_payload(), main.HTML_PARSER)
        assert utils.get_meta_name(soup) is None
