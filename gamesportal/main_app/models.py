from django.db import models
from django.utils.text import slugify 
from django.contrib.auth import get_user_model

from django.db.models import IntegerField, Model
from django.core.validators import MaxValueValidator, MinValueValidator

User = get_user_model()



# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Game(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(default="")

    description = models.TextField(blank=True)
    release_date = models.DateField()

    cover_image = models.ImageField(upload_to='gamecovers/', blank=True, default="gamecovers/No_Cover_Image.png")

    tags = models.ManyToManyField(to=Tag, related_name='tagged_games')

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Game, self).save(*args, **kwargs)

    
class GameList(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(default="")
    description = models.TextField(blank=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    games = models.ManyToManyField(to=Game, related_name='game_lists')

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(GameList, self).save(*args, **kwargs)


class Review(models.Model):
    body = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    likes = models.PositiveIntegerField()
    dislikes = models.PositiveIntegerField()
    score = models.IntegerField( default=0,
        validators=[
            MaxValueValidator(100),
            MinValueValidator(0)
        ])

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)