# Generated by Django 5.2 on 2025-05-01 14:38

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_post_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='author',
            name='email_address',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='author',
            name='first_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='author',
            name='last_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='posts', to='blog.author'),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(validators=[django.core.validators.MinLengthValidator(10)]),
        ),
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='excerpt',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='post',
            name='image_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(blank=True, default='', unique=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=150),
        ),
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(to='blog.tag'),
        ),
    ]
