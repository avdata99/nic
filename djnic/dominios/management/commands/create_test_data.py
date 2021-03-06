from datetime import timedelta
import logging
import random
from time import sleep
from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone
from dominios.models import Dominio, STATUS_NO_DISPONIBLE, STATUS_DISPONIBLE, DNSDominio
from zonas.models import GrupoZona, Zona, ZonaEnGrupo
from dnss.models import DNS
from registrantes.models import Registrante, TagForRegistrante, RegistranteTag
from cambios.models import CambiosDominio, CampoCambio


logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = 'Crear dominios para pruebas locales'

    # def add_arguments(self, parser):
    #     parser.add_argument('--sleep', nargs='?', type=int, default=41)

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS(f"Creating groups"))
        
        grupo_ar, created = GrupoZona.objects.get_or_create(nombre='Argentina', published=True)
        grupo_uy, created = GrupoZona.objects.get_or_create(nombre='Uruguay', published=True)
        grupo_cl, created = GrupoZona.objects.get_or_create(nombre='Chile', published=True)

        zona_ar,created = Zona.objects.get_or_create(nombre='ar')
        ZonaEnGrupo.objects.get_or_create(zona=zona_ar, grupo=grupo_ar, published=True)

        zona_gob_ar,created = Zona.objects.get_or_create(nombre='gob.ar')
        ZonaEnGrupo.objects.get_or_create(zona=zona_gob_ar, grupo=grupo_ar, published=True)

        zona_cl, created = Zona.objects.get_or_create(nombre='cl')
        ZonaEnGrupo.objects.get_or_create(zona=zona_cl, grupo=grupo_cl, published=True)

        zona_uy, created = Zona.objects.get_or_create(nombre='uy')
        ZonaEnGrupo.objects.get_or_create(zona=zona_uy, grupo=grupo_uy, published=True)

        zona_com_uy, created = Zona.objects.get_or_create(nombre='com.uy')
        ZonaEnGrupo.objects.get_or_create(zona=zona_com_uy, grupo=grupo_uy, published=True)

        zonas = [zona_ar, zona_cl, zona_com_uy, zona_gob_ar, zona_uy]

        for r in range(1, 50):
            for n in range(1, 4):
                DNS.objects.get_or_create(dominio=f'ns{n}.test{r}.com')

        for r in range(1, 7):
            TagForRegistrante.objects.get_or_create(nombre=f'RegTag{r}')
        
        for r in range(1, 70):
            reg, created = Registrante.objects.get_or_create(legal_uid=f'R00000{r}', name=f'Registrante {r}')
            for n in range(1, 3):
                if random.randint(1, 90) > 70:
                    tag = TagForRegistrante.objects.order_by('?').first()
                    RegistranteTag.objects.create(registrante=reg, tag=tag)
            
        hoy = timezone.now()
        for n in range(0, 500):
            for zona in zonas:
                
                dom, created = Dominio.objects.get_or_create(nombre=f'test-{n}.{zona.nombre}',zona=zona)
                # clean DNSs
                DNSDominio.objects.filter(dominio=dom).delete()
                dom.data_readed = hoy - timedelta(days=random.randint(1, 90))
                dom.data_updated = hoy - timedelta(days=random.randint(1, 60))
                

                if random.randint(1, 90) > 30:
                    dom.estado = STATUS_NO_DISPONIBLE
                    dom.registrante = Registrante.objects.order_by('?').first()
                    dom.registered = hoy - timedelta(days=random.randint(1, 900))
                    dom.expire = hoy + timedelta(days=random.randint(1, 90))
                    for n in range(1, random.randint(3, 6)):
                        dns = DNS.objects.order_by('?').first()
                        DNSDominio.objects.create(dominio=dom, dns=dns, orden=n)
                else:
                    dom.estado=STATUS_DISPONIBLE
                dom.save()

                # agregar registros de camibos
                starts = timezone.now() - timedelta(minutes=random.randint(1440000, 2880000))
                while starts < timezone.now():
                    cd = CambiosDominio.objects.create(dominio=dom, momento=starts, have_changes=False)
                    starts = starts + timedelta(minutes=random.randint(344000, 644000))
                    if random.randint(1, 90) > 40:
                        cd.have_changes = True
                        cd.save()
                        rlu = str(random.randint(10000, 90000))
                        rnm = f'reg {rlu}'
                        dns1 = f'ns{random.randint(1, 9)}.lala.com'
                        if random.randint(1, 90) > 40:
                            CampoCambio.objects.create(cambio=cd, campo='estado', anterior=STATUS_DISPONIBLE, nuevo=STATUS_NO_DISPONIBLE)
                            CampoCambio.objects.create(cambio=cd, campo='registrant_legal_uid', anterior='', nuevo=rlu)
                            CampoCambio.objects.create(cambio=cd, campo='DNS1', anterior='', nuevo=dns1)
                            CampoCambio.objects.create(cambio=cd, campo='registrant_name', anterior='', nuevo=rnm)
                        else:
                            CampoCambio.objects.create(cambio=cd, campo='estado', nuevo=STATUS_DISPONIBLE, anterior=STATUS_NO_DISPONIBLE)
                            CampoCambio.objects.create(cambio=cd, campo='registrant_legal_uid', nuevo='', anterior=rlu)
                            CampoCambio.objects.create(cambio=cd, campo='DNS1', nuevo='', anterior=dns1)
                            CampoCambio.objects.create(cambio=cd, campo='registrant_name', nuevo='', anterior=rnm)                                    

        self.stdout.write(self.style.SUCCESS(f"Finished"))
        