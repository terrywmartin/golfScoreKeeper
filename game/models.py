from django.db import models
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.conf import settings

from core.tasks import email_user, email_user_sync
from course.models import Course, Hole, Hazard
from users.models import User

import uuid

# Create your models here.
class Round(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True,primary_key=True)
    user = models.ForeignKey(User, related_name="owner", on_delete=models.SET_NULL, null=True, blank=True)
    course = models.ForeignKey(Course, related_name="course", on_delete=models.CASCADE, null=True, blank=True)
    golfers = models.ManyToManyField(User, related_name="rounds")
    played = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.course + " - " + str(self.created_at)
    
class RoundInvitation(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True,primary_key=True)
    from_user = models.ForeignKey(User, related_name="from_user", on_delete=models.CASCADE, null=True, blank=True)
    to_user = models.ForeignKey(User, related_name="to_user", on_delete=models.CASCADE, null=True, blank=True)
    round = models.ForeignKey(Round, related_name="round", on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def send_activation(self):

      html = render_to_string('emails/invite_user.html', {
        'user': self.first_name,
         'domain': settings.APP_URL,
         'app_name': settings.APP_NAME,
         'uid': urlsafe_base64_encode(force_bytes(self.id)),
         'token': default_token_generator.make_token(self),
         'debug': settings.DEBUG,
      })
      
      response = email_user_sync(self.email, html, subject="Activate account")

    def __str__(self):
        return "Invitation from " + self.user.email


class ScoreCard(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True,primary_key=True)
    user = models.ForeignKey(User, related_name="score_cards", on_delete=models.SET_NULL, null=True, blank=True)
    round = models.ForeignKey(Round, related_name="score_card", on_delete=models.CASCADE, null=True, blank=True)
    score = models.IntegerField(default=0, null=True, blank=True)
    starting_hole = models.IntegerField(default=1, null=True, blank=True)
    current_hole = models.IntegerField(null=True,blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Score card for " + self.round
    
class Stroke(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True,primary_key=True)
    stroke = models.IntegerField(blank=False, null=False)
    user = models.ForeignKey(User, related_name="strokes+", on_delete=models.SET_NULL, null=True, blank=True)
    hole = models.ForeignKey(Hole, related_name="strokes+", on_delete=models.SET_NULL, null=True, blank=True)
    score_card = models.ForeignKey(ScoreCard, related_name="stroke", on_delete=models.SET_NULL, null=True, blank=True)
    longitude = models.DecimalField(blank=True, null=True, decimal_places=3, max_digits=6)
    latitude = models.DecimalField(blank=True, null=True, decimal_places=3, max_digits=6)
    hazard = models.ForeignKey(Hazard, related_name="strokes",on_delete=models.SET_NULL, null=True,blank=True)
    in_rough = models.BooleanField(default=False, null=True, blank=True)
    out_of_bounds = models.BooleanField(default=False, null=True, blank=True)
    club = models.CharField(max_length=15, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 

class HoleStroke(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True,primary_key=True)
    strokes = models.IntegerField(default=0, blank=True, null=True)
    hole = models.ForeignKey(Hole, related_name="strokes",on_delete=models.SET_NULL, null=True, blank=True)
    score_card = models.ForeignKey(ScoreCard, related_name="strokes", on_delete=models.SET_NULL, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Hole " + self.hole.hole + ": " + str(self.strokes)
