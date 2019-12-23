from django.urls import path

from sample_crud.views import URLListView, SchoolClassAddView, StudentAddView, StudentListView

urlpatterns = [
    path('', URLListView.as_view(), name='all_urls'),
    path('school-class/add/', SchoolClassAddView.as_view(), name='school_class_add'),
    path('student/add/', StudentAddView.as_view(), name='student_add'),
    path('student/list/', StudentListView.as_view(), name='student_list')
]