from django.db import models
from django.contrib.auth.models import User
from events_attendance.models import Event
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile pictures')
    bio = models.CharField(max_length=350)
    events = models.ForeignKey(Event, on_delete=models.CASCADE)

    def __str__(self):
        return '{self.user.username} Profile'

    def save(self):
        super().save()

        image = Image.open(self.image.path)

        if image.height > 200 or image.width > 200:
            output_size = (200, 200)
            image.thumbnail(output_size)
            image.save(self.image.path)



