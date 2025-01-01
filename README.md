# CodeAlpha_Event_Registration_System

## Overview
The CodeAlpha Event Registration System is a web application built using Django that allows users to register for events, view event details, and manage their registrations. The system includes features such as email notifications for registration confirmations and cancellations.

## Features
- **Event Listing**: View a list of all available events.
- **Event Details**: View detailed information about each event.
- **Event Registration**: Register for events using a simple form.
- **Manage Registrations**: Cancel registrations using a unique token sent via email.
- **Email Notifications**: Receive confirmation and cancellation emails.

## Technologies Used
- **Backend Framework**: Django (Python)
- **Database**: SQLite
- **Frontend**: HTML, CSS,Bootstrap
- **Email**: Django's email backend

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/naty1914/CodeAlpha_Event_Registration_System.git
    cd CodeAlpha_Event_Registration_System
    ```

2. **Create a virtual environment**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install dependencies**:
    ```bash
    cd  event_registration_system 
    pip install -r requirements.txt
    ```



4. **Apply migrations**:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5. **Create a superuser**:
    ```bash
    python manage.py createsuperuser
    ```

6. **Run the development server**:
    ```bash
    python manage.py runserver
    ```

7. **Access the application**:
    Open your web browser and go to `http://127.0.0.1:8000/`. 
8. **Access the admin panel**:
    Go to `http://127.0.0.1:8000/admin/` and log in using the superuser credentials you created earlier. You can add, edit, and manage events, registrations, and users from the admin panel.


## Email Configuration

To configure email settings, open the `settings.py` file and update the following settings with your email provider's details:
```python


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'your-email-provider.com like smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your-email@example.com'
EMAIL_HOST_PASSWORD = 'your-email-password'
DEFAULT_FROM_EMAIL = 'your-email@example.com'
```
 ## Note: If you don't have an email provider, you can comment out the send_mail function calls in the views.py file.
## Usage

1. **View Events**:
    - Navigate to the homepage to see a list of all available events.

2. **Register for an Event**:
    - Click on an event to view its details and fill out the registration form.

3. **Manage Registrations**:
    - Use the unique token sent to your email to cancel your registration