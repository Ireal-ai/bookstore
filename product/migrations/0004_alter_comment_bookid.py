# Generated by Django 4.1.4 on 2022-12-16 13:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_remove_book_comment_alter_comment_bookid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='bookId',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.book', verbose_name='book id'),
        ),
    ]
