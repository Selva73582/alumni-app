from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bloodGroup=models.CharField(max_length=4,blank=True,null=True)
    contactNumber=models.CharField(max_length=20,null=True,blank=True)
    profilePicture=models.ImageField(upload_to='uploads/profile_pictures/',default='uploads/profile_pictures/photo_2023-12-23_15-24-37.jpg')
    city=models.CharField(max_length=256,null=True,blank=True)
    state=models.CharField(max_length=256,null=True,blank=True)
    country=models.CharField(max_length=256,null=True,blank=True)
    pincode=models.CharField(max_length=26,null=True,blank=True)
    
    
    
    def __str__(self):
        return self.user.username

    
class Experience(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    designation=models.CharField(max_length=256,blank=False,null=False)
    companyName=models.CharField(max_length=256,blank=False,null=False)
    FromDate=models.DateField(auto_now_add=False)
    EndDate = models.DateField(auto_now_add=False)

    def __str__(self):
        return self.user.username + " "+ self.designation


class Certifications(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Add a ForeignKey field for the user
    skill = models.CharField(max_length=256, blank=False, null=False)
    credentialId = models.CharField(max_length=126, blank=True, null=True)
    CertificateUrl = models.CharField(max_length=512, blank=True, null=True)
    certificate = models.FileField(upload_to='uploads/certificates/', null=True)
    organisationName = models.CharField(max_length=256)
    description = models.TextField(max_length=1000)
    dateOfCertification = models.DateField()






class Posting(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    image = models.ImageField(upload_to='post_images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
class UserFollow(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    following = models.ManyToManyField(User,related_name="followers")
    followers = models.ManyToManyField(User,related_name= "is_following",blank=True)

    def __str__(self):
        return self.user.username