from behave import *
class DiaryTest(TestCase):
    """Test suite for the user diary."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.client = APIClient()
        self.apple = Food.objects.create(name="apple", calories=50)
        self.oatmeal = Food.objects.create(name="oatmeal", calories=400)
        self.user = UserFactory()

    def test_user_can_add_food_to_diary(self):
        """Test the user can add food to their diary."""
        # import code; code.interact(local=dict(globals(), **locals()))
