from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import authenticate, login
from django.contrib import messages
from rest_framework import viewsets
from django.contrib.auth.decorators import login_required
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAdmin, IsOfficeStaff, IsLibrarian
from .models import CustomUser, Student, LibraryHistory, FeesHistory
from .serializers import CustomUserSerializer, StudentSerializer, LibraryHistorySerializer, FeesHistorySerializer
from django.contrib.auth import logout
from django.shortcuts import redirect
from .forms import UserRegistrationForm,FeesHistoryForm,LibraryHistoryForm,LibraryRecordForm   


@login_required
def register_user(request):
    
    if request.user.role != 'admin':
        messages.error(request, "You are not authorized to register users.")
        return redirect('admin_dashboard')

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "User created successfully!")
            return redirect('admin_dashboard') 
    else:
        form = UserRegistrationForm()

    return render(request, 'register_user.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            print(f"Authenticated user: {user}, Role: {user.role}") 
            login(request, user)
           
            if user.role == 'admin':
                return redirect('admin_dashboard')
            elif user.role == 'staff':   
                return redirect('office_staff_dashboard')
            elif user.role == 'librarian':
                return redirect('librarian_dashboard')
        else:
            print("Authentication failed")  
            messages.error(request, 'Invalid username or password')
    return render(request, 'login.html')

@login_required
def admin_dashboard(request):
    if request.user.role != 'admin':  
        messages.error(request, "You are not authorized to access this page.")
        return redirect('login')

    users = CustomUser.objects.all()
    students = Student.objects.all()
    fees_history = FeesHistory.objects.all()
    library_records = LibraryHistory.objects.all()

    context = {
        'users': users,
        'students': students,
        'fees_history': fees_history,
        'library_records': library_records,
    }
    return render(request, 'admin_dashboard.html', context)

@login_required
def manage_users(request):
    if request.user.role != 'admin': 
        messages.error(request, "You are not authorized to access this page.")
        return redirect('login')

    users = CustomUser.objects.all()  
    context = {
        'users': users
    }

    return render(request, 'manage_users.html', context)
@login_required
def edit_user(request, user_id):
    if request.user.role != 'admin':  
        messages.error(request, "You are not authorized to access this page.")
        return redirect('login')

    user = get_object_or_404(CustomUser, pk=user_id)

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, f"User {user.username} updated successfully!")
            return redirect('manage_users')
    else:
        form = UserRegistrationForm(instance=user)

    return render(request, 'edit_user.html', {'form': form, 'user': user})

@login_required
def delete_user(request, user_id):
    if request.user.role != 'admin':  
        messages.error(request, "You are not authorized to access this page.")
        return redirect('login')

    user = get_object_or_404(CustomUser, pk=user_id)
    user.delete()
    messages.success(request, f"User {user.username} deleted successfully!")
    return redirect('manage_users')

@login_required
def office_staff_dashboard(request):
    if request.user.role not in ['admin', 'staff']:
        messages.error(request, "You are not authorized to access this page.")
        return redirect('login')

    students = Student.objects.all()
    fees_history = FeesHistory.objects.all()
    library_records = LibraryHistory.objects.all()

    context = {
        'students': students,
        'fees_history': fees_history,
        'library_records': library_records,
    }
    return render(request, 'office_staff_dashboard.html', context)

def manage_fees_history(request):
   
    fees_history = FeesHistory.objects.all()
    
    
    context = {
        'fees_history': fees_history,
    }
    
    return render(request, 'manage_fees_history.html', context)

@login_required
def add_fee(request):
    if request.user.role not in ['admin', 'staff']:
        messages.error(request, "You are not authorized to perform this action.")
        return redirect('login')

    if request.method == 'POST':
        form = FeesHistoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Fee record added successfully.")
            return redirect('office_staff_dashboard')
    else:
        form = FeesHistoryForm()

    return render(request, 'add_fee.html', {'form': form})

@login_required
def edit_fee(request, fee_id):
    fee = FeesHistory.objects.get(id=fee_id)

    if request.user.role not in ['admin', 'staff']:
        messages.error(request, "You are not authorized to perform this action.")
        return redirect('login')

    if request.method == 'POST':
        form = FeesHistoryForm(request.POST, instance=fee)
        if form.is_valid():
            form.save()
            messages.success(request, "Fee record updated successfully.")
            return redirect('office_staff_dashboard')
    else:
        form = FeesHistoryForm(instance=fee)

    return render(request, 'edit_fee.html', {'form': form})

@login_required
def delete_fee(request, fee_id):
    fee = FeesHistory.objects.get(id=fee_id)

    if request.user.role not in ['admin', 'staff']:
        messages.error(request, "You are not authorized to perform this action.")
        return redirect('login')

    if request.method == 'POST':
        fee.delete()
        messages.success(request, "Fee record deleted successfully.")
        return redirect('office_staff_dashboard')

    return render(request, 'confirm_delete_fee.html', {'fee': fee})


@login_required
def librarian_dashboard(request):
    if request.user.role not in ['admin', 'librarian']:
        messages.error(request, "You are not authorized to access this page.")
        return redirect('login')

    students = Student.objects.all()  
    library_records = LibraryHistory.objects.all()  

    context = {
        'students': students,
        'library_records': library_records,
    }
    return render(request, 'librarian_dashboard.html', context)

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def add_library_record(request):
    if request.user.role not in ['admin', 'librarian']:
        messages.error(request, "You are not authorized to perform this action.")
        return redirect('login')

    if request.method == 'POST':
        form = LibraryRecordForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Library record added successfully.")
            return redirect('librarian_dashboard') 
        else:
            print(form.errors)  
    else:
        form = LibraryRecordForm()

    return render(request, 'add_library_record.html', {'form': form})


class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticated, IsAdmin]  


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get_permissions(self):
        if self.action in ['create', 'update', 'destroy']:
            return [IsAdmin()]
        return [IsAdmin() | IsOfficeStaff() | IsLibrarian()]


class LibraryHistoryViewSet(viewsets.ModelViewSet):
    queryset = LibraryHistory.objects.all()
    serializer_class = LibraryHistorySerializer

    def get_permissions(self):
        if self.action in ['create', 'update', 'destroy']:
            return [IsAdmin()]
        return [IsAdmin() | IsLibrarian()]


class FeesHistoryViewSet(viewsets.ModelViewSet):
    queryset = FeesHistory.objects.all()
    serializer_class = FeesHistorySerializer

    def get_permissions(self):
        if self.action in ['create', 'update', 'destroy']:
            return [IsAdmin() | IsOfficeStaff()]
        return [IsAdmin() | IsOfficeStaff()]
