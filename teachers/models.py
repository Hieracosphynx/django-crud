from django.db import models
from enum import Enum
from django.core.validators import RegexValidator
# Create your models here.
class Type(Enum):
    MALE = 'M'
    FEMALE = 'F'
    UNDEFINED = 'U'


class Teacher(models.Model):
    phone_regex = RegexValidator(regex=r'^\+1?d{9,15}',message='Phone number')

    teacher_number = models.CharField(max_length=120)
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    gender = models.CharField(max_length= 10, choices = [(tag,tag.value) for tag in Type] )
    address = models.CharField(max_length=120)
    mobile_number = models.CharField(validators=[phone_regex],max_length=17, blank=True)

    class Meta:
        ordering = ['last_name']
        verbose_name_plural = "teachers"