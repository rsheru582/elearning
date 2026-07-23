from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import JsonResponse
from .models import Course, Lesson, Quiz, Question

def marketing_home(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    return render(request, 'marketing.html')

@login_required(login_url='login')
def student_dashboard(request):
    # Dynamically query calculations for the user metrics
    total_courses = Course.objects.count()
    total_quizzes = Quiz.objects.count()
    
    context = {
        'total_courses_count': total_courses,
        'total_quizzes_count': total_quizzes,
        'progress_percentage': 75,  # Baseline sample progress metrics
        'hours_logged': "18.4"
    }
    return render(request, 'dashboard.html', context)


@login_required(login_url='login')
def course_catalog(request):
    return render(request, 'index.html')

@login_required(login_url='login')
def course_player(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    return render(request, 'player.html', {'course': course})

@login_required(login_url='login')
def quiz_view(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    return render(request, 'quiz.html', {'quiz': quiz})

def api_courses(request):
    courses = list(Course.objects.all().values('id', 'title', 'description', 'instructor', 'duration'))
    return JsonResponse(courses, safe=False)

def api_lessons(request, course_id):
    lessons = list(Lesson.objects.filter(course_id=course_id).order_by('order').values('title', 'video_url'))
    return JsonResponse(lessons, safe=False)

def api_quiz_questions(request, quiz_id):
    questions = list(Question.objects.filter(quiz_id=quiz_id).values('id', 'text', 'option_a', 'option_b', 'option_c', 'option_d'))
    return JsonResponse(questions, safe=False)

def api_quiz_verify(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    selected = request.GET.get('choice', '').upper()
    is_correct = (selected == question.correct_answer)
    return JsonResponse({'correct': is_correct, 'answer': question.correct_answer})

def user_register(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method == 'POST':
        u = request.POST.get('username')
        e = request.POST.get('email')
        p = request.POST.get('password')
        if User.objects.filter(username=u).exists():
            messages.error(request, "Username already taken.")
            return redirect('register')
        user = User.objects.create_user(username=u, email=e, password=p)
        login(request, user)
        return redirect('dashboard')
    return render(request, 'register.html')

def user_login(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method == 'POST':
        u = request.POST.get('username')
        p = request.POST.get('password')
        user = authenticate(request, username=u, password=p)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid credentials.")
            return redirect('login')
    return render(request, 'login.html')

def user_logout(request):
    logout(request)
    return redirect('marketing_home')
