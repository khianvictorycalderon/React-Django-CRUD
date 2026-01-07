import json
from django.http import JsonResponse
from django.shortcuts import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def demo(request):
    return HttpResponse("Your API is working!")

@csrf_exempt
def user(request):

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

        return JsonResponse({
            "message": "Successfully added!"
        }, status = 200)
    
    return JsonResponse({ 
        "message": "Method not allowed"
    }, status = 405)