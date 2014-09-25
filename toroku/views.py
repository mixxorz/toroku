import os

from django.shortcuts import render
from django.conf import settings


def home(request):
    hostname = 'None found'

    try:
        hostname_path = os.path.abspath(
            os.path.join(
                settings.BASE_DIR,
                os.path.pardir,
                'tor',
                'hidden_service',
                'hostname'
            )
        )
        f = open(hostname_path, 'r')
        hostname = f.read()
        f.close()
    except Exception:
        pass

    onion_url = hostname.strip()

    return render(request, 'home.html', {'onion_url': onion_url})
