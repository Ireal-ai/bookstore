# Generated by Django 4.1.4 on 2022-12-16 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_reporter_article'),
    ]

    operations = [
        migrations.AddField(
            model_name='reporter',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
