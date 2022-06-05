from DoctorServiceBackend.settings import *
from DoctorServiceBackend.wsgi import *
from DoctorServiceBackend.asgi import *

from users.models import *
from services.models import *

Doctor.objects.all().delete()
DoctorCategory.objects.all().delete()
SalesOfficer.objects.all().delete()
SalesOfficerRegion.objects.all().delete()

Service.objects.all().delete()
Content.objects.all().delete()
ServiceLanguage.objects.all().delete()