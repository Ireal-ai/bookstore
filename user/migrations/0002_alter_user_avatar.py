# Generated by Django 4.1.4 on 2022-12-21 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Your avatar'),
        ),
    ]
