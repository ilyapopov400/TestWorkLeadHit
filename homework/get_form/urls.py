from . import views
from django.urls import path

urlpatterns = [
    path('', views.Index.as_view(), name='get_form-index'),
    path('show/', views.ShowModelGetForm.as_view(), name='get_form-show_model_getform'),
    path('done/', views.done),
    path('no_done/', views.no_done),
]
