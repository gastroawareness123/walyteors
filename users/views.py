from django.shortcuts import render
from django.http import JsonResponse
from .services import store_doctor_hits
from .models import Doctor
from django.views.decorators.csrf import csrf_exempt

import json

@csrf_exempt
def doctor_hits_api(request):
    try:
        
        requestData = json.loads(request.body)

        doctor_id = requestData.get('doctor_id')
        if not doctor_id:
            return JsonResponse({'status':'failure','message':'Doctor Id is missing'}, status=400)
        
        doctor = Doctor.objects.get(id=int(doctor_id))

        requestData.pop('doctor_id')

        store_doctor_hits(doctor, requestData)

        return JsonResponse({'status':'success','message':'Doctor his registered'}, status=201)

    except Doctor.DoesNotExist:
        return JsonResponse({'status':'failure','message':'Doctor not found'}, status=404)

    except Exception as e:
        return JsonResponse({'status':'failure','message':str(e)}, status=500)
