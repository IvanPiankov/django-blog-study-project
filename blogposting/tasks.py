from django.contrib.auth.models import User
from django.core.mail import send_mail
from time import sleep
from celery import shared_task


@shared_task
def send_feedback_email(email_address, message):
    superusers_emails = list(User.objects.filter(is_superuser=True).exclude(email="").values_list('email', flat=True))
    sleep(10)  # Simulate expensive operation
    send_mail(
        "Your Feedback",
        f"\t{message}\n\nThank you!",
        "support@example.com",
        [email_address],
        fail_silently=False,
    )
    if superusers_emails:
        send_mail(
            "Feedback by user:",
            f"\t{message}\n\n",
            "support@example.com",
            superusers_emails,
            fail_silently=False
        )
