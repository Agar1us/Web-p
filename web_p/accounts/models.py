from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Avatar(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='avatars/', null=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 400 or img.width > 400:
            middle = min(img.height, img.width)
            new_img = img.crop(
                ((img.width - middle) // 2,
                 (img.height - middle) // 2,
                 img.width - (img.width - middle) // 2,
                 img.height - (img.height - middle) // 2))
            new_img = new_img.resize((400, 400))
            new_img.save(self.image.path)
