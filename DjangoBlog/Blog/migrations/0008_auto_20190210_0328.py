# Generated by Django 2.1.5 on 2019-02-10 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0007_auto_20190207_0407'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='post_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
