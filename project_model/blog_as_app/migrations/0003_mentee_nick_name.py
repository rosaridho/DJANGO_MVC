# Generated by Django 2.1.5 on 2019-02-11 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_as_app', '0002_remove_mentee_nick_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='mentee',
            name='nick_name',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
