# Generated by Django 4.0.3 on 2022-03-28 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0004_alter_image_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to='articles/'),
        ),
    ]