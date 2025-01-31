# A public API to retrieve Basic Information.

This is a project to return basic information, A project for HNG12 stage 0 backend.

## Technologies 
- Python Django.
- Django rest framework
- VPS for hosting

## Project setup

- Create and activate virtual environment in your desired folder location. `follow different steps foe windows or linux`
- Clone the project from `git clone https://github.com/homemix/HNG12Stage0`
- Change to root folder `cd HNG12Stage0`
- Install required packages `pip install -r requirements.txt`
- Run the project `python manage runserver`
- The project is served at `http://127.0.0.1:8000/api/info/`
- NOTE: This is a django project and follows django convention.

## Sample Output

From the GET endpoint this is the sample output.

`{
    "email": "kenmutati@gmail.com",
    "current_datetime": "2025-01-31T03:24:35.099210Z",
    "github_url": "https://github.com/homemix/HNG12Stage0"
}`