# Generated by Django 2.1.5 on 2019-02-13 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mentee', '0002_auto_20190213_0254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menteebase',
            name='profilePict',
            field=models.ImageField(upload_to='mentee'),
        ),
    ]