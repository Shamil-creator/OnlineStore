# Generated by Django 4.2.4 on 2023-08-24 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='color',
            field=models.CharField(default='white', max_length=255),
        ),
        migrations.AddField(
            model_name='product',
            name='storage',
            field=models.IntegerField(default=256),
        ),
    ]
