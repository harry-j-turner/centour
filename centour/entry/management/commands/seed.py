import json
from pathlib import Path
from django.core.management.base import BaseCommand
from entry.models import Entry

class Command(BaseCommand):
    help = 'Seeds the database with initial data for development.'

    def handle(self, *args, **options):

        seed_data_path = Path(__file__).resolve().parent / 'seed_data.json'

        with open(seed_data_path, 'r') as file:
            entries_data = json.load(file)

        for entry_data in entries_data:
            entry, created = Entry.objects.get_or_create(
                title=entry_data['title'],
                defaults=entry_data
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Successfully created entry: {entry.title}'))
            else:
                self.stdout.write(self.style.WARNING(f'Entry already exists: {entry.title}'))
