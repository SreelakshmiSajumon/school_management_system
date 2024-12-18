School Management System with Role-Based Access Control
This is a Django-based School Management System (SMS) API designed using Django Rest Framework (DRF) to manage student details, library history, and fee records. The system uses Role-Based Access Control (RBAC) to provide different access levels for Admin, Office Staff, and Librarian roles. The Admin has full control over the system, while Office Staff can manage student details and fees, and the Librarian has access to library records only.

Features
Authentication: Token-based login for different user roles (Admin, Office Staff, Librarian).
Role-Based Access Control (RBAC): Different permissions for Admin, Office Staff, and Librarian.
CRUD Operations: Perform create, read, update, and delete operations on students, library history, and fees history.
Admin Dashboard: Manage users (Office Staff, Librarians), and perform CRUD operations on students, library, and fees records.
Office Staff Dashboard: View and manage student details, library history, and fees records.
Librarian Dashboard: View-only access to student and library history.
Forms for Library History and Fees Remarks: Create and manage borrowing records and fee transactions for students.
Technologies Used
Backend: Django, Django Rest Framework (DRF)
Frontend: Django templates 
Libraries Used
Django: The backend framework.
Django Rest Framework (DRF)
Django REST Framework SimpleJWT
Django Messages: For handling user messages and confirmations.
djangorestframework: For serialization and API management.
