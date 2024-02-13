from django.db import models


class Message(models.Model):
    message_from = models.CharField(max_length=100)
    message_to = models.CharField(max_length=100)
    message_content = models.TextField()
    response_content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
     
 
    def __str__(self):
        return self.message_content
    
    class Meta:
        db_table = "penzi_message"

class Users(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    county = models.CharField(max_length=255)
    town = models.CharField(max_length=255)
    level_of_education = models.CharField(max_length=255, blank=True, null=True)
    profession = models.CharField(max_length=255, blank=True, null=True)
    marital_status = models.CharField(max_length=50, blank=True, null=True)
    religion = models.CharField(max_length=50, blank=True, null=True)
    ethnicity = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField()
    myself = models.TextField
    msisdn = models.IntegerField()
    registration_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "penzi_users"