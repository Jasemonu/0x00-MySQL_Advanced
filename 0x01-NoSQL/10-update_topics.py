#!/usr/bin/env python3
"""Write a Python function that changes all topics of a
school document based on the name:
"""


import pymongo


def update_topics(mongo_collection, name, topics):
    """ Update documents where the "name" field matches the provided name """
    result = mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
    return result.modified_count
