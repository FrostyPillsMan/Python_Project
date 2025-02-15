"""Basic asyncio"""

from typing import Optional
import httpx
from bs4 import BeautifulSoup
import asyncio
import httpx
from bs4 import BeautifulSoup


async def fetch_content(url: str) -> None:
    """Fetches and prints the title of a webpage given its URL."""
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, "html.parser")
            title: Optional[str] = soup.title.string if soup.title else "No title found"
            print(f"Title of {url}: {title}")
        except httpx.HTTPStatusError as e:
            print(f"Failed to fetch {url}. Status code: {e.response.status_code}")

async def main():
    urls = [
        "https://www.google.com/",
        "https://www.python.org/",
        "https://www.youtube.com/",
        "https://www.nonexistentwebsite12345/"
    ]
    tasks = [fetch_content(url) for url in urls]
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(main())

