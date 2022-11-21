from danpung_load_test import scrap_urls
import os
import lorem


async def generate_mkdn(url_list: list[str], directory: str) -> None:
    """ Generate markdown file """
    resultUrlList = await scrap_urls.scrap_urls(scrap_urls.UrlList(url_list), 1, 10)
    print(f"Number of URLs: {len(resultUrlList)}")

    for idx, url in enumerate(resultUrlList):
        title = url.title.strip().replace('\n', '')
        if title == "":
            title = lorem.sentence()
        filename = os.path.join(directory, f"file_{idx+1}.md")
        try:
            with open(filename, "w") as file:
                file.write(f"# {title}")
                file.write(f"\n\n")
                file.write(f"## {lorem.paragraph()}")
                file.write(f"\n\n")
                file.write(f"[{title}]({url.path})")
                file.write(f"\n\n")
                file.write(f"## {lorem.paragraph()}")
        except Exception as e:
            print(f"Error: {e}")
