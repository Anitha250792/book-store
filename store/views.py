from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render, redirect

from .forms import ContactForm
from . import data


def home(request):
    """Render the Inkleaf Book House landing page with all display content."""
    form = ContactForm()
    context = {
        "business": data.BUSINESS,
        "stats": data.STATS,
        "about_features": data.ABOUT_FEATURES,
        "categories": data.CATEGORIES,
        "books": data.BOOKS,
        "best_sellers": data.BEST_SELLERS,
        "offer": data.OFFER,
        "author": data.AUTHOR_SPOTLIGHT,
        "reading_benefits": data.READING_BENEFITS,
        "why_choose_us": data.WHY_CHOOSE_US,
        "testimonials": data.TESTIMONIALS,
        "gallery": data.GALLERY,
        "events": data.EVENTS,
        "delivery": data.DELIVERY,
        "form": form,
    }
    return render(request, "store/home.html", context)


def contact_enquiry(request):
    """Handle the enquiry form submission (no database storage)."""
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            cleaned = form.cleaned_data

            if settings.EMAIL_HOST_USER and settings.ENQUIRY_RECEIVING_EMAIL:
                subject = f"New enquiry from {cleaned['name']} — Inkleaf Book House"
                body = (
                    f"Name: {cleaned['name']}\n"
                    f"Phone: {cleaned['phone']}\n"
                    f"Email: {cleaned['email']}\n"
                    f"Interested in: {cleaned['interested_in']}\n\n"
                    f"Message:\n{cleaned['message']}"
                )
                try:
                    send_mail(
                        subject,
                        body,
                        settings.EMAIL_HOST_USER,
                        [settings.ENQUIRY_RECEIVING_EMAIL],
                        fail_silently=True,
                    )
                except Exception:
                    pass

            messages.success(
                request,
                "Thank you! Your enquiry has been received. Our team will contact you shortly.",
            )
            return redirect("/#contact")
        else:
            messages.error(request, "Please check the form for errors and try again.")

    return redirect("/#contact")
