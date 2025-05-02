from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    tenant = request.tenant
    context = {
        'tenant_name': tenant.name,
        'tenant_logo': tenant.logo_url if hasattr(tenant, 'logo_url') else '',
        'products': [
            {'name': 'Producto 1', 'price': '10.000', 'color': 'pastel-blue'},
            {'name': 'Producto 2', 'price': '12.000', 'color': 'pastel-pink'},
            {'name': 'Producto 3', 'price': '9.500', 'color': 'pastel-green'},
        ]
    }
    return render(request,'index.html',context=context)
