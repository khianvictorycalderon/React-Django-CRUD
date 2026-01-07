import json
from django.http import JsonResponse
from django.shortcuts import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import User

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

        # Field validation
        if not first_name or not last_name or not age:
            return JsonResponse({"message": "Missing fields"}, status=400)
        
        # Save to database
        try:
            User.objects.create(
                first_name = first_name,
                last_name = last_name,
                age = age
            )
        except Exception as e:
            return JsonResponse({
                "message": f"Error adding new user: {str(e)}"
            }, status = 500)

        return JsonResponse({
            "message": "Successfully added user!"
        }, status = 200)
    
    return JsonResponse({ 
        "message": "Method not allowed"
    }, status = 405)

@csrf_exempt
def users_list(request):
    if request.method == "GET":
        pass