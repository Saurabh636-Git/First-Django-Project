from django.urls import path
from django.utils.regex_helper import next_char
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.UserLogin.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('create_sales/', views.create_sales, name='create'),
    path('create_item/', views.create_item, name='create_item'),
    path('details/<item_id>/', views.details, name='details'),
    path('charts/<item_id>/', views.show_charts, name='show_charts'),
    path('<item_id>/pdf/', views.render_pdf_view, name='pdf')
]
