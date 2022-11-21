from dataclasses import dataclass
import requests
from bs4 import BeautifulSoup
import asyncio

@dataclass
class UrlItem:
    """Class for Url Information."""
    title: str
    path: str


# type alias for url list
UrlList = list[str]


def _convert_to_url_list(url_list: list[UrlItem]) -> UrlList:
    """ Convert UrlItem list to UrlList """
    return [url.path for url in url_list]


async def scrap_urls(url_list: UrlList, depth: int, limit: int) -> list[UrlItem]:
    """ scrap url list and return the list of urls found in the pages """

    if depth < 0:
        raise ValueError("The depth must be greater than 0")

    if depth == 0:
        return []

    new_url_list = []
    for url in url_list:
        # 1. Add the url to the new_url_list
        title = await get_title(url)
        new_url_list.append(UrlItem(title, url))

        # 2. Add the list of urls found in the page to the new_url_list
        urls_found = await scan_urls(url)
        new_url_list.extend(urls_found)

        # 3. Add the list of urls found in the urls found in the page to the new_url_list
        if len(urls_found) < limit:
            new_url_list.extend(await scrap_urls(
                _convert_to_url_list(urls_found), depth - 1, limit))
        else:
            new_url_list.extend(await scrap_urls(_convert_to_url_list(
                urls_found[0::limit]), depth - 1, limit))

    return new_url_list


async def scan_urls(url: str) -> list[UrlItem]:
    """ scan the content of the url and return the list of urls found in the page """
    url_list = []
    # scan the content of the url and return the list of urls found in the page
    # making requests instance
    reqs = requests.get(url)

    # using the BeautifulSoup module
    soup = BeautifulSoup(reqs.text, 'html.parser')

    for link in soup.findAll('a'):
        ahref = link.get('href')
        if ahref is not None:
            atext = link.text
            if atext is not None:
                if ahref.startswith("http"):
                    url_list.append(UrlItem(link.text, ahref))
                else:
                    url_list.append(UrlItem(link.text, url + ahref))
            else:
                title = await get_title(ahref)
                if ahref.startswith("http"):
                    url_list.append(UrlItem(title, ahref))
                else:
                    url_list.append(UrlItem(title, url + ahref))
    return url_list


async def get_title(url: str) -> str:
    """ Get the title of the url content """
    title_found = ""
    # making requests instance
    try:
        reqs = requests.get(url)

        # using the BeautifulSoup module
        soup = BeautifulSoup(reqs.text, 'html.parser')

        # displaying the title
        for title in soup.find_all('title'):
            title_found = title.get_text()

        if title_found == "":
            title_found = "No title found"
    except:
        print("Error getting title from url: " + url)

    return title_found
