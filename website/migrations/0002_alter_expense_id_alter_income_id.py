# Generated by Django 5.0.3 on 2024-03-23 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='income',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]