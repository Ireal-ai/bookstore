# Generated by Django 4.1.4 on 2022-12-26 07:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0020_alter_comment_userid_alter_genre_userid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Comment date'),
        ),
    ]
