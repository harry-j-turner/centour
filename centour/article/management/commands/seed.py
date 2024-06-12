import json
import pathlib

from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

from article.models import Article

User = get_user_model()


class Command(BaseCommand):

    help = "Seed the database with initial data."
    seed_data = pathlib.Path(__file__).parent / "seed_data.json"
    user = None

    def handle(self, *args, **options):

        self.create_users()
        self.create_seed_articles()

    def create_users(self):

        self.stdout.write(self.style.HTTP_INFO("Creating seed users."))

        self.user, _ = User.objects.get_or_create(
            username="admin",
            email="henry.j.turner@gmail.com",
            password="admin",
            is_staff=True,
            is_superuser=True,
        )

        self.user.set_password("admin")
        self.user.save()

        self.stdout.write(self.style.SUCCESS("Done."))

    def create_seed_articles(self):

        self.stdout.write(self.style.HTTP_INFO("Creating seed articles."))

        with open(self.seed_data, "r") as seed_data:
            articles = json.load(seed_data)
            for article in articles:
                Article.objects.get_or_create(
                    title=article["title"],
                    content=article["content"],
                    geohash=article["geohash"],
                    owner=self.user,
                )

        self.stdout.write(self.style.SUCCESS("Done."))
