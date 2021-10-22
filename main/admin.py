from django import forms
from django.contrib import admin
from ckeditor.widgets import CKEditorWidget
from django.contrib.flatpages.admin import FlatPageAdmin
from django.contrib.flatpages.models import FlatPage

from .models import Seller, Category, Tag, Ad


class FlatPageAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = FlatPage
        fields = '__all__'

class FlatPageAdmin(admin.ModelAdmin):
    form = FlatPageAdminForm



class SellerAdmin(admin.ModelAdmin):
    list_display = ('user', 'get_count_adds')


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        "slug": ("title",)
    }


# admin.site.unregister(FlatPage)
# admin.site.register(FlatPage, FlatPageAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Seller, SellerAdmin)
