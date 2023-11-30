from django.core.exceptions import ValidationError
from django.db import models


class Musician(models.Model):
    first_name = models.CharField(max_length=63)
    last_name = models.CharField(max_length=63)
    instrument = models.CharField(max_length=63)
    age = models.IntegerField()
    date_of_applying = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def clean(self):
        if not self.age >= 14:
            raise ValidationError(
                {
                    "age": "We do not accept people under 14"
                }
            )

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        self.full_clean()
        return super(Musician, self).save(force_insert, force_update, using, update_fields)