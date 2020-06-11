from django.db import models


class Location(models.Model):
    name = models.CharField(max_length =30)

    @classmethod
    def all_locations(cls):
        locations = Location.objects.all()
        return locations

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

    @classmethod
    def all_pics(cls):
        pics = Image.objects.all()
        return pics

    @classmethod
    def images_by_location(cls, location):
        pic_location = Image.objects.filter(Location)
        return pic_location

    @classmethod
    def search_category(cls,category):
        pics = cls.objects.filter(category__name__icontains=category)
        return pics

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    class Meta:
        ordering = ['name']

    # def update_image(self):

    # def get_image_by_id(id):

    # def search_image(category):

    # def filter_by_location(location):