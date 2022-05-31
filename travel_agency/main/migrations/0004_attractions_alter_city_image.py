# Generated by Django 4.0.4 on 2022-05-31 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20220530_2031'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attractions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='attraction_images')),
            ],
        ),
        migrations.AlterField(
            model_name='city',
            name='image',
            field=models.ImageField(upload_to='city_images/'),
        ),
    ]