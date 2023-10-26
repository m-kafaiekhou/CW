from typing import Union, Optional

from fastapi import FastAPI
from pydantic import BaseModel
from db.db_func import *
from db.mongo import db


collection_book = db['book']


class Book(BaseModel):
    name: str
    description: str
    price: float

    def get_doc(self):
        doc = {
            'name': self.name,
            'description': self.description,
            'price': self.price
        }

        return doc


    def save(self, id: Union[int, None]=None):
        if id:
            update(self.get_doc(), {'_id': id}, collection_book)
            return id
        else:
            return add(self.get_doc(), collection_book)

        
    def get(doc):
        item = get_one(doc, collection_book)
        return item


    @staticmethod
    def filter(doc):
        items = filter(doc, collection_book)
        data = [{item['_id'], item['name'], item['description'], item['price']} for item in items]
        return data


    @staticmethod
    def all():
        items = get_all(collection_book)
        data = [{str(item['_id']), item['name'], item['description'], item['price']} for item in items]

        return data

    @staticmethod
    def delete(id):
        delete({'_id': id}, collection_book)