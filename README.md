## Event Management System

This Event Management System is a web application developed using Django, a high-level Python web framework that encourages rapid development and clean, pragmatic design. The system allows users to manage events efficiently, providing features for event creation, booking, and user authentication.

### Features

- **User Registration and Authentication**: Users can create accounts, log in, and log out securely.
- **Event Management**: Authenticated users can create, view, and manage events.
- **Booking System**: Users can book events and view their bookings.
- **Contact Form**: A contact form for users to reach out with inquiries or feedback.

This project aims to streamline the process of event management by providing a user-friendly interface and robust backend functionality. It can be used by event organizers to manage various types of events, handle bookings, and communicate with participants effectively.

### Technologies Used

- **Django**: The primary framework used for backend development.
- **Bootstrap**: For responsive and modern frontend design.
- **SQLite**: Default database for development and testing purposes.

The project is structured to follow best practices in web development, ensuring maintainability and scalability.


### Install Django using pip
```bash
# Install Django
pip install django
```


### Perform database migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### Run the development server
```bash
python manage.py runserver
```

### Create a superuser
1. To create a superuser, run the following command:
```bash
python manage.py createsuperuser
```