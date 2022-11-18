from django.contrib import admin

from books.models import Offer, Patients, Request

admin.site.register(Patients)
admin.site.register(Request)
admin.site.register(Offer)
