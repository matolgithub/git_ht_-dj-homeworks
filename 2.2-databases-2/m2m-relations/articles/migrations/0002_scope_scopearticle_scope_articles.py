# Generated by Django 4.1 on 2022-08-14 12:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Scope',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
            ],
            options={
                'verbose_name': 'Тег',
                'verbose_name_plural': 'Теги',
            },
        ),
        migrations.CreateModel(
            name='ScopeArticle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_main', models.BooleanField()),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scope_article', to='articles.article')),
                ('scope', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scope_article', to='articles.scope')),
            ],
        ),
        migrations.AddField(
            model_name='scope',
            name='articles',
            field=models.ManyToManyField(related_name='scopes', through='articles.ScopeArticle', to='articles.article'),
        ),
    ]