#!/usr/bin/env python3
"""Write a Python function that lists all documents in a collection:"""


import pymongo


def list_all(mongo_collection):
    # Initialize an empty list to store the documents
    if not mongo_collection:
        return []
    # Iterate through the documents in the collection
    document_list = []
    for document in mongo_collection.find():
        document_list.append(document)
    
    # Return the list of documents
    return document_list
