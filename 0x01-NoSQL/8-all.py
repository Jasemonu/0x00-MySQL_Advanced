#!/usr/bin/env python3
"""Write a Python function that lists all documents in a collection:"""


import pymongo


def list_all(mongo_collection):
    # Initialize an empty list to store the documents
    if mongo_collection is not None:
        document_list = []
        # Iterate through the documents in the collection
        for document in mongo_collection.find():
            document_list.append(document)
        # Return the list of documents
        return document_list
    else:
        # Return an empty list if the collection is None
        return []
