from django.urls import reverse, resolve
# from pypro.django_assertions import assert_contains
import pytest
from model_bakery import baker
from django.test import TestCase

from superlists.lists.views import home_page

_test_case = TestCase()

assert_contains = _test_case.assertContains

@pytest.fixture
def resp(client, db):
    resp = client.get(reverse('list:home'))
    return resp


class HomePageTest(TestCase):
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)


def test_status_code(resp):
    assert resp.status_code == 200
