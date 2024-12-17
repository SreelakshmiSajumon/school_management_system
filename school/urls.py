from rest_framework.routers import DefaultRouter
from .views import login_view,register_user, CustomUserViewSet,StudentViewSet, LibraryHistoryViewSet, FeesHistoryViewSet
from django.urls import path, include
from . import views

router = DefaultRouter()
router.register('users', CustomUserViewSet, basename='user')
router.register('students', StudentViewSet, basename='student')
router.register('library-history', LibraryHistoryViewSet, basename='library-history')
router.register('fees-history', FeesHistoryViewSet, basename='fees-history')

urlpatterns = [
    path('login/', login_view, name='login'),
    path('register/', register_user, name='register_user'),
    path('api/', include(router.urls)),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('manage-users/', views.manage_users, name='manage_users'),
    path('edit-user/<int:user_id>/', views.edit_user, name='edit_user'), 
    path('delete-user/<int:user_id>/', views.delete_user, name='delete_user'),  
    path('office-staff-dashboard/', views.office_staff_dashboard, name='office_staff_dashboard'),
    path('manage-fees-history/', views.manage_fees_history, name='manage_fees_history'),
    path('add-fee/', views.add_fee, name='add_fee'),
    path('edit-fee/<int:fee_id>/', views.edit_fee, name='edit_fee'),
    path('delete-fee/<int:fee_id>/', views.delete_fee, name='delete_fee'),
    path('librarian-dashboard/', views.librarian_dashboard, name='librarian_dashboard'),
    path('add_library_record/', views.add_library_record, name='add_library_record'),
    path('logout/', views.logout_view, name='logout'),
]
