import factory
from faker import Faker

fake = Faker()

class ProductFactory(factory.Factory):
    class Meta:
        model = dict  # Example model, replace with your actual Product model
    
    name = fake.word()
    price = fake.random_number(digits=2)
    description = fake.text(max_nb_chars=100)
