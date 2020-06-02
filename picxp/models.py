from django.db import models
import datetime as dt

class Location(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()


class Category(models.Model):
    name = models.CharField(max_length = 30 )

    def __str__(self):
        return self.name

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()


class Image(models.Model):
    image = models.ImageField(upload_to = 'images/')
    name = models.CharField(max_length =60)
    description = models.TextField()
    location = models.ForeignKey(Location)
    category = models.ForeignKey(Category)
    pub_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

    @classmethod
    def all_pics(cls):
        today = dt.date.today()
        pics = cls.objects.filter(pub_date__date = today)
        return pics

    @classmethod
    def search_by_category(cls,search_term):
        pics = cls.objects.filter(title__icontains=search_term)
        return pics

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    # def update_image(self):

    # def get_image_by_id(id):

    # def search_image(category):

    # def filter_by_location(location):