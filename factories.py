import factory
from models import Product  # Import the Product class from models.py

class ProductFactory(factory.Factory):
    class Meta:
        model = Product

    name = factory.Faker('name')
    description = factory.Faker('text')
    price = factory.Faker('random_number', digits=5)
    available = factory.Faker('boolean')
    category = factory.Faker('word')
