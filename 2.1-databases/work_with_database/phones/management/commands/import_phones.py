import csv
from django.template.defaultfilters import slugify
from django.core.management.base import BaseCommand
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phone_data = csv.reader(file, delimiter=';')
            next(phone_data)

            for line in phone_data:
                Phone.objects.create(
                    id=int(line[0]),
                    name=line[1],
                    image=line[2],
                    price=round(float(line[3]), 2),
                    release_date=line[4],
                    lte_exists=line[5],
                    slug=slugify(line[1]),
                )
