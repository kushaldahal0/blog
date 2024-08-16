from django.db import models


class Contact(models.Model):
  c_no = models.AutoField(primary_key=True)
  Name = models.CharField(max_length=50)
  Phone = models.CharField(max_length=14)
  Email = models.CharField(max_length=50)
  Enquiry = models.TextField()

  def __str__(self):
    return f'{self.c_no}. {self.Name}'
