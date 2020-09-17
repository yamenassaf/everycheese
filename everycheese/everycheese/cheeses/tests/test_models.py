import pytest
from everycheese.cheeses.models import Cheese

pytestmark = pytest.mark.django_db

def test___str__():
    cheese = Cheese.objects.create(name='Stracchino')
    assert 'Stracchino' == str(cheese)
    assert 'Stracchino' == cheese.__str__()