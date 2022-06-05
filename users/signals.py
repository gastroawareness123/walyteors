from .services import generate_qrcode_for_doctor
from django.core.files import File
from django.db import transaction

def post_save_activities_for_doctor(sender, instance, created, *args, **kwargs):
    if not instance.qr_code:
        print('reached here signals')
        try:
            with transaction.atomic():
                doctor = instance.__class__.objects.select_related('sales_officer', 'sales_officer__region').get(id=instance.id)
                path = generate_qrcode_for_doctor(doctor)
                instance.qr_code = f'media\\{path}'
                instance.save()
        except Exception as e:
            print(str(e))
