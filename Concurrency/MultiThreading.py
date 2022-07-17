# Good for IO Bound Tasks
# pip install ping3
import time
import concurrent.futures
import pandas as pd
from ping3 import ping

def ping_host(host):
    resp = ping(host)

    if resp == False or resp == None :
        return {"host":host,"ping_status":False}
    else:
        return {"host":host, "ping_status":True}

if __name__ == "__main__":
    # Read in list of hosts to ping
    df = pd.read_excel('top_sites.xlsx')
    top_sites = df.iloc[:,1].values.tolist()

    start = time.perf_counter()

    # Without MultiThreading
    # for site in top_sites:
    #     print(f'site {site} ping status is: {ping_host(site)}')

    # With MultiThreading w List Comprehension 
    # with concurrent.futures.ThreadPoolExecutor() as executor:
    #     results = [executor.submit(ping_host, site) for site in top_sites]

    #     for f in concurrent.futures.as_completed(results):
    #         print(f.result())

    # With MultiTreading w map function
    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = executor.map(ping_host, top_sites)

        # for result in results:
        #     print(f'{result["host"]} : {result["ping_status"]}')

        # print(list(results))

    finish = time.perf_counter()

    print(f'Finished in {finish - start} seconds')