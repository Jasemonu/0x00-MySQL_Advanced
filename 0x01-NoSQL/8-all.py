#!/usr/bin/env python3
"""Write a Python function that lists all documents in a collection:"""


import pymongo


def list_all(mongo_collection):
    """Return list of all docs in collection"""
    if not mongo_collection:
        return []
    document_list = []
    for document in mongo_collection.find():
        document_list.append(document)
    return document_list
