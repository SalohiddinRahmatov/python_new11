from django.contrib import admin
from myfiles.models import *
# Register your models here.
class AdminType(admin. ModelAdmin):
    list_display = ['id','nomi']
admin. site.register(Type, AdminType)
class AdminMax(admin.ModelAdmin):
    list_display = ['id','nomi','tur','vaqt','malumot','rasm']
admin. site.register(Maxsulotlar,AdminMax)

# Register your models here.

class AdminProject(admin.ModelAdmin):
    list_display = ['id','nomi','tur','vaqt','malumot','rasm']
admin. site.register(Project,AdminProject)

class AdminProject1(admin.ModelAdmin):
    list_display = ['id','nomi','tur','vaqt','malumot','rasm']
admin. site.register(Project1,AdminProject1)

class AdminServices(admin.ModelAdmin):
    list_display = ['id','nomi','tur','vaqt','malumot','rasm']
admin. site.register(Services,AdminServices)

class AdminAbout(admin.ModelAdmin):
    list_display = ['id','nomi','tur','vaqt','malumot','rasm']
admin. site.register(About,AdminAbout)

class AdminBlog(admin.ModelAdmin):
    list_display = ['id','nomi','tur','vaqt','malumot']
admin. site.register(Blog,AdminBlog)

class AdminMurojat(admin.ModelAdmin):
    list_display = ['id','ism','fam','mail','text','vaqt']
admin. site.register(Murojat,AdminMurojat)

class AdminGmail(admin.ModelAdmin):
    list_display = ["id",'gmail']
admin. site.register(Gmail,AdminGmail)