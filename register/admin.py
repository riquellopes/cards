from django.contrib import admin
from register.models import (Card, Category, DollarToday, FollowUpCard, Installments)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    fields = ('name', )
    list_display = ('name', )

@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ('name', 'dot', 'category', )

@admin.register(DollarToday)
class DollarTodayAdmin(admin.ModelAdmin):
    
    def has_add_permission(self, request, obj=None):
        return False
    
    def has_change_permission(self, request, obj=None):
        return False

@admin.register(FollowUpCard)
class FollowUpCardAdmin(admin.ModelAdmin):
    list_display = ('card', 'due_date', 'amount', 'notify', )

@admin.register(Installments)
class InstallmentsAdmin(admin.ModelAdmin):
    list_display = ('card', 'amount', 'get_installments')

    def get_installments(self, obj) -> str:
        return "%d/%d" % (obj.current_installment, obj.total_installments)
    get_installments.short_description = 'Installments'