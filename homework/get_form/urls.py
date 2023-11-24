from . import views
from django.urls import path

urlpatterns = [
    # path('', views.index, name='get_form-index'),
    path('', views.Index.as_view(), name='get_form-index'),
    path('done/', views.done),
    path('no_done/', views.no_done),
]
