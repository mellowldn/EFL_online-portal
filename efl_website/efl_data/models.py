from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, Group, Permission, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import BaseUserManager

class NewEmployeeManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        # Normalize the email by lowercasing it
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

    def get_by_natural_key(self, employee):
        return self.get(employee=employee)


class NewEmployee(AbstractBaseUser, PermissionsMixin):
    dob = models.DateField()
    email = models.EmailField(max_length=255, unique=True)
    surname = models.CharField(max_length=255)
    forename = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    postcode = models.CharField(max_length=255)
    add1 = models.CharField(max_length=255)
    add2 = models.CharField(max_length=255)
    employee = models.CharField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    ROLE_CHOICES = [
        ('EMP', 'Employee'),
        ('MNG', 'Manager'),
        ('CEO', 'CEO'),
    ]
    role = models.CharField(max_length=3, choices=ROLE_CHOICES, default='EMP')
    USERNAME_FIELD = 'employee'
    REQUIRED_FIELDS = ['email', 'password']

    groups = models.ManyToManyField(
        Group,
        verbose_name=_('groups'),
        blank=True,
        help_text=_(
            'The groups this user belongs to. A user will get all permissions '
            'granted to each of their groups.'
        ),
        related_name="customuser_set",
        related_query_name="user",
    )

    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        help_text=_('Specific permissions for this user.'),
        related_name="customuser_set",
        related_query_name="user",
    )
    
    objects = NewEmployeeManager()

    class Meta:
        db_table = 'newemployee'