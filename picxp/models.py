from django.db import models
import datetime as dt

class location(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name

class category(models.Model):
    name = models.CharField(max_length = 30 )

    def __str__(self):
        return self.name

class Image(models.Model):
    image = models.ImageField(upload_to = 'images/')
    name = models.CharField(max_length =60)
    description = models.TextField()
    location = models.ManyToManyField(location)
    category = models.ManyToManyField(category)
    pub_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

    @classmethod
    def pics_new(cls):
        today = dt.date.today()
        pics = cls.objects.filter(pub_date__date = today)
        return pics

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    # def update_image(self):

    # def get_image_by_id(id):

    # def search_image(category):

    # def filter_by_location(location):