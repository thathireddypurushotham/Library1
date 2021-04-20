from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver



# Create your models here.
class ComplaintBox(models.Model):
	p_name=models.CharField(max_length=120)
	p_email=models.EmailField(max_length=120)
	p_complaint=models.CharField(max_length=10000)
	#p_subject=models.CharField(max_length=100)
	#p_body=models.CharField(max_length=1000)

class ImProfile(models.Model):
	g=[('M',"male"),('F',"female")]
	age=models.IntegerField(default=10)
	impf=models.ImageField(upload_to='profiles/',default="profile.jpg")
	gender=models.CharField(max_length=20,choices=g)
	uid=models.OneToOneField(User,on_delete=models.CASCADE)


@receiver(post_save,sender=User)
def CreateProfile(sender,instance,created,**kwargs):
	if created:
		ImProfile.objects.create(uid=instance)