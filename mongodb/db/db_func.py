

async def add(doc, collection):
    return str(await collection.insert_one(doc).inserted_id)


async def update(updated_val, based_on, collection):
    return str(await collection.update_one(based_on, {"$set": updated_val}))


async def delete(based_on, collection):
    return await collection.delete_one(based_on)


async def get_one(doc, collection):
    return await collection.find_one(doc)


async def filter(doc, collection):
    return await collection.find(doc)


async def get_all(collection):
    return await collection.find()