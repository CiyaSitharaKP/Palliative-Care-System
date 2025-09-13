🏥 Palliative Care Management System

A full-stack web application for managing patients, staff, medicines, bed equipment, and reports in a palliative care setup. Built with Django, MySQL, HTML, CSS, JavaScript, Bootstrap, jQuery, and AJAX.



🚀 Features

Admin Module :

Add, view, edit, delete staff details

Add, view, edit, delete bed equipment details

View divisions and patients in each division

View patient history & reports

Change password


Staff Module :

Add, edit, view, delete patient details

Add, edit, view, delete medicine details

Add reports for patients

Add & view feedback

My Profile

Change password




🛠 Tech Stack

Frontend: HTML, CSS, Bootstrap, JavaScript, jQuery, AJAX

Backend: Python, Django

Database: MySQL

Tools: VS Code, Git, GitHub




📂 Project Setup

1. Clone repository

git clone https://github.com/YourUsername/palliative-care-system.git
cd palliative-care-system


2. Create virtual environment & activate

python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate


3. Database setup

Create a MySQL database (e.g., palliative_care_db)

Update database settings in settings.py

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'palliative_care_db',
        'USER': 'root',
        'PASSWORD': 'yourpassword',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

4. Run migrations
   
python manage.py makemigrations

python manage.py migrate


5. Create superuser
   
python manage.py createsuperuser


6. Run server

python manage.py runserver




📸 Screenshots

All screenshots of the project are available inside the "screenshots" folder of this respository.



✨ Future Enhancements

Role-based access with Django REST API

Patient report analytics with charts

Online consultation & appointment booking

Cloud deployment





🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.




📜 License

This project is for educational purposes only.

