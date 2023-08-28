from django.db import models
from django.utils import timezone
# Create your models here.


class Todo(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    is_completed = models.BooleanField(default=False)
    deadline = models.PositiveIntegerField(default=5)
    # New field to store the is_expired property value
    is_expired = models.BooleanField(default=False)

    @property
    def if_expired(self):
        return timezone.now() > self.created_at + timezone.timedelta(minutes=self.deadline)

    def publish(self):
        if self.if_expired and not self.is_expired:
            self.is_expired = True
            self.save()

    def __str__(self):
        return self.name


class Magento(models.Model):
    email = models.EmailField(unique=True)
    phone = models.IntegerField(unique=True)

    def __str__(self):
        return self.name
