from django.core.mail import send_mail
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings

User = get_user_model()


@receiver(post_save, sender=User)

def send_notification_usr(sender, instanse, created, **kwargs):
    if created:
        subject = f'Уведомление о регистрации.'
        message = f'''Приветствуем {instanse.username} .
вы успешно зарегестрированы!
'''


        from_email = settings.EMAIL_HOST_USER
        to_email = instanse.email
        send_mail(subject, message, from_email, [to_email])