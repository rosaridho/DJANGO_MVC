# Generated by Django 2.1.5 on 2019-02-11 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_as_app', '0003_mentee_nick_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mentee',
            name='name',
            field=models.TextField(max_length=255),
        ),
    ]
