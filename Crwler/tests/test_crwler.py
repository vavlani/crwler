import pytest
from src import crwler
import tempfile


def test_crawl_website(mocker):
    # Your test cases for crwler.py
    with tempfile.TemporaryDirectory() as tmpdirname:
        test_url = 'https://googleapis.github.io/google-api-python-client/docs/dyn/slides_v1.html'
        


