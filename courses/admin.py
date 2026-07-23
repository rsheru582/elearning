from django.contrib import admin
from .models import Course, Lesson, Quiz, Question

# Configure administrative display layouts
class LessonInline(admin.TabularInline):
    model = Lesson
    extra = 1

class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'duration', 'instructor')
    search_fields = ('title', 'instructor')
    inlines = [LessonInline]

class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1

class QuizAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'course')
    search_fields = ('title',)
    inlines = [QuestionInline]

# Overwrite native site headers with custom branded naming conventions
admin.site.site_header = "ELearn OPERATIONAL GATEWAY"
admin.site.site_title = "ELearn Control Terminal"
admin.site.index_title = "System Data Core Configuration Desk"

# Apply customized administrative registration hooks
admin.site.register(Course, CourseAdmin)
admin.site.register(Quiz, QuizAdmin)
admin.site.register(Lesson)
admin.site.register(Question)
