from django.db import models

class Operation(models.Model):
    first_number = models.FloatField()
    second_number = models.FloatField()
    operation = models.CharField(max_length=10)
    result = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.first_number} {self.operation} {self.second_number} = {self.result}'
