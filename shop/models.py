from django.db import models



class Person(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    age = models.PositiveSmallIntegerField(default=10, null=True, blank=True)


    class Meta():
        db_table = "people"
        verbose_name_plural = "people"


    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    @property
    def is_adult(self):
        return self.age >= 18
    
    def __str__(self):
        return self.full_name
