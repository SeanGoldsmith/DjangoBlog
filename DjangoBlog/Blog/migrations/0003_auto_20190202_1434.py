# Generated by Django 2.1.5 on 2019-02-02 22:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0002_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='blog_post_id',
            new_name='blog_post',
        ),
    ]
