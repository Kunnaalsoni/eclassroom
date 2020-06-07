from django.db import models


# Create your models here.
class Subjects(models.Model):
    subjects_names = models.CharField(max_length=64)

    def __str__(self):
        return self.subjects_names


class Classrooms(models.Model):
    classroom_names = models.CharField(max_length=25)

    def __str__(self):
        return self.classroom_names


class ClassContent(models.Model):
    classroom = models.ForeignKey(Classrooms, on_delete=models.CASCADE)
    subjects = models.ForeignKey(Subjects, on_delete=models.CASCADE)
    date = models.DateField()
    video_url = models.URLField()
    notes_url = models.URLField()
