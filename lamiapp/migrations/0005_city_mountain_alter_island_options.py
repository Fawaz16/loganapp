# Generated by Django 4.0.4 on 2022-06-22 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lamiapp', '0004_island'),
    ]

    operations = [
        migrations.CreateModel(
            name='city',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='blog_image')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='mountain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='blog_image')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.AlterModelOptions(
            name='island',
            options={'ordering': ['-id']},
        ),
    ]
