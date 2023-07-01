
async def __load__(info):
    print('loaded', __name__, info)


async def __drop__(info):
    print('dropped', __name__, info)