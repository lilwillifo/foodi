import factory
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User

class UserFactory(factory.django.DjangoModelFactory):
    """
    Creates a standard active user.
    """
    class Meta:
        model = User

    username = factory.Sequence(lambda n: 'username.{}'.format(n))
    email = factory.Sequence(lambda n: 'user.{}@test.test'.format(n))
    password = make_password('pass')
    is_active = True

    @factory.post_generation
    def foods(self, create, extracted, **kwargs):
        """
        Where 'foods' are defined, add them to this user.
        """
        if not create:
            return

        if extracted:
            for food in extracted:
                self.food.add(food)
