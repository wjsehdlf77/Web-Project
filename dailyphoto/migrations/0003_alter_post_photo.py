# Generated by Django 4.0.2 on 2022-02-09 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dailyphoto', '0002_post_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='photo',
            field=models.ImageField(blank=True, default=1, upload_to='pic'),
            preserve_default=False,
        ),
    ]
