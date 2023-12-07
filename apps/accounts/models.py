from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField





class CustomUser(AbstractUser):
    email = models.EmailField(
        'Электронная почта',
        unique=True,
    )
    phone_number = PhoneNumberField(
        'Номер телефона',
        help_text = 'Пример: +996700707070'
    )
    REQUIRED_FIELDS = ['email', 'phone_number']
    def __str__(self):
        return f'{self.username}'

    class Meta:
        verbose_name= 'Пользователь'
        verbose_name_plural= 'Пользователи'
