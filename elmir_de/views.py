from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Vacancy, City, AusbildungProgram, ContactMessage


def index(request):
    cities = City.objects.filter(is_active=True)
    latest_vacancies = Vacancy.objects.filter(is_active=True).select_related('city')[:6]
    context = {
        'cities': cities,
        'latest_vacancies': latest_vacancies,
    }
    return render(request, 'index.html', context)


def vacancies(request):
    cities = City.objects.filter(is_active=True)
    all_vacancies = Vacancy.objects.filter(is_active=True).select_related('city')
    context = {
        'vacancies': all_vacancies,
        'cities': cities,
    }
    return render(request, 'vacancies.html', context)


def vacancy_detail(request, pk):
    vacancy = get_object_or_404(Vacancy, pk=pk, is_active=True)
    related = Vacancy.objects.filter(type=vacancy.type, is_active=True).exclude(pk=pk)[:3]
    context = {
        'vacancy': vacancy,
        'related': related,
    }
    return render(request, 'vacancy_detail.html', context)


def ausbildung(request):
    programs = AusbildungProgram.objects.filter(is_active=True).select_related('city')
    context = {
        'ausbildung_programs': programs,
    }
    return render(request, 'ausbildung.html', context)


def ferienjob(request):
    ferienjob_vacancies = Vacancy.objects.filter(type='ferienjob', is_active=True).select_related('city')
    context = {
        'ferienjob_vacancies': ferienjob_vacancies,
    }
    return render(request, 'ferienjob.html', context)


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        phone = request.POST.get('phone', '').strip()
        interest = request.POST.get('interest', 'ferienjob')
        msg = request.POST.get('message', '').strip()

        if name and phone:
            ContactMessage.objects.create(
                name=name,
                phone=phone,
                interest=interest,
                message=msg
            )
            messages.success(request, '✅ Your message has been sent! We will contact you soon.')
            return redirect('contact')
        else:
            messages.error(request, '❌ Please fill in your name and phone number.')

    return render(request, 'contact.html')
