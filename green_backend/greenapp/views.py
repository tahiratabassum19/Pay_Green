from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.shortcuts import redirect
from .models import User

def store_message(request):
    messages = request.GET.get('message', '')
    return JsonResponse({'status': 'success'})

def signup(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        date_of_birth = request.POST.get('date_of_birth')
        type_of_card = request.POST.get('type_of_card')
        total_income = request.POST.get('total_income')

        user = User(
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
            date_of_birth=date_of_birth,
            type_of_card=type_of_card,
            total_income=total_income
        )
        user.save()

        # after showing the success message it will redirect to the login page to login 
        messages.success(request, 'Signed Up. Please login.')
        return redirect('login')

    return HttpResponse('error')

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)
            if user.password == password:
                messages.success(request, 'Login successful')
                return redirect('Home')
            else:
                messages.error(request, 'Incorrect password')
                return redirect('login')
        
        except User.DoesNotExist:
            messages.error(request, 'User not found. Please sign up.')
            return redirect('signup')

    return HttpResponse('Invalid request method.')

def calculate_total_score(request):
    initial_scores = {
        'food': 0,
        'transportation': 0,
        'energy_production': 0,
        'hobbies': 0
    }

    # Calculate the carbon usages
    carbon_use = {
        'food': 10,  
        'transportation': 20,  
        'energy_production': 5,  
        'hobbies': 15  
    }

    score_changed = {
        'food': 0,
        'transportation': 0,
        'energy_production': 0,
        'hobbies': 0
    }

    for types, carbon_use in carbon_use.items():
        if carbon_use <= initial_scores[types]:
            score_changed[types] += 1
        else:
            score_changed[types] -= 1

    # Calculating the total score
    total_score = sum(initial_scores.values()) + sum(score_changed.values())


# frontend show part 
