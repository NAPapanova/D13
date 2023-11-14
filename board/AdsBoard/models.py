from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.db.models import Sum

class User(AbstractUser):
    email = models.EmailField(
        ('email address'),
        unique=True,
    )
    email_verify = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

class Author(models.Model):
    authorUser = models.OneToOneField(User, on_delete = models.CASCADE)

    def update_replies(self):
        adsRep = self.post_set.all().aggregate(postRating=Sum('Replies'))
        aRep = 0
        aRep += adsRep.get('adsReplies')

        self.save()   

class Ads(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ManyToManyField('Category', through='AdsCategory')
    title = models.CharField(max_length=30)
    discription = models.TextField()
    replies = models.SmallIntegerField(default=0)

    
    time_create = models.DateTimeField(auto_now_add=True)
    actuality = models.BooleanField(default=True)

    TANKS = 'TNKS'
    HEALS = 'HLS'
    DD = 'DD'
    SAILERS = 'SL'
    GUILDMASTERS = 'GDMSTR'
    KWESTGIVER = 'KWG'
    BLACKSMITH = 'BLKSMTH'
    TANNER = 'TN'
    POTIONBREWERS = 'PB'
    SPELLSMASTER = 'SM'
    
    CATEGORY_CHOICES = (
        (TANKS,'Танки'),
        (HEALS,'Хилы'),
        (DD,'ДД'),
        (SAILERS,'Торговцы'),
        (GUILDMASTERS,'Гилдмастеры'),
        (KWESTGIVER,'Квестгиверы'),
        (BLACKSMITH,'Кузнецы'),
        (TANNER,'Кожевники'),
        (POTIONBREWERS,'Зельевары'),
        (SPELLSMASTER,'Мастера заклинаний'),
    )
    categoryType = models.CharField(max_length=2, choices=CATEGORY_CHOICES, default=TANKS)

    def __str__(self):
        return f'{self.title}-{self.author}'

    def get_absolute_url(self):
        return reverse('post', args=[str(self.id)])

    def reply(self):
        self.replies += 1
        return self.reply_text[0:50] + '...'
    
class Reply(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reply_text = models.TextField()
    post = models.ForeignKey(Ads, on_delete=models.CASCADE, related_name='replies')


class Category(models.Model):
    name = models.CharField(max_length=15)

    def __str__(self):
        return self.name


class AdsCategory(models.Model):
    advertisement = models.ForeignKey(Ads, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class OneTimeCode(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    code = models.CharField(max_length=6)