from django.contrib.auth.models import User
from django.db import models


class Project(models.Model):
    header = models.CharField(max_length=100)
    description = models.TextField()
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
    deadline = models.DateTimeField()
    proj = models.ForeignKey(to=Project, on_delete=models.CASCADE)

    def __str__(self):
        return self.header


class TaskFile(models.Model):
    file = models.FileField(upload_to='files/')
    task = models.ForeignKey(Task, on_delete=models.CASCADE)


class InviteProj(models.Model):
    proj = models.ForeignKey(to=Project, on_delete=models.CASCADE)
    from_user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='p_from_user')
    to_user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='p_to_user')


class MembershipProject(models.Model):
    proj = models.ForeignKey(Project, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class MembershipTask(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
