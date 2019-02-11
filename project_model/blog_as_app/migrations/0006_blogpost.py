# Generated by Django 2.1.5 on 2019-02-11 07:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog_as_app', '0005_auto_20190211_0713'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated', models.DateTimeField(default=django.utils.timezone.now)),
                ('title', models.CharField(max_length=255)),
                ('content', models.CharField(max_length=255)),
                ('created_by', models.CharField(max_length=255)),
            ],
        ),
    ]
