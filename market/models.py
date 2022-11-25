from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    deskripsi = models.TextField()

    def __str__(self):
        return self.title

class Produk(models.Model):
    nama = models.CharField(max_length=200)
    deskripsi = models.TextField()
    harga = models.CharField(max_length=200)
    diskon = models.CharField(max_length=200)

    def __str__(self):
        return self.nama

class Keranjang(models.Model):
    produk = models.TextField()
    jumlah = models.CharField(max_length=200)
    
    def __str__(self):
        return self.produk
    
class Pemesanan(models.Model):
    total_harga = models.CharField(max_length=200)
    nomor_pembayaran = models.CharField(max_length=200)

    def __str__(self):
        return self.total_harga

class Whislist(models.Model):
    produk = models.CharField(max_length=200)
    jumlah_produk = models.CharField(max_length=200)

    def __str__(self):
        return self.produk