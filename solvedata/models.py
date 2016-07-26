from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class MyUser(models.Model):
	user = models.OneToOneField(User)
	class Meta:
		app_label='solvedata'
		permissions = (
			("solve_data", "Can solve data"),
		)
