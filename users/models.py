from django.db import models
from django.contrib.auth.models import User
from events_attendance.models import Event
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='photo_1440-09-28_06.40.24.jpeg.jpg', upload_to='profile pictures')
    bio = models.CharField(max_length=350)
    events = models.ForeignKey(Event, on_delete=models.CASCADE)

    def __str__(self):
        return '{self.user.username} Profile'

    def save(self):
        super().save()

        image = Image.open(self.image.path)

        if image.height > 300 or image.width > 300:
            output_size = (200, 200)
            image.thumbnail(output_size)
            image.save(self.image.path)
class CV(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birth_day = models.DateTimeField()
    volunteer_work = models.CharField(max_length=350)
    professional_associations = models.CharField(max_length=350)
    skills = models.CharField(max_length=350)





