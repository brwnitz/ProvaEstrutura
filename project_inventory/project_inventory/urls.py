from django.urls import path
from app_inventory import views

urlpatterns = [
    #Rota, View Responsável, Nome de Referencia
    path('',views.home,name='home'),
    path('products/register',views.register,name='register'),
    path('products/overall',views.overall,name='overall'),
    path('products/update/<int:param>',views.update,name='update')
]
