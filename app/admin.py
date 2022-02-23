from django.contrib import admin
from app.models import Orders, Questions, Reviews, TutorEarnedDetail, TutorPaymenyDetails, TutorSolvedLabs, UserDetails,TutorRegister,Blog,TutorSolvedAssignment,TutorAccount,LabOrders,TutorBalance
@admin.register(UserDetails)
class UserDetailsAdmin(admin.ModelAdmin):
    list_display = ['user','phone','study_level','assignment_reference_style']
    autocomplete_fields = ['user']
    search_fields = ['phone']

@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    list_display = ['pk','user','subject','deadline']
    search_fields = ['deadline','subject']

    def image_img(self):
        if self.image:
            return u'<img src="%s" />' % self.image.url 
        else:
            return '(No image found)'
    image_img.short_description = 'Thumb'
    image_img.allow_tags = True

admin.site.register(TutorBalance)
admin.site.register(LabOrders)
admin.site.register(TutorRegister)
admin.site.register(TutorAccount)
admin.site.register(Blog)
admin.site.register(TutorSolvedAssignment)
admin.site.register(TutorSolvedLabs)
admin.site.register(TutorPaymenyDetails)
admin.site.register(TutorEarnedDetail)
admin.site.register(Questions)

admin.site.register(Reviews)