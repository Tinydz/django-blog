from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
	user = models.OneToOneField(User)
	email = models.EmailField(blank=True, null=True)
	qq = models.CharField(max_length=20, blank=True, null=True)
	telnum = models.CharField(max_length=15, blank=True, null=True)

	def __str__(self):
		return self.user.username

