from faker import Faker

fake = Faker()

def fake_product():
    """Generate a fake product with random data"""
    return{
        'name':fake.word(),
        'category':fake.word(),
        'price':round(fake.random_number(digits=2),2),
        'availabilty':fake.boolean(),
    }