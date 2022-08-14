from django.db import models


class Article(models.Model):

    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title


class Scope(models.Model):
    name = models.CharField(max_length=80)
    articles = models.ManyToManyField(Article, related_name='scopes', through='ScopeArticle')

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return self.name


class ScopeArticle(models.Model):
    article = models.ForeignKey(Article, related_name='scope_article', on_delete=models.CASCADE)
    scope = models.ForeignKey(Scope, related_name='scope_article', on_delete=models.CASCADE)
    is_main = models.BooleanField()
