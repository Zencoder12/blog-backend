from django.db import models
from django.utils import timezone
from django.conf import settings


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name


class Post(models.Model):

    class PostObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status="published")

    options = (
        ('draft', 'Draft'),
        ('published', 'Published')
    )

    category = models.ForeignKey(
        Category, on_delete=models.PROTECT, default=1)
    title = models.CharField(max_length=250)
    excerpt = models.TextField(max_length=250, null=True)
    content = models.TextField(max_length=1024)
    # because we using the unique_for_date attribute, we can use it as the main identifier for Posts
    slug = models.SlugField(max_length=250, unique_for_date='published')
    published = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='blog_posts', default=1)
    status = models.CharField(
        max_length=10, choices=options, default='published')

    # give possibility to define queries outside the Post model class
    objects = models.Manager()  # default manager
    published_objects = PostObjects()  # custom manager

    class Meta:
        ordering = ('-published',)

    def __str__(self) -> str:
        return self.title
