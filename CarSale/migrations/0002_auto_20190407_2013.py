# Generated by Django 2.2 on 2019-04-07 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CarSale', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='', upload_to='image/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='text_opis',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
