# booklist
Recruitment task.

### Built with

**Python** version 3.8.0<br/>
**Django** version: 3.2.9<br/>
**Django Rest Framework** version: 3.12.4<br/>

### Functionality overview

This is a website which enables the user to add and update books and also fetch them from Google API.

### Installing and Prerequisites

To run the app locally:

1. Clone this repository.

2. Export SECRET_KEY in the terminal:

```
export SECRET_KEY='your-key'
```
3. Create virtual environment and run it:

```
virtualenv venv

source venv/bin/activate
```

3. Go into the app directory and install dependencies:

```
pip install -r requirements.txt
```

4. Make migrations:

```
python manage.py makemigrations
```

5. Migrate:

```
python manage.py migrate
```

6. Create a superuser:

```
python manage.py createsuperuser
```

7. Finally run the server:

```
python manage.py runserver
```

8. You can visit the app at http://127.0.0.1:8000 or http://localhost:8000

### API usage
The application provides one with an API endpoint which enables one to search for books with filters.

To see all the books, visit:
```
GET /api/v1/books/
```

Filters can be applied with the following query parameters:

title__icontains - look for a title<br/>
author__name__icontains - look for an author</br>
pub_language__icontains - look for a publication language<br/>
pub_date__gt - look for a publication date greater than<br/>
pub_date__lt - look for a publication date less than<br/>

For example:
```
GET /api/v1/books/?title__icontains=test&author__name__icontains=test&pub_language__icontains=test&pub_date__gt=2020&pub_date__lt=2021
```


