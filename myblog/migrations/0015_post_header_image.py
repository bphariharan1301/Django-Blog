# Generated by Django 3.1.3 on 2020-11-29 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0014_post_snippet'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='header_image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
