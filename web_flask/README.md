irBnB Clone - Web Framework

## Description
This is the second phase of the AirBnB clone project where we integrate Flask web framework to create dynamic web pages for our application. The project implements a RESTful API that handles database storage and front-end integration.

## Features
- Flask web application with multiple routes
- Database storage engine with both file and MySQL storage options
- Dynamic webpage rendering with Jinja2 templates
- RESTful API endpoints
- State and City relationships
- HTML filters for amenities and locations

## Environment
- Python 3.8+
- Flask 2.0+
- MySQL 5.7+
- SQLAlchemy 1.4+

## Setup
```bash
# Install dependencies
pip3 install -r requirements.txt

# Set up MySQL database
cat setup_mysql_dev.sql | mysql -hlocalhost -uroot -p

# Run Flask application
python3 -m web_flask.0-hello_route
```

## Usage
The web application will be listening on `0.0.0.0:5000`. Available routes include:
- `/`: Display "Hello HBNB!"
- `/hbnb`: Display "HBNB"
- `/states_list`: Display list of all states
- `/cities_by_states`: Display all cities by state
- `/states/<id>`: Display specific state and its cities
- `/hbnb_filters`: Display locations and amenities filters

## Authors
Shighi
