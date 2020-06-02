from django.test import TestCase
from .models import Author, Image, tags


# Create your tests here.
class AuthorTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.moha= Author (first_name = 'Mohamed', last_name ='Mohamed', email ='moha@moha.com')

    def test_instance(self):
        self.assertTrue(isinstance(self.moha,Author))

        # Testing Save Method
    def test_save_method(self):
        self.moha.save_author()
        authors = Author.objects.all()
        self.assertTrue(len(authors) > 0)

class ImageTestClass(TestCase):
    