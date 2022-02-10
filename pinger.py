import asyncio
import aiohttp
from os import getenv

url_list = getenv('URLS', '').split(',')

async def fetch(session: aiohttp.ClientSession, url: str):
    async with session.get(url) as response:
        return response

async def fetch_all(urls: list[str]):
    async with aiohttp.ClientSession(loop=asyncio.get_event_loop()) as session:
        results = await asyncio.gather(*[fetch(session, url) for url in urls], return_exceptions=True)
        return results

if __name__ == '__main__':
    urls = [a for a in url_list if a]
    htmls = asyncio.run(fetch_all(urls))
    print(f'Pinged {len(urls)} url{"s" if len(urls) > 1 else "" }!')
