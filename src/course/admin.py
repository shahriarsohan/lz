from django.contrib import admin

from .models import Courses, CourseContent


# class CourseContent(admin.StackedInline):
#     model = CourseContent


# @admin.register(Courses)
# class CourseAdmin(admin.ModelAdmin):
#     inlines = [CourseContent]

#     class Meta:
#         model = Courses


# admin.site.register(CourseContent)


class PhotoInline(admin.StackedInline):
    model = CourseContent


@admin.register(Courses)
class AuthorAdmin(admin.ModelAdmin):
    inlines = [PhotoInline]
