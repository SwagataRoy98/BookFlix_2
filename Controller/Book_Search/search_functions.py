import json
import requests
from time import sleep


def search(title, author=None):
    query_dictionary = {}
    url = "https://openlibrary.org/search.json?" + 'q=' + title
    if author:
        url = url + '&author=' + author
    resp = requests.get(url)
    obj = resp.json()
    obj_docs = obj["docs"]
    key_obj = obj_docs[0]
    query_dictionary['edition'] = []
    edition_list = key_obj["edition_key"][:10]
    for edition in edition_list:
        query_dictionary["edition"].append(search_by_edition(edition))
        sleep(1)
    return query_dictionary


def search_by_edition(key):
    data_dictionary = {}
    url = "https://openlibrary.org"
    print(key)
    resp = requests.get(url + '/works/' + key + '.json')
    obj = resp.json()
    data_dictionary["title"] = obj["title"]
    try:
        data_dictionary["description"] = obj["description"]
    except:
        data_dictionary["description"] = "Data not available"
    try:
        author_url = obj["authors"][0]["author"]["key"]
        author_resp = requests.get(url + author_url + '.json').json()
        data_dictionary["author"] = author_resp["name"]
        print(author_resp["name"])
    except:
        data_dictionary["author"] = "Author Name not available"

    data_dictionary["cover_url"] = "https://covers.openlibrary.org/b/olid/" + key + "-M.jpg"
    return data_dictionary
