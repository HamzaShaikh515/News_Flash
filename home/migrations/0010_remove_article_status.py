# Generated by Django 5.0.3 on 2024-03-29 17:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_status_article_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='status',
        ),
    ]
