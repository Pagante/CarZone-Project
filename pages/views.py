from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import redirect, render
from .models import Team
from cars.models import Car
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    teams = Team.objects.all()

    featured_cars = Car.objects.order_by('-created_date').filter(is_features=True)

    all_cars = Car.objects.order_by('-created_date')
    # search_field = Car.objects.values('model', 'city', 'year', 'body_style')
    model_search = Car.objects.values_list('model', flat=True).distinct()
    city_search = Car.objects.values_list('city', flat=True).distinct()
    year_search = Car.objects.values_list('year', flat=True).distinct()
    body_style_search = Car.objects.values_list('body_style', flat=True).distinct()
    data = {
        'teams':teams,
        'featured_cars':featured_cars,
        'all_cars':all_cars,
        'model_search':model_search,
        'city_search':city_search,
        'year_search':year_search,
        'body_style_search':body_style_search
    }
    return render(request, 'pages/index.html', data)


def about(request):
    teams = Team.objects.all()
    data = {
        'teams':teams
    }
    return render(request, 'pages/about.html', data)

def services(request):
    return render(request, 'pages/services.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        phone = request.POST['phone']
        message = request.POST['message']

        # email_subject= "You have a new message from CarZone website regarding the " + subject
        # message_body = "name: " + name, "E-mail: "+ email, "Subject: "+ subject, "Phone: "+ phone, "Message:" + message

        # superusers_emails = User.objects.filter(is_superuser=True).values_list('email')
        # admin_email = superusers_emails

        send_mail(
            subject,
            message,
            'meshlrd14@gmail.com',
            ['meshlrd14@gmail.com'],
            fail_silently=False,
            )

        messages.success(request, 'Thank You for contacting us. We will get back to you shortly.')

        return redirect('contact')

    return render(request, 'pages/contact.html')
