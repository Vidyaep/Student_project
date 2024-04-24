from django.urls import path
from studentdetails.views import *

urlpatterns = [
    path('school/list', school_list, name='school-list'),
    path('school/add', school_add, name='school-add'),
    path('batch/list', batch_list, name='batch-list'),
    path('batch/add', batch_add, name='batch-add'),
    path('student/list', student_list, name='student-list'),
    path('student/add', student_add, name='student-add'),
    path('school/<int:school_id>/delete/', school_delete, name='school-delete'),
    path('student/<int:student_id>/edit/', student_edit, name='student-edit'),
    path('school/<int:school_id>/update/', school_update, name='school-update'),
    path('school/<int:school_id>/batchs/',SchoolWithBatch.as_view(),name='School-With-Batch'),
]