# Generated by Django 4.2.6 on 2023-10-08 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartdetail',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='cartdetail',
            name='total',
            field=models.FloatField(default=0),
        ),
    ]