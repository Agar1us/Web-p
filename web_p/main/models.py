from django.contrib.auth.models import User
from django.db import models


class Proj(models.Model):
    header = models.CharField(max_length=100)
    decription = models.TextField()
    creator = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="creator")
    members = models.ManyToManyField(User, related_name="team", through='MembershipProject', through_fields=('proj', 'user'),)
    date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.header


class Task(models.Model):
    header = models.CharField(max_length=100)
    description = models.TextField()
    members = models.ManyToManyField(User, through='MembershipTask', through_fields=('task', 'user'), )
    date = models.DateTimeField(auto_now_add=True)
    proj = models.ForeignKey(to=Proj, on_delete=models.CASCADE)

    def __str__(self):
        return self.header

class MembershipProject(models.Model):
    proj = models.ForeignKey(Proj, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    inviter = models.ForeignKey(User, on_delete=models.CASCADE, related_name="membership_invites",)


class MembershipTask(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class TaskFile(models.Model):
    file = models.FileField(upload_to='files/')
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
