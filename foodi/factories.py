import factory
from .models import Food

class FoodFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Food

    name = factory.Sequence(lambda n: 'food{}'.format(n))
