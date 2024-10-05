from django.db import models
import uuid
from django.contrib.auth.models import User

# Create your models here.

class BaseModel(models.Model):
	uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	created_date=models.DateTimeField(auto_now_add=True)
	updated_date=models.DateTimeField(auto_now_add=True)

	class Meta:
		abstract=True

class Note(BaseModel):
	user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="notes")
	title=models.CharField(max_length=200)
	content=models.TextField()
	is_archieved=models.BooleanField(default=False)
	PRIORITY_CHOICES = [
		('Low', 'Low'),
		('Medium', 'Medium'),
		('High', 'High'),
	]
	priority=models.CharField(max_length=6,choices=PRIORITY_CHOICES,default='Medium')
	attchment=models.FileField(upload_to="attachments/",blank=True,null=True)

	def __str__(self):
		return self.title

