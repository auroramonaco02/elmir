from django.db import models


class City(models.Model):
    name = models.CharField(max_length=100)
    state = models.CharField(max_length=100, blank=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Cities"
        ordering = ['name']

    def __str__(self):
        return self.name


class Vacancy(models.Model):
    TYPE_CHOICES = [
        ('ferienjob', 'Ferienjob (3 Monate)'),
        ('arbeit', 'Arbeitsvertrag (8 Monate)'),
        ('ausbildung', 'Ausbildung'),
    ]

    title = models.CharField(max_length=200)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True, blank=True)
    description = models.TextField(blank=True)
    requirements = models.TextField(blank=True)
    salary = models.CharField(max_length=100, blank=True)
    duration = models.CharField(max_length=100, blank=True)
    accommodation_included = models.BooleanField(default=False)
    meals_included = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Vacancies"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.title} — {self.city} ({self.get_type_display()})"

    def get_city_name(self):
        return self.city.name if self.city else "Various Cities"


class AusbildungProgram(models.Model):
    title = models.CharField(max_length=200)
    icon = models.CharField(max_length=10, default='🎓')
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True, blank=True)
    description = models.TextField(blank=True)
    duration = models.CharField(max_length=100, default='2–3 Jahre')
    salary = models.CharField(max_length=100, blank=True)
    requirements = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title


class ContactMessage(models.Model):
    INTEREST_CHOICES = [
        ('ferienjob', 'Ferienjob'),
        ('arbeit', 'Arbeitsvertrag'),
        ('ausbildung', 'Ausbildung'),
    ]

    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=30)
    interest = models.CharField(max_length=20, choices=INTEREST_CHOICES, default='ferienjob')
    message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} — {self.phone} ({self.created_at.strftime('%d.%m.%Y')})"
