import json
from django.http import JsonResponse

# Create your views here.
def demo(request):

    if request.method == "POST":

        # Parse JSON from body
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({
                "message": "Invalid JSON"
            }, status = 400)
        
        first_name = data.get("first_name")
        last_name = data.get("last_name")
        age = data.get("age")

        print("Received data:")
        print("First Name:", first_name)
        print("Last Name:", last_name)
        print("Age:", age)