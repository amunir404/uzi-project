import factory
from django.contrib.auth.models import User
from faker import Faker

fake = Faker()
class UserFactory(factory.Factory):
    class Meta:
        model = User

    first_name = 'John'
    last_name = 'Doe'
    username = 'amunirrr'
    email = 'jDZfM@example.com'