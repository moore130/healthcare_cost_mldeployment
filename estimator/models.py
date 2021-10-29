from django.db import models

class PredResults(models.Model):
    age = models.IntegerField()
    bmi = models.FloatField()
    children = models.IntegerField()
    sex_female = models.IntegerField()
    sex_male = models.IntegerField()
    smoke_no = models.IntegerField()
    smoke_yes = models.IntegerField()
    charges = models.FloatField()

    def __str__(self):
        return self.charges
