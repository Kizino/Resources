import aiohttp
import asyncio
import time

async def fetch(session, url):
    async with session.get(url) as resp:
        return await resp.json()
         
async def asyncStarter(url_list : list[str]):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in url_list:
            tasks.append(asyncio.ensure_future(fetch(session, url)))

        return await asyncio.gather(*tasks)
    
if __name__ == '__main__':
    start_time = time.time()
    
    pkm_url_list = [f'https://pokeapi.co/api/v2/pokemon/{number}'for number in range(1, 151)]
    response = asyncio.run(asyncStarter(pkm_url_list))

    for pkm in response:
        print(pkm['name'])

    print("--- %s seconds ---" % (time.time() - start_time))
    