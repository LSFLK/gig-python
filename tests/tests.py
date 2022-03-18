from src.gig.gig import Server as GIG_Server
from src.gig.models import Entity

server = GIG_Server("http://localhost:9000/")
SRI_LANKA = "Sri Lanka"


def test_get():
    entity = server.get(SRI_LANKA)
    assert entity.title == SRI_LANKA


def test_normalize_name():
    results = server.normalize_name("sri lanka")
    assert SRI_LANKA in results


def test_normalize_location():
    results = server.normalize_location("colombo")
    assert "Colombo" in results


def test_get_links():
    entities = server.get_links(SRI_LANKA)
    assert len(entities) > 0


def test_get_relations():
    entities = server.get_relations(SRI_LANKA)
    assert len(entities) > 0


def test_search():
    entities = server.search(SRI_LANKA, attributes_list=["title"])
    assert len(entities) > 0


def test_add():
    entity = Entity()
    entity.title = "LDF Test Entity"
    result = server.add(entity)
    assert result in [200, 202]


def test_terminate():
    entity = Entity()
    entity.title = "LDF Test Entity"
    entity.source_date = "2021-01-02T15:04:05-07:00"
    entity.source = "python-lib"
    result = server.terminate(entity)
    assert result in [200, 202]


def test_add_all():
    entity = Entity()
    entity.title = "LDF Batch"
    result = server.add_all([entity])
    assert result in [200, 202]
