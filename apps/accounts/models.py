from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _




class CustomUser(AbstractUser):
    email = models.EmailField(
        'Электронная почта',
        unique=True,
    )
    phone_number = PhoneNumberField(
        'Номер телефона',
        help_text = 'Пример: +996700707070'
    )
    is_active = models.BooleanField(
        _("active"),
        default=False,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )


    REQUIRED_FIELDS = ['email', 'phone_number']
    def __str__(self):
        return f'{self.username}'

    class Meta:
        verbose_name= 'Пользователь'
        verbose_name_plural= 'Пользователи'
