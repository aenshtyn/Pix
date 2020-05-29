from django.db import models
import datetime as dt

# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length =30)
    last_name = models.CharField(max_length =30)
    email = models.EmailField()

    def __str__(self):
        return self.first_name

    
    class Meta:
        ordering = ['first_name']

    def save_author(self):
        self.save()


class tags(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name


class Picture(models.Model):
    title = models.CharField(max_length =60)
    post = models.TextField()
    author = models.ForeignKey(Author)
    tags = models.ManyToManyField(tags)
    pub_date = models.DateTimeField(auto_now_add=True)
    picture_image = models.ImageField(upload_to= 'pictures/' )

    def __str__(self):
        return self.title

    @classmethod
    def pics_new(cls):
        today = dt.date.today()
        pics = cls.objects.filter(pub_date__date = today)
        return pics