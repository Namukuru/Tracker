# Generated by Django 5.0.3 on 2024-03-16 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_remove_category_user_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='category',
            field=models.CharField(max_length=200),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]