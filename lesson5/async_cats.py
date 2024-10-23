import time
# import requests
import httpx
import uuid
import asyncio

def time_decor(func):
    def inner(*args, **kwargs):
        time_start = time.time()
        func(*args, **kwargs)
        print(time.time() - time_start)

    return inner


# def get_res(url):
#     return requests.get(url, allow_redirects=True)
#
#
# def write_file(res: requests.Response):
#     file_name = f'{uuid.uuid4()}.jpg'
#     with open(file_name, 'wb') as f:
#         f.write(res.content)
#
#
# @time_decor
# def main():
#     url = 'https://loremflickr.com/320/240/cat'
#     for _ in range(50):
#         write_file(get_res(url))
#
# main()


def write_file(data):
    file_name = f'{uuid.uuid4()}.jpg'
    with open(file_name, 'wb') as f:
        f.write(data)


async def get_res(url, client:httpx.AsyncClient):
    res = await client.get(url, follow_redirects=True)
    write_file(res.read())

async def start():
    url = 'https://loremflickr.com/320/240/cat'
    tasks = []
    async with httpx.AsyncClient() as client:
        for _ in range(50):
            task = asyncio.create_task(get_res(url, client))
            tasks.append(task)

        await asyncio.gather(*tasks)


@time_decor
def main():
    asyncio.run(start())

main()
