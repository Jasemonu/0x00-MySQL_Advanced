#!/usr/bin/env python3
"""Write a Python function that lists all documents in a collection:"""

import pymongo


def list_all(mongo_collection):
    if mongo_collection is None:
        return []
    document_list = []
    documents = mongo_collection.find()
    for document in documents:
        document_list.append(document)
    return document_list
