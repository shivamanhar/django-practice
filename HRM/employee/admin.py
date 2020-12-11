from django.contrib import admin

# Register your models here.

from .models import Question,Choice, Employes,Sudent

'''admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Employes)'''

class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 10

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Sudent)