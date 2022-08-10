from django.shortcuts import render, redirect, reverse
from .models import Service
from users.models import Doctor
from .decorators import select_language
from django.contrib import messages

@select_language
def doctor_service_page_view(request,id):
    context = {}
    try:
        selected_language = request.GET.get('language')
        doctor = Doctor.objects.select_related('category').get(id=id)
        if selected_language:
            doctor_service = Service.objects.prefetch_related('contents').select_related('language').filter(categories = doctor.category, language__name = selected_language).last()
        else:
            doctor_service = Service.objects.prefetch_related('contents').filter(categories = doctor.category).last()
        if doctor_service:
            service_content = doctor_service.contents.all().order_by('-id')
        else:
            service_content = None

        context = {
            'service': doctor_service,
            'doctor': doctor,
            'contents':service_content,
        }
    
    except Doctor.DoesNotExist:
        # messages.error(request, 'Doctor doesnot exist. Please make sure the the link is proper')
        pass
    except Service.DoesNotExist:
        messages.error(request, 'Doctor does not have any currnt service page.')
    except Exception as e:
        messages.error('Something went wrong')

    return render(request, 'services/Service.html',context=context)
        

def language_selected_page_view(request):
    if request.method == 'POST':
        return redirect(f'{request.GET.get("next")}?language={request.POST.get("language")}')
    return render(request, 'services/select_language_page.html')

def index_page(request):
    return render(request, 'services/index.html')
