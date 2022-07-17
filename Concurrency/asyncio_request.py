# pip3 install asyncio
# pip3 install aiohttp
import aiohttp
import asyncio
import time
import logging

async def fetch(session, url):
    try:
        async with session.get(url) as resp:
            assert resp.status == 200
            return await resp.json()
    except:
        logging.error(f'Cant fetch data from: {url}')
         
async def asyncStarter(url_list : list[str]):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in url_list:
            tasks.append(asyncio.ensure_future(fetch(session, url)))

        return await asyncio.gather(*tasks)
    
if __name__ == '__main__':
    start_time = time.time()
    
    pkm_url_list = [f'https://pokeapi.co/api/v2/pokemona/{number}'for number in range(1, 151)]
    response = asyncio.run(asyncStarter(pkm_url_list))

    for pkm in response:
        print(pkm['name'])

    print("--- %s seconds ---" % (time.time() - start_time))
    