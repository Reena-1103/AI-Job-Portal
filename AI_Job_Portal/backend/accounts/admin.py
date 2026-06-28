from django.contrib import admin
from .models import Register, Job, ApplyJob, Recommendation

admin.site.register(Register)
admin.site.register(Job)
admin.site.register(ApplyJob)
admin.site.register(Recommendation)