import qrcode
from django.conf import settings
import os

LINK_TEMPLATE_FOR_QRCODE = 'http://127.0.0.1:8000/{}'

def generate_qrcode_for_doctor(doctor):
    print('reached here services')
    qr_code = qrcode.make(LINK_TEMPLATE_FOR_QRCODE.format(doctor.id))
    image_dest = f'qr_codes/{doctor.id}_{doctor.name}_{doctor.sales_officer.region}.jpg'
    storage_path = os.path.join(settings.MEDIA_ROOT_URL, image_dest)
    qr_code.save(storage_path)
    print(storage_path)
    return image_dest

def store_doctor_hits(doctor, data):
    from .models import DoctorHits
    city = data.get('city')
    village = data.get('village')
    state = data.get('state')
    latitude = data.get('latitude')
    longitude = data.get('longitude')

    search_params = {
        'doctor':doctor
    }

    if not city and village:
        village_or_city = village
    else:
        village_or_city = city
    search_params['village_or_city'] = village_or_city.upper()

    if state:
        search_params['state'] = state.upper()

    print(search_params)

    already_registered_hit = DoctorHits.objects.filter(**search_params).order_by('id')
    print(already_registered_hit)
    if already_registered_hit:
        already_registered_hit = already_registered_hit.last()
        already_registered_hit.hit_count += 1
        already_registered_hit.save()
    else:
        DoctorHits.objects.create(doctor=doctor, village_or_city=village_or_city.upper(), state=state.upper(), longitude=longitude,latitude=latitude)

    