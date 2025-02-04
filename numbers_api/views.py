import requests
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def is_perfect(n):
    """Check if a number is a perfect number."""
    return n == sum(i for i in range(1, n) if n % i == 0)


def is_armstrong(n):
    """Check if a number is an Armstrong number."""
    digits = [int(d) for d in str(n)]
    return sum(d ** len(digits) for d in digits) == n


def get_fun_fact(n):
    """Fetch a fun fact from the Numbers API."""
    try:
        response = requests.get(f"http://numbersapi.com/{n}")
        if response.status_code == 200:
            return response.text
    except requests.RequestException:
        return None
    return None


@api_view(["GET"])
def classify_number(request):
    """Classifies a number with various mathematical properties."""
    number_param = request.GET.get("number")

    if number_param is None or not number_param.lstrip("-").isdigit():
        return Response({"number": "alphabet", "error": True}, status=status.HTTP_400_BAD_REQUEST)

    number = int(number_param)

    properties = ["odd" if number % 2 else "even"]
    if is_armstrong(number):
        properties.append("armstrong")

    response_data = {
        "number": number,
        "is_prime": is_prime(number),
        "is_perfect": is_perfect(number),
        "properties": properties,
        "digit_sum": sum(int(d) for d in str(abs(number))),
        "fun_fact": get_fun_fact(number)
    }

    return Response(response_data, status=status.HTTP_200_OK)
