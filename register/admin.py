from django.contrib import admin
from register.models import (Card, Category, DollarToday, FollowUpCard, Installments, STATUS)

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

class FollowUpCardFilterByStatus(admin.SimpleListFilter):
    title = 'status'
    parameter_name = 'status'

    def lookups(self, request, model_admin):
        return STATUS

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(status=self.value())
        queryset.filter()

class FollowUpCardFilterByCard(admin.SimpleListFilter):
    title = 'card'
    parameter_name = 'card'

    def lookups(self, request, model_admin):
        return [(c.id, c.name) for c in Card.objects.all()]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(card__id__exact=self.value())
        queryset.filter()

@admin.register(FollowUpCard)
class FollowUpCardAdmin(admin.ModelAdmin):
    list_display = ('card', 'due_date', 'amount', 'status', 'notify', )
    list_filter = (FollowUpCardFilterByStatus, FollowUpCardFilterByCard, )

@admin.register(Installments)
class InstallmentsAdmin(admin.ModelAdmin):
    list_display = ('card', 'amount', 'get_installments')

    def get_installments(self, obj) -> str:
        return "%d/%d" % (obj.current_installment, obj.total_installments)
    get_installments.short_description = 'Installments'