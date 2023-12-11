from . import views
from django.urls import path

urlpatterns = [
    path('', views.Index.as_view(), name='get_form-index'),
    path('show/', views.ShowModelGetForm.as_view(), name='get_form-show_model_getform'),
    path('show/<int:pk>', views.ShowOneModelGetForm.as_view(), name='get_one_page'),
    path('update/<int:pk>', views.UpdateModelGetForm.as_view(), name='update_one_page'),
    path('done/', views.done),
    path('no_done/', views.no_done),
]
