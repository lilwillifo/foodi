import factory
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from foodi.models import Diary, Profile

class UserFactory(factory.django.DjangoModelFactory):
    """
    Creates a standard active user.
    """
    class Meta:
        model = User

    username = factory.Sequence(lambda n: 'username.{}'.format(n))
    email = factory.Sequence(lambda n: 'user.{}@test.test'.format(n))
    password = make_password('pass')
    foods = []
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
                Diary.objects.create(food=food, user=self.profile, servings=1, date_eaten='2008-01-01')

class ProfileFactory(factory.django.DjangoModelFactory):
    """
    Creates a standard active profile.
    """
    class Meta:
        model = Profile

    top_5_foods = []

    @factory.post_generation
    def top_5_foods(self, create, extracted, **kwargs):
        """
        Where 'foods' are defined, add them to this user.
        """
        if not create:
            return

        if extracted:
            for food in extracted:
                Diary.objects.create(food=food, user=self, servings=10, date_eaten='2008-01-01')
