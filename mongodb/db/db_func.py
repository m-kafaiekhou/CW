

def add(doc, collection):
    return str(collection.insert_one(doc).inserted_id)


def update(updated_val, based_on, collection):
    return str(collection.update_one(based_on, {"$set": updated_val}))


def delete(based_on, collection):
    return collection.delete_one(based_on)


def get_one(doc, collection):
    return collection.find_one(doc)


def filter(doc, collection):
    return collection.find(doc)


def get_all(collection):
    return collection.find()