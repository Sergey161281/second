from django.urls import path
from .views import *

urlpatterns = [
   # path('', index, name='home'),
    path('send_message/', send_message, name='send_message'),
    path('', HomeEmemergy.as_view(), name='home'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    # path('cat/<int:category_id>/', get_category, name='category'),
    path('cat/<int:category_id>/', EmemergyByCategory.as_view(), name='category'),

    #path('ememergy/<int:ememergy_id>/', view_ememergy, name='view_ememergy'),
    #path('ememergy/<int:ememergy_id>/', ViewEmemergy.as_view(), name='view_ememergy'),
    path('ememergy/<int:pk>', ViewEmemergy.as_view(), name='view_ememergy'),

    #path('ememergy/add_droch/', add_droch, name='add_droch'),
    path('ememergy/add_droch/', CreateDroch.as_view(), name='add_droch'),
]