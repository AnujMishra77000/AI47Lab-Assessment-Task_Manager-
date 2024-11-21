from django.core.mail import send_mail
from django.conf import settings

def send_email_to_user(email):
       subject = "This email is system generated server"
       message = settings.SITE_URL
       from_email = settings.EMAIL_HOST_USER
       recipient_list = [email]
       send_mail(subject, message, from_email, recipient_list)
