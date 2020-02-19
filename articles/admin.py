from django.contrib import admin

# Register your models here.
from .models import Article



@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title' , 'view' , 'published_at' , 'show')
    date_hierarchy = 'published_at'
    search_fields = ('title' , 'body')

    list_filter = ('published_at',)
    ordering = ['view']
    actions = ['make_hide' , 'make_show']

    # fields = ('title' , 'body' , 'published_at')
    # exclude = ('view',)
    fieldsets = (
        (None, {
            'fields' : ('title' , 'body' , 'published_at')
        }),
        ('Advanced Options' , {
            'classes' : ('collapse',),
            'fields' : ('view','show')
        })
    )

    def make_hide(self , request , queryset):
        row_updated = queryset.update(show = 0)

        self.giveMessage(request , row_updated , 'hide')

    make_hide.short_description = "Make selected articles as hide"

    def make_show(self , request , queryset):
        row_updated = queryset.update(show = 1)

        self.giveMessage(request , row_updated , 'show')

    make_show.short_description = "Make selected articles as show"


    def giveMessage(self , request , row_updated , type):
        if(row_updated == 1) :
            message_bit = '1 article was'
        else:
            message_bit = "%s articles were" % row_updated
    
        self.message_user(request , "%s successfully marked as %s" % (message_bit , type))