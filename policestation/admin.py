from django.contrib import admin

from policestation.models import Commissioner, Complaint, Constable, Fir, Inspector, Manageinfo


admin.site.site_header = "E-police Station Admin"
admin.site.site_title = "E-Police Station Admin Portal"
admin.site.index_title = "Welcome To E-Police Station"

# Register your models here.

admin.site.register(Commissioner)
admin.site.register(Fir)
admin.site.register(Complaint)
admin.site.register(Inspector)
admin.site.register(Constable)
admin.site.register(Manageinfo)



