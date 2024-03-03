# E-commerce Website

<p align="center">
    <img src="docs/images/.png" width='500'/>
</p>

Build a full e-commerce website.


**Features:**


**Techs Used:**

- Python, Django
- JavaScript
- Bootstrap

Further it can be implemented with: React.js, REST API (Django Rest Framework) and Docker or Postgres for database.

Project Guide: [docs](docs/)

### Setup

1. Clone, Create Env, Install requirements and run server.

```bash
# Clone the repository
git clone

# Create virtual environment
python -m venv env

# Activate the environment
.\env\Scripts\activate

# Install requirements
pip install -r requirements.txt

# Run server
python manage.py runserver
```


### Project Structure

```bash
app
├───Core
│   ├───migrations
│   ├───templates
│   ├───tests
│   ├───urls.py
│   └───views.py
├───QuantumCart
│   ├───settings.py
│   ├───urls.py
│   └───wsgi.py
├───docs
│   ├───images
│   └───README.md
├───products
│   ├───migrations
│   ├───templates
│   ├───tests
│   ├───urls.py
│   └───views.py
├───static
│   └───css
├───templates
├───.gitignore
├───db.sqlite3
├───manage.py
├───README.md
└───requirements.txt
```
