from django.db import models
from organize.models import User



class Poll(models.Model):

    subject = models.TextField(null=True, blank=True)
    detail = models.TextField(null=True, blank=True)
    # picture = models.models.ImageField(_(""), upload_to=None, height_field=None, width_field=None, max_length=None)
    start_date = models.DateField(auto_now=False, auto_now_add=True)
    start_time = models.TimeField(auto_now=True,null=True)
    end_date = models.DateField(auto_now=False, auto_now_add=False)
    end_time = models.TimeField(auto_now=False,null=True)
    password = models.CharField(max_length=10)
    create_by = models.CharField(max_length=50)
    create_date = models.DateField(auto_now=True)
    create_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

class Pollchoice(models.Model):
    poll_choice_id = models.IntegerField(primary_key=True)
    subject = models.CharField(max_length=50)
    # image = models.models.ImageField(_(""), upload_to=None, height_field=None, width_field=None, max_length=None)
    polls = models.ManyToManyField(Poll)

class Pollvote(models.Model):
    vote_id = models.IntegerField(primary_key=True)
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, null=True)
    poll_choice = models.ForeignKey(Pollchoice, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

