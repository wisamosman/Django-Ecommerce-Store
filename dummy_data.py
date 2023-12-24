import os , django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()


from faker import Faker
import random
from products.models import Product,Brand


def seed_brand(n):
    fake = Faker()
    images = ['2.jpg','3.jpg','4.jpg','5.jpg','6.jpg','7.jpg','8.jpeg','9.jpg','10.jpg','11.png','12.png','13.jpeg','14.jpeg']

    for x in range(n):
        Brand.objects.create(
            name = fake.name() , 
            image = f'brand/{images[random.randint(0,12)]}'
        )
    print(f'{n} Brands Was Created Successfuly ...')


def seed_product(n):
    fake = Faker()
    images = ['2.jpg','3.jpg','4.jpg','5.jpg','6.jpg','7.jpg','8.jpeg','9.jpg','10.jpg','11.png','12.png','13.jpeg','14.jpeg']
    flag_types = ['New','Sale','Feature']

    for x in range(n):
        Product.objects.create(
            name = fake.name() ,
            description=fake.text(max_nb_chars=30000) , 
            sku = random.randint(100,10000000) , 
            price = round(random.uniform(20.99,99.99),2) , 
            subtitle=fake.text(max_nb_chars=600) , 
            image = f'brand/{images[random.randint(0,12)]}',
            brand  = Brand.objects.get(id=random.randint(1,18)),
            flag = flag_types[random.randint(0,2)],
        )
    print(f'{n} Product Was Created Successfuly ...')



seed_brand(100)
seed_product(3000)