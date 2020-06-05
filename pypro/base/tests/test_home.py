from pypro.django_assertions import assert_contains
from django.urls import reverse
import pytest


@pytest.fixture
def resp(client):
    resp = client. get(reverse('home'))
    return resp


def test_status_code(resp):
    assert resp.status_code == 200


def test_title(resp):
    assert_contains(resp, '<title>Web Design</title>')


def test_home_link(resp):
    assert_contains(resp, f'href="{reverse("home")}">Gab Casas</a>')
