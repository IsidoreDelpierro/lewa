from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.

class Institution(models.Model):
    OWNERSHIP = (
            ('public': 'Public'),
            ('private': 'Private'),
            ('religious': 'Religious'),
    )
    name = models.CharField(max_length=400)
    address = models.CharField(max_length=100)
    ownership = models.CharField(max_length=20, choices=OWNERSHIP)

    class Meta:
        verbose_name_plural = "Institutions"

    def __str__(self):
        return self.name

class Faculty(models.Model):
    faculty = models.CharField(max_length=200)
    institution = models.ForeignKey(Institution, default=1, verbose_name="Institution", on_delete=models.SET_DEFAULT)

    class Meta:
        verbose_name_plural = "Faculties"

    def __str__(self):
        return str(self.faculty)

class Department(models.Model):
    department = models.CharField(max_length=200)
    faculty = models.ForeignKey(Faculty, default=1, verbose_name="Faculty", on_delete=models.SET_DEFAULT)

    class Meta:
        verbose_name_plural = "Departments"

    def __str__(self):
        return str(self.department)

class Program(models.Model):
    program = models.CharField(max_length=200)
    department = models.ForeignKey(Department, default=1, verbose_name="Department", on_delete=models.SET_DEFAULT)
    length = models.IntegerField()

    class Meta:
        verbose_name_plural = "Programs"

    def __str__(self):
        return str(self.program)

class Level(models.Model):
    level = models.CharField(max_length=10)
    year = models.DateTimeField(default=datetime.now())

    class Meta:
        verbose_name_plural = "Levels"

    def __str__(self):
        return str(self.level)

class Status(models.Model):
    status = models.CharField(max_length=10)

    class Meta:
        verbose_name_plural = "Status"

    def __str__(self):
        return str(self.status)

class Course(models.Model):
    code = models.CharField(max_length=6)
    title = models.CharField(max_length=60)
    status = models.ManyToManyField(Status)
    load = models.IntegerField()

    class Meta:
        verbose_name_plural = "Courses"

    def __str__(self):
        return str(self.code)

class Semester(models.Model):
    SEMESTER = (
            (1, 'First'),
            (2, 'Second'),
            (3, 'Resit'),
    )
    semester = models.CharField(max_length=20, null=True, choices=SEMESTER)
    text = models.CharField(max_length=50)
    level = models.ForeignKey(Level, default=1, verbose_name="Level", on_delete=models.SET_DEFAULT)
    gradepoint = models.FloatField(default=0.0)

    class Meta:
        verbose_name_plural = "Semesters"

    def __str__(self):
        return str(self.text)+" Semester"

class Result(models.Model):
    semester = models.ForeignKey(Semester, default=1, verbose_name="Semester", on_delete=models.SET_DEFAULT)
    level = models.ForeignKey(Level, default=1, verbose_name="Level", on_delete=models.SET_DEFAULT)
    course = models.ForeignKey(Course, default=1, verbose_name="Course", on_delete=models.SET_DEFAULT)
    assessment = models.IntegerField()
    exam = models.IntegerField()

    class Meta:
        verbose_name_plural = "Results"

    def __str__(self):
        return str(self.semester) +" "+ str(self.level)

class Honour(models.Model):
    honour = models.CharField(max_length=60)

    class Meta:
        verbose_name_plural = "Honours"

    def __str__(self):
        return str(self.honour)

class Profile(models.Model):
    base_user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    #firstname = models.CharField(max_length=50)
    #lastname = models.CharField(max_length=50)
    title = models.ForeignKey(Title, default=1, verbose_name="Title", on_delete=models.SET_DEFAULT)

    class Meta:
        verbose_name_plural = "Profiles"

    def __str__(self):
        fullname = str(self.base_user.first_name)+" "+str(self.base_user.last_name)
        return fullname

class Student(Profile):
    STATUS = (
            ('current', 'Current'),
            ('former', 'Former'),
            ('suspended', 'Suspended'),
    )
    matricule = models.CharField(max_length=50)
    program = models.ForeignKey(Program, default=1, verbose_name="Program", on_delete=models.SET_DEFAULT)
    status = models.CharField(max_length=20, null=True, choices=STATUS)
    gpa = models.FloatField(default=0.00)

    class Meta:
        verbose_name_plural = "Students"

    def __str__(self):
        return self.matricule

class Employee(Profile):
    STATUS = (
        ('active', 'Active'),
        ('suspended', 'Suspended'),
        ('leave', 'On Leave'),
        ('retired', 'Retired'),
        ('fired', 'Fired'),
        ('transferred', 'Transferred'),
    )
    salary = models.IntegerField()
    hire_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=STATUS)

    class Meta:
        verbose_name_plural = "Employees"

    def __str__(self):
        fullname = str(self.base_user.first_name)+" "+str(self.base_user.last_name)
        return "Employee: " + fullname

class Teacher(Employee):
    courses = models.ManyToManyField(Course)

    class Meta:
        verbose_name_plural = "Teachers"

    def __str__(self):
        fullname = str(self.base_user.first_name)+" "+str(self.base_user.last_name)
        return "Teacher: " + fullname

class Staff(Employee):
    role = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Staff"

    def __str__(self):
        fullname = str(self.base_user.first_name)+" "+str(self.base_user.last_name)
        return "Staff: " + fullname

class Administrator(Employee):
    role = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Administrators"

    def __str__(self):
        fullname = str(self.base_user.first_name)+" "+str(self.base_user.last_name)
        return "Admin: " + fullname
