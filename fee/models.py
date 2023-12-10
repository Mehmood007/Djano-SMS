from django.db import models

from student.models import Student


class Fee(models.Model):
    amount = models.IntegerField()
    f_type = models.CharField(max_length=14)
    applies_scholarship = models.BooleanField()

    def __str__(self):
        return f"{self.f_type} scholarship applied={self.applies_scholarship}"


class StudentFee(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    fee = models.ForeignKey(Fee, on_delete=models.CASCADE)
    amount = models.IntegerField()
    payment_date = models.DateField()

    def __str__(self):
        return f"{self.amount} payment_date={self.payment_date}"
