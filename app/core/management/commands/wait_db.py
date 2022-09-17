'''
Wait for Database
'''
from django.core.management.base import BaseCommand
import time
from psycopg2 import OperationalError as Psycopg2Error
from django.db.utils import OperationalError


class Command(BaseCommand):
    def handle(self, *args, **options):
        db = False
        while not db:
            try:
                self.check(databases=['default'])
                db = True
            except (Psycopg2Error, OperationalError):
                self.stdout.write("Database unavailable")
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS("Database available"))
