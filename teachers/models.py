from django.db import models
from enum import Enum
from django.core.validators import RegexValidator
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.
class Type(Enum):
    MALE = 'M'
    FEMALE = 'F'
    UNDEFINED = 'U'


class Teacher(models.Model):
    # phone_regex = RegexValidator(regex=r'^\+\d{9,15}$',message='Phone number')
    # mobile_number = models.CharField(validators=[phone_regex],max_length=16, blank=True)
    # gender = models.CharField(choices = [(tag,tag.value) for tag in Type], max_length=15 )
    MALE = 'M'
    FEMALE = 'F'
    UNDEFINED = 'U'

    GENDER = [
        (MALE, 'MALE'),
        (FEMALE, 'FEMALE'),
        (UNDEFINED, 'UNDEFINED')
    ]

    teacher_number = models.CharField(max_length=120)
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    gender = models.CharField(choices=GENDER, max_length=15)
    address = models.CharField(max_length=120)
    mobile_number = PhoneNumberField(blank = True)
    class Meta:
        ordering = ['last_name']
        verbose_name_plural = "teachers"

    def __str__(self):
        return self.teacher_number