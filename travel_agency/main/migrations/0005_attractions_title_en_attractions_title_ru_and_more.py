# Generated by Django 4.0.4 on 2022-05-31 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_attractions_alter_city_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='attractions',
            name='title_en',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='attractions',
            name='title_ru',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='attractions',
            name='title_tr',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='attractions',
            name='title_uz',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='city',
            name='name_en',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='city',
            name='name_ru',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='city',
            name='name_tr',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='city',
            name='name_uz',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='gallery',
            name='title_en',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='gallery',
            name='title_ru',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='gallery',
            name='title_tr',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='gallery',
            name='title_uz',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
