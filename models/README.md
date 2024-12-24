# AirBnB Clone v2

## Project Overview
This project builds upon the AirBnB clone v1, introducing new features and storage capabilities using MySQL. The implementation includes ORM with SQLAlchemy and enhances the console functionality.

## Key Features

### Console Improvements
- Enhanced object creation with parameter support
- Syntax: `create <Class name> <param 1> <param 2> <param 3>...`
- Parameter support for strings, floats, and integers
- Example: `create State name="California"`

### Storage Engines
The project supports two storage engines:
1. File Storage (JSON)
2. Database Storage (MySQL)

Storage type can be switched using the `HBNB_TYPE_STORAGE` environment variable:
- `db` for Database Storage
- `file` for File Storage (default)

### Database Configuration
Two MySQL database setups are provided:
1. Development database:
   - Database: `hbnb_dev_db`
   - User: `hbnb_dev`
   - Password: `hbnb_dev_pwd`

2. Test database:
   - Database: `hbnb_test_db`
   - User: `hbnb_test`
   - Password: `hbnb_test_pwd`

## Models

### Base Model
- Serves as the foundation for all other models
- Implements common attributes: id, created_at, updated_at
- Integrates with both storage engines

### User Model
- Attributes:
  - email (string, 128 characters)
  - password (string, 128 characters)
  - first_name (string, 128 characters, nullable)
  - last_name (string, 128 characters, nullable)
- Relationships:
  - places (one-to-many with Place)
  - reviews (one-to-many with Review)

### State and City Models
- State attributes:
  - name (string, 128 characters)
  - cities (relationship to City)
- City attributes:
  - name (string, 128 characters)
  - state_id (foreign key to states.id)
  - places (relationship to Place)

### Place Model
- Attributes:
  - city_id (foreign key to cities.id)
  - user_id (foreign key to users.id)
  - name (string, 128 characters)
  - description (string, 1024 characters, nullable)
  - number_rooms (integer, default 0)
  - number_bathrooms (integer, default 0)
  - max_guest (integer, default 0)
  - price_by_night (integer, default 0)
  - latitude (float, nullable)
  - longitude (float, nullable)
- Relationships:
  - reviews (one-to-many with Review)
  - amenities (many-to-many with Amenity)

### Review Model
- Attributes:
  - text (string, 1024 characters)
  - place_id (foreign key to places.id)
  - user_id (foreign key to users.id)

### Amenity Model
- Attributes:
  - name (string, 128 characters)
- Relationships:
  - place_amenities (many-to-many with Place)

## File Structure
- `console.py`: Command interpreter
- `models/`: Core models and storage engines
  - `engine/`: Storage engine implementations
    - `file_storage.py`: JSON file storage
    - `db_storage.py`: MySQL database storage
  - `base_model.py`: Base model class
  - `user.py`: User model
  - `state.py`: State model
  - `city.py`: City model
  - `place.py`: Place model
  - `review.py`: Review model
  - `amenity.py`: Amenity model
- `setup_mysql_dev.sql`: Development database setup
- `setup_mysql_test.sql`: Test database setup
- `tests/`: Unit tests

## Usage Examples

### Console Commands
```bash
# Create a new User
create User email="user@example.com" password="password123" first_name="John" last_name="Doe"

# Create a Place
create Place city_id="city-id" user_id="user-id" name="Cozy_Cottage" number_rooms=2 max_guest=4

# Create a Review
create Review place_id="place-id" user_id="user-id" text="Great_place!"

# Create an Amenity
create Amenity name="WiFi"
```

### Database Usage
```bash
# Run console with database storage
HBNB_MYSQL_USER=hbnb_dev \
HBNB_MYSQL_PWD=hbnb_dev_pwd \
HBNB_MYSQL_HOST=localhost \
HBNB_MYSQL_DB=hbnb_dev_db \
HBNB_TYPE_STORAGE=db \
./console.py
```

## Requirements
- Python 3.x
- MySQL 5.7
- SQLAlchemy 1.4.x
- MySQLdb 2.x

## Testing
Unit tests must pass for all storage engines:
```bash
python3 -m unittest discover tests
```

For database-specific tests:
```bash
HBNB_ENV=test \
HBNB_MYSQL_USER=hbnb_test \
HBNB_MYSQL_PWD=hbnb_test_pwd \
HBNB_MYSQL_HOST=localhost \
HBNB_MYSQL_DB=hbnb_test_db \
HBNB_TYPE_STORAGE=db \
python3 -m unittest discover tests
``
AUTHOR:SHIGHI`
