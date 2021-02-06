from django.shortcuts import render, get_object_or_404
from .models import Form
from django.contrib import messages

# Create your views here.
def home(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        designation = request.POST.get('designation')
        industry = request.POST.get('industry')
        website = request.POST.get('website')
        description = request.POST.get('description')

        form = Form(first_name=first_name, last_name=last_name, designation=designation, industry=industry, website=website, description=description)        
        form.save()
        messages.success(request, 'Successful')
        forms = Form.objects.order_by('-created_date');
        data = {
            'forms': forms,
        }
        return render(request, 'pages/home.html', data)
    if request.method == 'GET':
        forms = Form.objects.order_by('-created_date');
        data = {
            'forms': forms,
        }        
        return render(request, 'pages/home.html', data)

def delete(request, id):
    form = get_object_or_404(Form, pk=id)
    form.delete()

    forms = Form.objects.order_by('-created_date');
    data = {
        'forms': forms,
    }        
    return render(request, 'pages/home.html', data)

def edit(request, id):
    form = get_object_or_404(Form, pk=id)
    temp = form
    form.delete()    

    forms = Form.objects.order_by('-created_date');
    data = {
        'forms': forms,
        'form_detail': temp
    }    
    return render(request, 'pages/home.html', data)