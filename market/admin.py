from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Blog)
admin.site.register(models.Produk)
admin.site.register(models.Keranjang)
admin.site.register(models.Pemesanan)
admin.site.register(models.Whislist)