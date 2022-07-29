from django.contrib import admin
from .models import Post



@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, {'fields': ['title']}),
		('User Information', {'fields': ['author']}),
		('Date and Content', {'fields': ['content', 'date_posted']}),
	]
