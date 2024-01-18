from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin, UserManager, AbstractUser
from django.db import models
from django.db.models import OneToOneField
from django.utils.translation import gettext_lazy as _

# Create your models here.


class CustomUserManager(BaseUserManager):
    def create_user(self, phone_number, password=None, **extra_fields):
        if not phone_number:
            raise ValueError('Users must have a phone number')
        if len(phone_number) != 13:
            raise ValueError('Phone number is incorrect')

        user = self.model(
            phone_number=phone_number,
            **extra_fields,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, password, **extra_fields):
        user = self.create_user(
            phone_number=phone_number,
            password=password,
            **extra_fields,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractUser, PermissionsMixin):
    first_name = models.CharField(_("First name"), max_length=50, blank=True)
    last_name = models.CharField(_("Last name"), max_length=50, blank=True)
    phone_number = models.CharField(_("Phone number"), max_length=13, blank=True, unique=True)
    email = models.EmailField(_("Email address"), unique=True, null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    username = models.CharField(_("username"), max_length=50, unique=True, null=True, blank=True)
    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    # groups = models.ManyToManyField(
    #     'auth.Group',
    #     related_name='custom_user_set',
    #     # Other fields...
    # )
    # user_permissions = models.ManyToManyField(
    #     'auth.Permission',
    #     related_name='custom_user_set',
    #     # Other fields...
    # )

    def full_name(self):
        return f'{self.first_name} {self.last_name}'


class Driver(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='driver')
    pinfl = models.CharField(_("PINFL"), max_length=14, unique=True)


class Role(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    role = models.ForeignKey(Role, on_delete=models.CASCADE, related_name='profile')

    def __str__(self):
        return f"{self.user.full_name()} {self.role.name}"
