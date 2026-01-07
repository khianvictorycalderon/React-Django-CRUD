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
        users = User.objects.all().values("id", "first_name", "last_name", "age")
        return JsonResponse(list(users), safe = False)
    return JsonResponse({ 
        "message": "Method not allowed"
    }, status = 405)

@csrf_exempt
def user_update(request, user_id: int):
    if request.method not in ["PATCH", "PUT"]:
        return JsonResponse({"message": "Method not allowed"}, status=405)

    # Find user
    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return JsonResponse({"message": "User not found"}, status=404)

    # Parse JSON body
    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({"message": "Invalid JSON"}, status=400)

    # Update fields if they exist
    if "first_name" in data:
        user.first_name = data["first_name"]
    if "last_name" in data:
        user.last_name = data["last_name"]
    if "age" in data:
        user.age = data["age"]

    user.save()

    return JsonResponse({
        "message": "User updated successfully",
        "user": {
            "id": user.id,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "age": user.age
        }
    })

@csrf_exempt
def user_delete(request, user_id: int):
    if request.method == "DELETE":
        try:
            user = User.objects.get(id=user_id)
            user.delete()
            return JsonResponse({
                "message": "User deleted successfully."
            }, status = 200)
        except User.DoesNotExist:
            return JsonResponse({
                "message": "User not found."
            }, status=404)
    
    return JsonResponse({
        "message": "Method not allowed"
    }, status=405)