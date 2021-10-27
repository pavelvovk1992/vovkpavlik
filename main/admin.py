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
        fields = "__all__"

class FlatPageAdmin(admin.ModelAdmin):
    form = FlatPageAdminForm


@admin.register(Seller)
class SellerAdmin(admin.ModelAdmin):
    list_display = ["user", "get_count_adds"]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        "slug": ("name",)
    }


@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):
    list_display = [
        "seller",
        "category",
        "name",
        "price",
        "created_at",
        "updated_at",
        "is_archive"
    ]


admin.site.register(Tag)
