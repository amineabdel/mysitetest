from django.db import models


class Author(models.Model):
    author_name = models.CharField(max_length=50)

    def __str__(self):
        return self.author_name

class Quote(models.Model):
    quote_text = models.CharField(max_length=300)
    quote_author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.quote_text
     

    