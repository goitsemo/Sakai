from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('register/', 
         views.StudentRegistrationView.as_view(), 
         name='student_registration'),
     path('enroll-course/',
         views.StudentEnrollCourseView.as_view(),
         name='student_enroll_course'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
