from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, ScopeArticle, Scope


class ScopeArticleInlineFormset(BaseInlineFormSet):
    def clean(self):
        tag_count = 0
        for form in self.forms:
            if form.cleaned_data['is_main']:
                tag_count += 1
        if tag_count == 0:
            raise ValidationError('Предупреждение! Обязательно укажите основной тег!')
        elif tag_count > 1:
            raise ValidationError('Внимание! Основным может быть только один тег!')

        return super().clean()


class ScopeArticleInline(admin.TabularInline):
    model = ScopeArticle
    extra = 1
    formset = ScopeArticleInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopeArticleInline]
    list_display = ['id', 'title', 'published_at']


@admin.register(Scope)
class ScopeAdmin(admin.ModelAdmin):
    inlines = [ScopeArticleInline]
    list_display = ['id', 'name']
