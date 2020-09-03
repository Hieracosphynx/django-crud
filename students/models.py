from django.db import models

# Create your models here.

class Student(models.Model):
    ACCOUNTING = 'ACC'
    INFO_TECH = 'ICT'
    MEDICAL_TECHNOLOGY = 'MEDTECH'
    CIVIL_ENGINEER = 'CIVENG'

    COURSE_IN_SCHOOL = [
        (ACCOUNTING, 'Accounting'),
        (INFO_TECH, 'Information Communications Technology'),
        (MEDICAL_TECHNOLOGY, 'Medical Technology'),
        (CIVIL_ENGINEER, 'Civil Engineer')
        ]
    student_number = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    student_address = models.CharField(max_length=120)
    course = models.CharField(max_length=50, choices=COURSE_IN_SCHOOL, default=None)

    class Meta:
        ordering = ["last_name"]
        verbose_name_plural = "students"

    def __str__(self):
        return self.student_number
