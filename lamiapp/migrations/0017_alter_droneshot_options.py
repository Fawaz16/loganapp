# Generated by Django 4.0.4 on 2022-07-20 17:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lamiapp', '0016_droneshot'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='droneshot',
            options={'ordering': ['-id']},
        ),
    ]
