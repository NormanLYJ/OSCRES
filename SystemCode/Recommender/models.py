from django.db import models

class Student(models.Model):
    id = models.AutoField(primary_key=True)
    region =  models.CharField(max_length=50, default="none")
    country =  models.CharField(max_length=50, default="none")
    academic_reputation_rank = models.CharField(max_length=50, default="none")
    employer_reputation_rank = models.CharField(max_length=50, default="none")
    faculty_student_rank = models.CharField(max_length=50, default="none")
    international_faculty_rank = models.CharField(max_length=50, default="none")
    international_student_rank = models.CharField(max_length=50, default="none")
    citation_rank = models.CharField(max_length=50, default="none")
    ielts = models.CharField(max_length=50, default="none")
    toefl = models.CharField(max_length=50, default="none")
    work_study = models.CharField(max_length=50, default="none")
    min_tution_fee = models.CharField(max_length=50, default="none")
    max_tution_fee = models.CharField(max_length=50, default="none")
    international_student_percentage = models.CharField(max_length=50, default="none")
    cost_index = models.CharField(max_length=50, default="none")
    math = models.CharField(max_length=50, default="none")
    chinese = models.CharField(max_length=50, default="none")
    english = models.CharField(max_length=50, default="none")
    physics = models.CharField(max_length=50, default="none")
    chemistry = models.CharField(max_length=50, default="none")
    biology = models.CharField(max_length=50, default="none")
    history = models.CharField(max_length=50, default="none")
    geogrophy = models.CharField(max_length=50, default="none")
    politics = models.CharField(max_length=50, default="none")
    art = models.CharField(max_length=50, default="none")


class University_Course(models.Model):
    id = models.PositiveSmallIntegerField(primary_key=True)
    name = models.CharField(max_length=50, default="unknown")
    country = models.CharField(max_length=20, default="unknown")
    population_size = models.CharField(max_length=20, default="unknown")
    age = models.PositiveSmallIntegerField(default = 0)
    status = models.CharField(max_length=20, default="unknown")
    academic_reputation_score = models.FloatField(max_length=20, default=0.0)
    academic_reputation_rank = models.PositiveSmallIntegerField(default = 0)
    employer_reputation_score = models.FloatField(max_length=20, default=0.0)
    employer_reputation_rank = models.PositiveSmallIntegerField(default = 0)
    faculty_student_score = models.FloatField(max_length=20, default=0.0)
    faculty_student_rank = models.PositiveSmallIntegerField(default = 0)
    citation_score = models.FloatField(max_length=20, default=0.0)
    citation_rank = models.PositiveSmallIntegerField(default = 0)
    international_faculty_score	= models.FloatField(max_length=20, default=0.0)
    international_faculty_rank = models.PositiveSmallIntegerField(default = 0)
    international_student_score	= models.FloatField(max_length=20, default=0.0)
    international_student_rank = models.PositiveSmallIntegerField(default = 0)
    overall_score = models.FloatField(max_length=20, default=0.0)
    city = models.CharField(max_length=20, default="unknown")
    region = models.CharField(max_length=20, default="unknown")
    cost_of_living_index = models.FloatField(max_length=20, default=0.0)
    international_student_percentage = models.FloatField(max_length=20, default=0.0)
    field_of_study = models.CharField(max_length=20, default="unknown")
    subject = models.CharField(max_length=50, default="unknown")
    program_name = models.CharField(max_length=20, default="unknown")
    min_IELTS = models.FloatField(max_length=20, default=0.0)	
    min_TOEFL = models.FloatField(max_length=20, default=0.0)
    min_GPA	= models.CharField(max_length=20, default="unknown")
    campus_setting = models.CharField(max_length=20, default="unknown")
    offer_work_study_program = models.BooleanField(default=False)
    average_tuition_fee = models.PositiveIntegerField(default = 0)
    offer_airport_pickup = models.BooleanField(default=False)
    acceptance_rate = models.FloatField(max_length=20, default=0.0)


class Country(models.Model):
    name = models.CharField(max_length=50)

