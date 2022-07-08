# Generated by Django 4.0.4 on 2022-06-19 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lamiapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='main_page_pic',
            options={'ordering': ['-id']},
        ),
        migrations.RenameField(
            model_name='main_page_pic',
            old_name='image',
            new_name='image1',
        ),
        migrations.AddField(
            model_name='main_page_pic',
            name='image10',
            field=models.ImageField(default=1, upload_to='blog_image'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='main_page_pic',
            name='image11',
            field=models.ImageField(default=1, upload_to='blog_image'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='main_page_pic',
            name='image2',
            field=models.ImageField(default=1, upload_to='blog_image'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='main_page_pic',
            name='image3',
            field=models.ImageField(default=1, upload_to='blog_image'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='main_page_pic',
            name='image4',
            field=models.ImageField(default=1, upload_to='blog_image'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='main_page_pic',
            name='image5',
            field=models.ImageField(default=1, upload_to='blog_image'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='main_page_pic',
            name='image6',
            field=models.ImageField(default=1, upload_to='blog_image'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='main_page_pic',
            name='image7',
            field=models.ImageField(default=1, upload_to='blog_image'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='main_page_pic',
            name='image8',
            field=models.ImageField(default=1, upload_to='blog_image'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='main_page_pic',
            name='image9',
            field=models.ImageField(default=1, upload_to='blog_image'),
            preserve_default=False,
        ),
    ]
