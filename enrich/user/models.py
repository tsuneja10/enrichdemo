from django.db import models
from django.contrib.auth.models import Group
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

EMAIL_VALID_CHOICES = (
    (1, "Null"),
    (2, "False"),
    (3, "True"),
   
)
class CustomAccountManager(BaseUserManager):
    def create_superuser(self, email, user_name, first_name, password, **other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')

        return self.create_user(email, user_name, first_name, password, **other_fields)

    def create_user(self, email, user_name, first_name, password, **other_fields):

        if not email:
            raise ValueError(_('You must provide an email address'))

        email = self.normalize_email(email)
        user = self.model(email=email, user_name=user_name,
                          first_name=first_name, **other_fields)
        user.set_password(password)
        user.save()
        return user


class NewUser(AbstractBaseUser, PermissionsMixin):
    email = models.CharField(max_length=250, unique=True)
    user_name = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE,blank=True,null=True)
    start_date = models.DateTimeField(default=timezone.now)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name', 'first_name','last_name']

    def __str__(self):
        return self.user_name

class LanguageConvert(models.Model):

    input_text = models.CharField(max_length=150,  blank=False)
    converted_text = models.CharField(max_length=150, blank=True)
    input_lan = models.CharField(max_length=150, blank=False)
    output_lan = models.CharField(max_length=150, blank=False)
    user = models.ForeignKey(NewUser, on_delete=models.CASCADE,blank=False)
    email = models.CharField(max_length=150,  blank=False)
    created_at = models.DateTimeField(default=timezone.now)
    is_valid_email = models.CharField(
        max_length = 20,
        choices = EMAIL_VALID_CHOICES,
        default = '1'
        )
    REQUIRED_FIELDS = ['input_text', 'converted_text','input_lan','output_lan','user','email']

    def __str__(self):
        return self.input_text

