from danpung_load_test import scrap_urls
from time import perf_counter
import pytest
import asyncio


@pytest.mark.asyncio
async def test_get_title():

    time_before = perf_counter()
    """ Test get_title function """
    google_url = "https://www.google.com"
    title = await scrap_urls.get_title(google_url)
    assert title == "Google"

    youtube_url = "https://www.youtube.com"
    title = await scrap_urls.get_title(youtube_url)
    assert title == "YouTube"
    print(f"Time taken: {perf_counter() - time_before}")

    time_before = perf_counter()
    results = await asyncio.gather(
        scrap_urls.get_title(google_url),
        scrap_urls.get_title(youtube_url)
    )
    print(f"Time taken for gather: {perf_counter() - time_before}")
    assert results[0] == "Google"
    assert results[1] == "YouTube"

@pytest.mark.asyncio
async def test_scan_urls():
    """ Test scan_urls function """
    url = "https://www.google.com"
    url_list = await scrap_urls.scan_urls(url)
    # print(url_list)
    assert len(url_list) > 0

    url = "https://www.youtube.com"
    url_list = await scrap_urls.scan_urls(url)
    # print(url_list)
    assert len(url_list) > 0

@pytest.mark.asyncio
async def test_scrap_urls():
    """ Test scrap_urls function """
    # url = "https://www.google.com"
    # url_list = scrap_urls.scrap_urls([url], 3)
    # print(url_list)
    # assert len(url_list) > 0

    time_before = perf_counter()

    url = "https://www.youtube.com"
    url_list = await scrap_urls.scrap_urls([url], 3, 100)
    print(f"Number of URLs: {len(url_list)}")
    assert len(url_list) > 0

    print(f"Time taken: {perf_counter() - time_before}")
