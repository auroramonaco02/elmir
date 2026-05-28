from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('vacancies', views.vacancies, name='vacancies'),
    path('vacancies/<int:pk>', views.vacancy_detail, name='vacancy_detail'),
    path('ausbildung', views.ausbildung, name='ausbildung'),
    path('ferienJob', views.ferienjob, name='ferienjob'),
    path('contact', views.contact, name='contact'),
]
