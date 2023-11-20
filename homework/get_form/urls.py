from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='get_form-index'),
    path('done/', views.done),
]
