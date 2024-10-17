import factory
from models import Account  # Assuming Account is defined in your models.py
from factory.fuzzy import FuzzyChoice

class AccountFactory(factory.Factory):
    """Creates fake accounts"""

    class Meta:
        model = Account

    id = factory.Sequence(lambda n: n)
    name = factory.Faker('name')
    email = factory.Faker('email')
    number = factory.Faker('random_number')  # Corrected to a valid Faker provider
    disabled = FuzzyChoice(choices=[True, False])


