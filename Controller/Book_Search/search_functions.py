import json
import requests


def search(title, author=None):
    query_dictionary = {}
    url = "https://openlibrary.org/search.json?" + 'q='+title
    if author:
        url = url + '&author=' + author
    resp = requests.get(url)
    obj = resp.json()
    obj_docs = obj["docs"]
    key_obj = obj_docs[0]
    ol_id = key_obj["key"]
    query_dictionary["ol_id"] = ol_id

    query_dictionary["author_name"] = key_obj["author_name"]
    query_dictionary["edition_key"] = key_obj["edition_key"]
    for k,v in enumerate(query_dictionary["edition_key"]):
        if k > 4:
            break

    return query_dictionary

# def search_by_key(key):
#     data_dictionary = {}
#     url = "https://openlibrary.org/works"
#     resp = request.get(url+key)
#     obj = resp.json()
#     data_dictionary["title"] = obj["title"]
