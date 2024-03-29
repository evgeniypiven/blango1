# Generated by Django 3.2.6 on 2022-06-30 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True, verbose_name='Title')),
                ('summary', models.TextField(blank=True, verbose_name='Summary')),
                ('content', models.TextField(blank=True, verbose_name='Content')),
                ('slug', models.SlugField(unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Modified At')),
                ('published_at', models.DateTimeField(blank=True, null=True, verbose_name='Published At')),
            ],
        ),
    ]
