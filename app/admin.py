from django.contrib import admin
from app.models import Orders, Questions, Reviews, TutorEarnedDetail, TutorPaymenyDetails, TutorSolvedLabs, UserDetails,TutorRegister,TutorSolvedAssignment,TutorAccount,LabOrders,TutorBalance
@admin.register(UserDetails)
class UserDetailsAdmin(admin.ModelAdmin):
    list_display = ['user','phone','study_level','assignment_reference_style']
    autocomplete_fields = ['user']
    search_fields = ['phone']

@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    list_display = ['order_id','user','subject','deadline']
    search_fields = ['deadline','subject']

    def image_img(self):
        if self.image:
            return u'<img src="%s" />' % self.image.url 
        else:
            return '(No image found)'
    image_img.short_description = 'Thumb'
    image_img.allow_tags = True

@admin.register(TutorBalance)
class TutorBalance(admin.ModelAdmin):
    list_display = ['tutor']
    search_fields = ['tutor']
     
admin.site.register(LabOrders)
@admin.register(TutorRegister)
class TutorRegisterAdmin(admin.ModelAdmin):
    list_display = ['unique_id','tutor','subject']
    search_fields = ['unique_id','subject']
@admin.register(TutorAccount)
class TutorAccountAdmin(admin.ModelAdmin):
    list_display = ['tutor','pan_number','name_on_pan']
    search_fields = ['tutor','pan_number','name_on_pan']
    
admin.site.register(TutorSolvedAssignment)
admin.site.register(TutorSolvedLabs)
admin.site.register(TutorPaymenyDetails)
admin.site.register(TutorEarnedDetail)
admin.site.register(Questions)

admin.site.register(Reviews)

admin.site.site_header  =  "Tutorchamps Admin"  
admin.site.index_title  =  "TutorChamps Admin"