from django.urls import path

from . import views

urlpatterns = {
    path('', views.home, name='home'),
    path('process/', views.process, name='process'),
    path('process-ele-type/<str:param>', views.process_ele_type, name='process-ele-type'),
}
