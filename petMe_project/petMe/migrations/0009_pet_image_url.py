# Generated by Django 4.1 on 2022-09-09 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petMe', '0008_remove_pet_image_url_species_image_url_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='pet',
            name='image_url',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
