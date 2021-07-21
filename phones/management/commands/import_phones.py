import csv
from django.core.management.base import BaseCommand
from phones.models import Phone
from django.utils.text import slugify


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))
        lst = []
        for phone in phones:
            lst.append(phone)

        for i in lst:
            p = Phone(id=i['id'], name=i['name'], price=i['price'], image=i['image'],
                      release_date=i['release_date'], lte_exists=i['lte_exists'],
                      slug=slugify(i["name"]))
            p.save()

