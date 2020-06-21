from django.contrib import admin

from .models import Post,Contact,About,Product


#once we have created the DB we need to import it , and register it here----IMPORTANT
admin.site.register(Post)
admin.site.register(Contact)
admin.site.register(About)
admin.site.register(Product)