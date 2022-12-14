# Generated by Django 4.1.4 on 2022-12-22 08:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0018_alter_book_cover'),
        ('user', '0005_user_groups_user_is_superuser_user_user_permissions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='comments',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_id', to='product.comment'),
        ),
        migrations.AlterField(
            model_name='user',
            name='ratings',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_id', to='product.rating'),
        ),
    ]
