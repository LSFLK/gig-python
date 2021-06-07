from gig import gig

server = gig("http://localhost:9000/")


def test_get():
    entity = server.get("Sri Lanka")
    assert entity.title == "Sri Lanka"


def test_normalize_name():
    results = server.normalize_name("sri lanka")
    assert "Sri Lanka" in results


def test_normalize_location():
    results = server.normalize_name("colombo")
    assert "Colombo" in results


def test_get_links():
    entities = server.get_links("Sri Lanka")
    assert len(entities) > 0


def test_get_relations():
    entities = server.get_links("Sri Lanka")
    assert len(entities) > 0


def test_search():
    entities = server.search("Sri Lanka", attributes_list=["title"])
    assert len(entities) > 0


test_normalize_location()
test_normalize_name()
