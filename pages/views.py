from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings


def home(request):
    return render(request, 'pages/home.html')


def about(request):
    return render(request, 'pages/about.html')


def experience(request):
    return render(request, 'pages/experience.html')


def contact(request):
    success = False
    error_message = None
    if request.method == "POST": # means the the form was not empty and user submitted
        form = ContactForm(request.POST) 
        #collect info from the form
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            #build email content
            message_body = (
                f'You received a new contact email from your portfolio app,\n\nFrom:  {name}\nEmail: {email}\nMessage: {message}'
            )
            try:
                send_mail(
                    subject="New Portfolio Form Submission",
                    message=message_body,
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[settings.DEFAULT_FROM_EMAIL],
                    fail_silently=False,
                )
                success = True
                form = ContactForm()
            except Exception as exc:
                error_message = (
                    "Sorry, the email could not be sent right now. Please try again in a moment."
                )
                form.add_error(None, str(exc))
    else:
        form = ContactForm()

    return render(request, "pages/contact.html", {
        "form": form,
        "success": success,
        "error_message": error_message,
    })
