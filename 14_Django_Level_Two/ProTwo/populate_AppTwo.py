import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ProTwo.settings")

import django
django.setup()

# Fake pop script
from AppTwo.models import User
from faker import Faker

fakegen = Faker()

def populate(N=5):

    for entry in range(N):

        fake_f_name = fakegen.first_name()
        fake_l_name = fakegen.last_name()
        fake_email = fakegen.email()

        user = User.objects.get_or_create(first_name=fake_f_name,
                                          last_name=fake_l_name,
                                          email=fake_email)

if __name__ == '__main__':
    print("Start populating...")
    populate(20)
    print("Populated!")