# Servifi Django Project

## Overview
Servifi is a Django-based web application featuring user authentication, a dashboard interface, and a ticketing system. It is designed for rapid development and prototyping, using SQLite for local data storage and Gmail SMTP for email (development mode).

## Features
- Custom user authentication (with a custom user model)
- User dashboard for managing workflows
- Ticketing system for issue tracking or support
- Admin interface with statistics and enhanced widgets
- Modular app structure for easy maintenance and extension

## Technology Stack
- Python 3.x
- Django 4.2.6
- SQLite (local development)
- Third-party Django apps: `admin_tools_stats`, `django_nvd3`, `widget_tweaks`
- Frontend: HTML templates + static assets (CSS, JS)

## Project Structure
```
servifi/
├── accounts/     # User authentication and profile management
├── dashboard/    # Dashboard UI and logic
├── ticket/       # Ticketing/issue tracking app
├── django_project/ # Project settings and configuration
├── static/       # Static files (CSS, JS, images)
├── templates/    # HTML templates
├── db.sqlite3    # SQLite database (development)
├── manage.py     # Django management script
```

## Getting Started
### Prerequisites
- Python 3.x
- pip (Python package manager)

### Installation
1. Clone the repository:
   ```bash
   git clone <your-repo-url>
   cd servifi
   ```
2. (Optional) Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install django django-nvd3 django-admin-tools widget-tweaks
   ```
4. Apply migrations:
   ```bash
   python manage.py migrate
   ```
5. Create a superuser for admin access:
   ```bash
   python manage.py createsuperuser
   ```
6. Run the development server:
   ```bash
   python manage.py runserver
   ```

### Access the App
- Visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser.
- Admin interface: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

## Configuration Notes
- **Email:** Uses Gmail SMTP for sending emails. By default, emails are printed to the console for development.
- **Custom User Model:** The project uses a custom user model located in `accounts.User`. Update references accordingly if extending authentication.
- **Static & Templates:** Place your static files in `static/` and HTML templates in `templates/`.

## License
MIT License

---

For questions or contributions, please open an issue or submit a pull request.
