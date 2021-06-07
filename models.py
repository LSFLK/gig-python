from datetime import datetime


class Entity:
    def __init__(self):
        self.id = None
        self.title = ""
        self.image_url = ""
        self.source = ""
        self.source_signature = ""
        self.source_date = datetime.now()
        self.attributes = {}
        self.links = []
        self.categories = []
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.snippet = ""
        self.search_text = ""


class Attribute:
    def __init__(self):
        self.name = ""
        self.values = []


class Link:
    def __init__(self):
        self.title = ""
        self.dates = []


class Value:
    def __init__(self):
        self.value_type = ""
        self.value_string = ""
        self.source = ""
        self.date = datetime.now()
        self.updated_at = datetime.now()
