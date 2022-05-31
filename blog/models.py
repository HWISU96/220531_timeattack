from django.db import models

# Create your models here.

class Category(models.Model):
    class Meta:
        db_table = "category"

    category_title = models.CharField(max_length=20, null=False)
    category_explain = models.CharField(max_length=256, null=False)


class Article(models.Model):
    class Meta:
        db_table = "article"

    article_title = models.CharField(max_length=20, null=False)
    article_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    article_content = models.CharField(max_length=256, default='')