# 🇩🇪 Elmir_DE — Germany Work & Study Portal

**Languages / Тилдер / Языки:** 🇩🇪 DE | 🇰🇬 KY | 🇷🇺 RU | 🇬🇧 EN | 🇹🇷 TR  
**Contact / Байланыш:** +996 502 826 439

---

## 🚀 Quick Setup (English)

### Requirements
- Python 3.9+
- pip

### Installation

```bash
# 1. Enter project folder
cd Elmir_DE

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate        # Linux/Mac
venv\Scripts\activate           # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run migrations
python manage.py migrate

# 5. Load initial data (cities + sample vacancies)
python manage.py loaddata elmir_de/fixtures/initial_data.json

# 6. Create admin user
python manage.py createsuperuser

# 7. Start the server
python manage.py runserver
```

Visit: **http://127.0.0.1:8000**  
Admin: **http://127.0.0.1:8000/admin**

---

## 🚀 Орнотуу (Кыргызча)

### Талаптар
- Python 3.9+

### Орнотуу

```bash
cd Elmir_DE
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py loaddata elmir_de/fixtures/initial_data.json
python manage.py createsuperuser
python manage.py runserver
```

Сайт: **http://127.0.0.1:8000**  
Башкаруу панели: **http://127.0.0.1:8000/admin**

---

## 🚀 Установка (Русский)

```bash
cd Elmir_DE
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py loaddata elmir_de/fixtures/initial_data.json
python manage.py createsuperuser
python manage.py runserver
```

Сайт: **http://127.0.0.1:8000**  
Панель управления: **http://127.0.0.1:8000/admin**

---

## 📁 Project Structure

```
Elmir_DE/
├── manage.py
├── requirements.txt
├── elmir_de_project/          # Django project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── elmir_de/                  # Main app
│   ├── models.py              # Database models
│   ├── views.py               # Page views
│   ├── urls.py                # URL routing
│   ├── admin.py               # Admin panel
│   └── fixtures/
│       └── initial_data.json  # Sample data (16 cities + vacancies)
├── templates/                 # HTML templates
│   ├── base.html
│   ├── index.html
│   ├── vacancies.html
│   ├── ausbildung.html
│   ├── ferienjob.html
│   └── contact.html
└── static/
    ├── css/style.css          # Main styles
    └── js/
        ├── i18n.js            # 5-language translations
        └── main.js            # Animations & interactions
```

## 📞 Contact / Байланыш / Контакт

**Phone / WhatsApp / Telegram:** +996 502 826 439

## 🌐 Pages

| URL | Page |
|-----|------|
| `/` | Home |
| `/vacancies` | All Vacancies |
| `/ausbildung` | Ausbildung Programs |
| `/ferienJob` | Ferienjob |
| `/contact` | Contact Form |
| `/admin` | Admin Panel |
