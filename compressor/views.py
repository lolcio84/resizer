from django.shortcuts import render
from .models import Visit

def get_client_ip(request):
    # Próbuje wyciągnąć IP, jeśli serwer jest za proxy (częste na hostingu)
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def index(request):
    # Pobierz IP i zapisz wizytę
    ip = get_client_ip(request)
    Visit.objects.create(ip_address=ip)
    
    return render(request, 'compressor/index.html')

