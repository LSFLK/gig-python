class Entity:
    def __init__(self):
        self.id = None
        self.title = ""
        self.image_url = ""
        self.source = ""
        self.source_signature = ""
        self.source_date = "2006-01-02T15:04:05-07:00"
        self.attributes = {}
        self.links = []
        self.categories = []
        self.created_at = "2006-01-02T15:04:05-07:00"
        self.updated_at = "2006-01-02T15:04:05-07:00"
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
        self.date = "2006-01-02T15:04:05-07:00"
        self.updated_at = "2006-01-02T15:04:05-07:00"
