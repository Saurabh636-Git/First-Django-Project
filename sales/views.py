from sales.utils import get_bar_chart, get_line_chart, get_pie_chart, img_trns
from django import forms
from django.shortcuts import redirect, render, get_object_or_404
from .forms import *
from .models import *
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from xhtml2pdf import pisa

# Create your views here.

class UserLogin(LoginView):
    template_name = 'sales/login.html'
    fields = '__all__'
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy('index')

def register_user(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        print('got it here')
        if form.is_valid():
            form.save()
            print('saved')
    context = {
        'form': form
    }

    return render(request, 'sales/register.html', context)

@login_required(login_url='login')
def index(request):
    items = Item.objects.all()
    
    
    context = {
        'items': items,
    }
    return render(request, 'sales/index.html', context)

@login_required(login_url='login')
def create_sales(request):
    
    if request.method == 'POST':
        print('@@@', request.POST)
        forms = SalesForm(request.POST)
        forms.save()
        return redirect('index')
    else:
        forms = SalesForm()
    # print(SalesForm())
    # print('#')
    # print(forms)
    context = {
        'forms': forms,
    }

    return render(request, 'sales/create_sales.html', context)

@login_required(login_url='login')
def create_item(request):
    
    if request.method == 'POST':
        forms = ItemForm(request.POST)
        if forms.is_valid():
            print(request.POST)
            forms.save()
            return redirect('index')
    else:
        forms = ItemForm()
    context = {
        'forms': forms,
    }

    return render(request, 'sales/create_item.html', context)

@login_required(login_url='login')
def details(request, item_id):
    item = Item.objects.get(pk=item_id)
    list = Sale.objects.filter(items=item)
    
    context = {
        'list': list,
    }

    return render(request, 'sales/details.html', context)

@login_required(login_url='login')
def show_charts(request, item_id):
    item = Item.objects.get(pk=item_id)
    list = Sale.objects.filter(items=item)
    
    x = [x.date.strftime('%d %B %Y') for x in list]
    y = [y.total for y in list]
    x.sort()
    
    line_chart = get_line_chart(x, y)
    bar_chart = get_bar_chart(x,y)
    pie_chart = get_pie_chart(x,y)
    
    context = {
        'x': x,
        'line_chart': line_chart,
        'bar_chart': bar_chart,
        'pie_chart': pie_chart,
        'item': item,
    }

    return render(request, 'sales/charts.html', context)

@login_required(login_url='login')
def render_pdf_view(request, item_id):
    template_path = 'sales/pdf.html'
    obj = get_object_or_404(Item, pk=item_id)
    list = Sale.objects.filter(items=obj)
    charts = img_trns(list)
    line_chart = charts[0]
    bar_chart = charts[1]
    pie_chart = charts[2]
    context = {
        'obj': obj,
        'line_chart': line_chart,
        'bar_chart': bar_chart,
        'pie_chart': pie_chart,

    }
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    # if download:
    # response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # if display:
    response['Content-Disposition'] = 'filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response