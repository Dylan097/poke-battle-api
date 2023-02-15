from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.contrib.auth.models import User


class Pokemon(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.TextField()
    caught = models.DateTimeField(auto_now_add=True)
    sprite_front = models.ImageField(
        upload_to='images/'
    )
    sprite_back = models.ImageField(
        upload_to='images/'
    )
    nickname = models.CharField(max_length=25, blank=True)
    evolve_from = models.IntegerField(blank=True)
    active = models.BooleanField(default=True)
    pokedex_index = models.IntegerField()
    moveset = ArrayField(
        models.TextField(),
        size=4
    )
    level = models.IntegerField()
    stats = ArrayField(
        models.IntegerField(),
        size=6
    )

    class Meta:
        ordering = ['-pokedex_index']

    def __str__(self):
        return f"{self.owner}'s {self.name}"
