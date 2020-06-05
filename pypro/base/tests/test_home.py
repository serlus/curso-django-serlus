from pypro.django_assertions import assert_contains
from django.test import Client


def test_status_code(client: Client):
    resp = client. get('/')
    assert resp.status_code == 200

def test_title(client: Client):
    resp = client. get('/')
    assert_contains(resp, '<title>Web Design</title>')
