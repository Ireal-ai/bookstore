# Generated by Django 4.1.4 on 2022-12-19 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_alter_comment_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rating',
            old_name='book',
            new_name='bookId',
        ),
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=models.TextField(default='Test', max_length=900, verbose_name='Comment'),
        ),
    ]
