from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages

from user.models import UserProfile


@login_required
def home(request):
    return render(request, 'home.html')


def register_view(request):
    if request.method == 'POST':
        full_name = request.POST['username'] 
        language = request.POST['language']   
        terms_agreed = request.POST.get('terms', False)  
        
        # Create a username from the full name (e.g., john_doe)
        username = full_name.lower().replace(' ', '_')
        
        # Validate inputs
        if not terms_agreed:
            messages.error(request, 'You must agree to the terms and conditions.')
        elif not language:
            messages.error(request, 'Please select a language.')
        else:
            try:
                # Create user with the generated username
                user = User.objects.create_user(username=username, password=None)  # No password for voice authentication
                
                # Save additional information in user profile or similar model
                user_profile, created = UserProfile.objects.get_or_create(user=user)
                user_profile.full_name = full_name
                user_profile.language = language
                user_profile.save()
                
                # Log the user in
                login(request, user)
                return redirect('home')
            except Exception as e:
                messages.error(request, f'Registration failed: {str(e)}')
    
    return render(request, 'registration/register.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        
        # Check if we're getting a voice authentication
        # You would replace this with your actual voice authentication logic
        user = None
        
        # If you have a traditional password field as fallback
        password = request.POST.get('password', None)
        if password:
            user = authenticate(request, username=username, password=password)
        else:
            # This is where you would implement voice authentication
            # For example, you might have a voice sample saved in request.FILES
            # voice_sample = request.FILES.get('voice_sample')
            # user = authenticate_with_voice(username, voice_sample)
            
            # For now, as a placeholder implementation:
            from django.contrib.auth.models import User
            try:
                user = User.objects.get(username=username)
                # In a real implementation, verify voice before setting user
            except User.DoesNotExist:
                user = None
        
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Authentication failed. Please try again.")
    
    return render(request, 'registration/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

from django.core.mail import send_mail
from django.http import HttpResponse

def test_email(request):
    send_mail(
        'Test Email',
        'This is a test email from Django.',
        'santosisadru@gmail.com',  # From email (must match EMAIL_HOST_USER)
        ['santosisadru@example.com'],  # Replace with your actual recipient email
        fail_silently=False,  # Make Django raise errors if email fails
    )
    return HttpResponse('Test email sent!')
