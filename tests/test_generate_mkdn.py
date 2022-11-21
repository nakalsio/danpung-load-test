from danpung_load_test import generate_mkdn
from time import perf_counter
import pytest
import asyncio


@pytest.mark.asyncio
async def test_generate_mkdn():
    """ Test generate_mkdn function """
    time_before = perf_counter()
    
    # tests\test_generate_mkdn.py Number of URLs: 16988
    # Time taken: 55.5314146
    # url_list = [
    #     "https://github.com/dzharii/awesome-typescript",
    #     "https://github.com/vinta/awesome-python"
    # ]
    
    # tests\test_generate_mkdn.py Number of URLs: 123551
    # Time taken: 477.6334055
    url_list = [
        "https://github.com/avelino/awesome-go",
        "https://github.com/rust-unofficial/awesome-rust"
    ]
    await generate_mkdn.generate_mkdn(url_list, "data")
    print(f"Time taken: {perf_counter() - time_before}")
