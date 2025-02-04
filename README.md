# Part 1:  A public API to retrieve Basic Information.

This is a project to return basic information, A project for HNG12 stage 0 backend.

## Technologies 
- Python Django.
- Django rest framework
- VPS for hosting

## Project setup

- Create and activate virtual environment in your desired folder location. `follow different steps for windows or linux`
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

## URL
 http://hng120.homemixsystems.co.ke/api/info/
 

# Part 2: Number Classification API

A Django REST API that classifies numbers based on mathematical properties and fetches a fun fact from the Numbers API.

## 🚀 Features
- Checks if a number is **prime**, **perfect**, or **Armstrong**.
- Determines **parity** (odd/even).
- Computes the **sum of digits**.
- Fetches a **fun fact** from the Numbers API.
- Returns JSON responses with appropriate **HTTP status codes**.

## Output

`Required JSON Response Format (200 OK):
{
    "number": 371,
    "is_prime": false,
    "is_perfect": false,
    "properties": ["armstrong", "odd"],
    "digit_sum": 11,  // sum of its digits
    "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371" //gotten from the numbers API
}
Required JSON Response Format (400 Bad Request)
{
    "number": "alphabet",
    "error": true
}
`

## URL

 http://hng120.homemixsystems.co.ke/api/classify-number?number=371
