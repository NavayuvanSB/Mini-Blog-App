# Generated by Django 3.2 on 2021-04-08 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20210408_1552'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='post_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Posted Date'),
        ),
    ]
