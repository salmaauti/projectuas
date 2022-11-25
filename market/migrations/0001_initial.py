# Generated by Django 4.1.3 on 2022-11-21 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('deskripsi', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Keranjang',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('produk', models.TextField()),
                ('jumlah', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Pemesanan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_harga', models.CharField(max_length=200)),
                ('nomor_pembayaran', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Produk',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=200)),
                ('deskripsi', models.TextField()),
                ('harga', models.CharField(max_length=200)),
                ('diskon', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Whislist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('produk', models.CharField(max_length=200)),
                ('jumlah_produk', models.CharField(max_length=200)),
            ],
        ),
    ]
