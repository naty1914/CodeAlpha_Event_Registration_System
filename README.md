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
- **Frontend**: HTML, CSS
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
    pip install -r requirements.txt
    ```

4. **Generate the requirements file**:
    ```bash
    pip freeze > requirements.txt
    ```

5. **Apply migrations**:
    ```bash
    python manage.py migrate
    ```

6. **Create a superuser**:
    ```bash
    python manage.py createsuperuser
    ```

7. **Run the development server**:
    ```bash
    python manage.py runserver
    ```

8. **Access the application**:
    Open your web browser and go to `http://127.0.0.1:8000/`.

## Email Configuration

To configure email settings, open the `settings.py` file and update the following settings with your email provider's details:

```python


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.your-email-provider.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your-email@example.com'
EMAIL_HOST_PASSWORD = 'your-email-password'
DEFAULT_FROM_EMAIL = 'your-email@example.com'

## Usage

1. **View Events**:
    - Navigate to the homepage to see a list of all available events.

2. **Register for an Event**:
    - Click on an event to view its details and fill out the registration form.

3. **Manage Registrations**:
    - Use the unique token sent to your email to cancel your registration