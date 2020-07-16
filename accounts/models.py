from django.db import models

# Create your models here.

class Projects(models.Model):
	TYPES=(('Maintanace','Maintanace'),('Security','Security'),('Research','Research')

		)
	name=models.CharField(max_length=200,null=True)
	ProjectType=models.CharField(max_length=200,null=True,choices=TYPES)
	manager=models.CharField(max_length=200,null=True)
	frontend=models.CharField(max_length=200,null=True)
	backend=models.CharField(max_length=200,null=True)
	client_name=models.CharField(max_length=200,null=True)
	Description=models.CharField(max_length=500,null=True)
	start_date=models.DateTimeField(null=True)
	due_date=models.DateTimeField(null=True)

	def __str__(self):
		return self.name
class ProjectBug(models.Model):
	TYPES=(('High','High'),('Medium','Medium'),('Low','Low'))
	name=models.CharField(max_length=200,null=True)
	project=models.ForeignKey(Projects,null=True,on_delete=models.SET_NULL)
	bug_description=models.CharField(max_length=1000,null=True)
	priority=models.CharField(max_length=200,null=True,choices=TYPES)

	def __str__(self):
		return self.name

