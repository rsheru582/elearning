from django.contrib import admin
from django.urls import path
from courses import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.marketing_home, name='marketing_home'),
    path('courses/', views.course_catalog, name='course_catalog'),
    # Change views.dashboard to views.student_dashboard on this line:
    path('dashboard/', views.student_dashboard, name='dashboard'), 
    path('login/', views.user_login, name='login'),
    path('register/', views.user_register, name='register'),
    path('logout/', views.user_logout, name='logout'),
    path('course/<int:course_id>/', views.course_player, name='course_player'),
    path('quiz/<int:quiz_id>/', views.quiz_view, name='quiz_view'),
    path('api/courses/', views.api_courses, name='api_courses'),
    path('api/courses/<int:course_id>/lessons/', views.api_lessons, name='api_lessons'),
    path('api/quiz/<int:quiz_id>/', views.api_quiz_questions, name='api_quiz_questions'),
    path('api/question/<int:question_id>/verify/', views.api_quiz_verify, name='api_quiz_verify'),
]
