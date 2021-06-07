import requests, json
from types import SimpleNamespace


class Server:
    def __init__(self, server_url, timeout=30):
        self.server_url = server_url
        self.time_out = timeout
        test_connection = requests.get(server_url).status_code
        if test_connection == 200:
            print("remote server reached")
        else:
            raise Exception("Error: unable to reach server")

    def add(self, entity):
        return 0

    def add_all(self, entities):
        return 0

    def terminate(self, title="", category=[]):
        return 0

    def get(self, title, date=None, attributes_list=None, image_only=False):
        response = requests.get(self.server_url + f'api/get/{title}',
                                params={"date": date, "attributes": attributes_list, "imageOnly": image_only},
                                timeout=self.time_out)

        if response.status_code != 200:
            raise Exception('No entity found')
        return json.loads(response.content, object_hook=lambda d: SimpleNamespace(**d))

    def get_links(self, title, attributes_list=None, page=None, limit=10):
        response = requests.get(self.server_url + f'api/links/{title}',
                                params={"page": page, "attributes": attributes_list, "limit": limit},
                                timeout=self.time_out)
        if response.status_code != 200:
            raise Exception('No entity found')
        result = json.loads(response.content, object_hook=lambda d: SimpleNamespace(**d))
        if result is None:
            raise Exception('No links found')
        return result

    def get_relations(self, title, attributes_list=[], page=1, limit=10):
        response = requests.get(self.server_url + f'api/links/{title}',
                                params={"page": page, "attributes": ','.join(attributes_list), "limit": limit},
                                timeout=self.time_out)
        if response.status_code != 200:
            raise Exception('No entity found')
        result = json.loads(response.content, object_hook=lambda d: SimpleNamespace(**d))
        if result is None:
            raise Exception('No related entities found')
        return result

    def search(self, search_text, attributes_list=[], category_list=[], page=1, limit=10):
        response = requests.get(self.server_url + f'api/search',
                                params={"query": search_text, "page": page, "attributes": ','.join(attributes_list),
                                        "categories": ','.join(category_list), "limit": limit},
                                timeout=self.time_out)
        if response.status_code != 200:
            raise Exception('No entity found')
        result = json.loads(response.content, object_hook=lambda d: SimpleNamespace(**d))
        if result is None:
            raise Exception('No related entities found')
        return result

    def normalize_name(self, search_text):
        response = requests.get(self.server_url + f'api/normalize/name',
                                params={"searchText": search_text}, timeout=self.time_out)
        if response.status_code != 200:
            raise Exception('No result found')
        return json.loads(response.content)

    def normalize_location(self, search_text):
        response = requests.get(self.server_url + f'api/normalize/location',
                                params={"searchText": search_text}, timeout=self.time_out)
        if response.status_code != 200:
            raise Exception('No result found')
        return json.loads(response.content)
