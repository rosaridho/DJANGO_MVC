# Generated by Django 2.1.5 on 2019-02-11 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dokter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=255)),
                ('nomor_telepon', models.TextField(max_length=255)),
                ('bidang', models.CharField(max_length=255)),
                ('jadwal_praktek', models.TextField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Obat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=255)),
                ('kandungan', models.CharField(max_length=255)),
                ('khasiat', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Pasien',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=255)),
                ('nomor_telepon', models.TextField(max_length=255)),
                ('alamat', models.CharField(max_length=255)),
                ('keluhan', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Resep',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=255)),
                ('total_harga', models.TextField(max_length=255)),
                ('kumpulan_obat', models.CharField(max_length=255)),
            ],
        ),
    ]
