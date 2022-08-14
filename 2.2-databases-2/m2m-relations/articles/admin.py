from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, ScopeArticle, Scope


class ScopeArticleInlineFormset(BaseInlineFormSet):
    def clean(self):
        n = 0
        for form in self.forms:
            # В form.cleaned_data будет словарь с данными
            # каждой отдельной формы, которые вы можете проверить
            # my_list.append(form.cleaned_data)
            if form.cleaned_data['is_main']:
                n += 1
        if n < 1:
            raise ValidationError('Укажите основной тэг!')
        elif n > 1:
            raise ValidationError('Основным может быть только один тэг!')
            # вызовом исключения ValidationError можно указать админке о наличие ошибки
            # таким образом объект не будет сохранен,
            # а пользователю выведется соответствующее сообщение об ошибке
            # raise ValidationError('Ошибка заполнения формы')
        return super().clean()  # вызываем базовый код переопределяемого метода


class ScopeArticleInline(admin.TabularInline):
    model = ScopeArticle
    extra = 0
    formset = ScopeArticleInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopeArticleInline]
    list_display = ['id', 'title']


@admin.register(Scope)
class ScopeAdmin(admin.ModelAdmin):
    inlines = [ScopeArticleInline]
    list_display = ['id', 'name']
