from django.db import models


# Create your models here.


class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email_address = models.EmailField(max_length=50)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


class Tag(models.Model):
    caption = models.CharField(max_length=15)

    def __str__(self) -> str:
        return f"{self.caption}"


class Post(models.Model):
    title = models.CharField(max_length=80)
    excerpt = models.TextField(max_length=200)
    content = models.TextField()
    date = models.DateField()
    image = models.CharField(max_length=50, null=True, blank=True)
    slug = models.SlugField(
        default="", unique=True, blank=True, null=False, db_index=True
    )
    author = models.ForeignKey(
        Author, on_delete=models.SET_NULL, null=True, related_name="posts"
    )
    tags = models.ManyToManyField(Tag, blank=True, related_name="tags")

    def __str__(self) -> str:
        return f"{self.title}"
