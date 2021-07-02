from django.core import management
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        management.call_command('loaddata', 'directors', verbosity=0)
        management.call_command('loaddata', 'producers', verbosity=0)
        management.call_command('loaddata', 'planets', verbosity=0)
        management.call_command('loaddata', 'people', verbosity=0)
        management.call_command('loaddata', 'films', verbosity=0)
        self.stdout.write(self.style.SUCCESS('The fixtures were loaded successfully.'))
