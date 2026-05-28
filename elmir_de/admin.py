from django.contrib import admin
from .models import Vacancy, City, AusbildungProgram, ContactMessage


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'state', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('name',)


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ('title', 'type', 'city', 'salary', 'is_active', 'created_at')
    list_filter = ('type', 'is_active', 'city')
    search_fields = ('title', 'description')
    list_editable = ('is_active',)


@admin.register(AusbildungProgram)
class AusbildungProgramAdmin(admin.ModelAdmin):
    list_display = ('title', 'city', 'duration', 'salary', 'is_active')
    list_filter = ('is_active', 'city')
    search_fields = ('title',)


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'interest', 'created_at', 'is_read')
    list_filter = ('interest', 'is_read')
    list_editable = ('is_read',)
    readonly_fields = ('name', 'phone', 'interest', 'message', 'created_at')
