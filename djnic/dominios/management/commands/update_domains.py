from datetime import datetime, timedelta
import logging
from time import sleep
from django.core.management.base import BaseCommand, CommandError
from django.db.models import Q
from django.utils import timezone
from dominios.models import Dominio
from whoare.exceptions import TooManyQueriesError


logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = 'Actualziar datos de dominios'

    def add_arguments(self, parser):
        parser.add_argument('--limit', nargs='?', type=int, default=10)
        parser.add_argument('--sleep', nargs='?', type=int, default=10)


    def handle(self, *args, **options):
        limit = options['limit']
        dominios = Dominio.objects.all().order_by('-priority_to_update')[:limit]
        print(dominios)
        c = 0
        for dominio in dominios:
            c += 1
            self.stdout.write(self.style.SUCCESS(f"{c} {dominio} expire:{dominio.expire} \n\tpts:{dominio.priority_to_update} \n\tnext:{dominio.next_update_priority}"))
            try:
                Dominio.add_from_whois(domain=dominio.full_domain())
            except TooManyQueriesError:
                self.stdout.write(self.style.SUCCESS(f"WHOIS TooManyQueriesError"))
                sleep(15)
            
            sleep(options['sleep'])

            self.stdout.write(self.style.SUCCESS(f" - {dominio.priority_to_update} {dominio.next_update_priority}"))

        self.stdout.write(self.style.SUCCESS(f"{c} processed"))
        