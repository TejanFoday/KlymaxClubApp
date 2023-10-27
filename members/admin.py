from django.contrib import admin
from .models import Member, CampusDon, Event, Content

class MemberAdmin(admin.ModelAdmin):
    list_display = (
        'join_date', 'membership_status', 'member_id', 'full_name', 'nick_name', 
        'phone_number', 'email_address', 'year_joining_klymax', 'year_joining_foundation', 
        'continent', 'country', 'state_district_city', 'occupation', 'field_of_study', 
        'foundation_position', 'skills_expertise'
    )
    list_filter = ('membership_status', 'continent', 'country',)
    search_fields = ('full_name', 'member_id', 'email_address',)

class CampusDonAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'nick_name', 'current_year_in_college', 'faculty', 'department', 'year_joined_club', 'club_position')
    search_fields = ('full_name', 'faculty', 'department','phone_number')

class ContentAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return request.user.is_superuser

    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser

class EventAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return request.user.is_superuser

    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser

# Register your models with the custom admins
admin.site.register(Member, MemberAdmin)
admin.site.register(CampusDon, CampusDonAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Content, ContentAdmin)

