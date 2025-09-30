from django.db import models
from django.contrib.auth.models import User

class Petition(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="petitions")
    created_at = models.DateTimeField(auto_now_add=True)

    def yes_votes(self):
        return self.votes.filter(value=True).count()

    def no_votes(self):
        return self.votes.filter(value=False).count()

    def __str__(self):
        return f"{self.title} (by {self.created_by.username})"


class PetitionVote(models.Model):
    petition = models.ForeignKey(Petition, on_delete=models.CASCADE, related_name="votes")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    value = models.BooleanField()  # True = Yes, False = No
    voted_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('petition', 'user')  # one vote per user per petition

    def __str__(self):
        return f"{self.user.username} voted {'Yes' if self.value else 'No'} on {self.petition.title}"
