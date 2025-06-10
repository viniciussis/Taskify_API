# Taskify API - A Django Task Management System

This project is a RESTful API for managing projects and tasks.

## Project Development Checklist

### Phase 0: Project Setup
TODO: Install necessary packages: `pip install djangorestframework djangorestframework-simplejwt`
TODO: Configure `settings.py`:
    - TODO: Add `rest_framework`, `rest_framework_simplejwt`, and `core` to `INSTALLED_APPS`.
    - TODO: Configure `REST_FRAMEWORK` settings for default authentication (JWT) and permissions.
TODO: Create initial database migrations (`python manage.py makemigrations` and `python manage.py migrate`).
TODO: Create a superuser to access the admin panel (`python manage.py createsuperuser`).

### Phase 1: Models and Admin
TODO: Define core models in `core/models.py`:
    - TODO: Create a `Project` model with fields like `title`, `description`, and a `ForeignKey` to the `User`.
    - TODO: Create a `Task` model with fields like `title`, `description`, `status` (e.g., 'To Do', 'In Progress', 'Done'), `due_date`, and a `ForeignKey` to the `Project`.
TODO: Register models in `core/admin.py` to make them accessible in the Django admin interface.
TODO: Create and apply the database migrations for the new models.

### Phase 2: API - Serialization
TODO: Create a `serializers.py` file in the `core` app.
TODO: Implement `ProjectSerializer` to handle `Project` model data.
TODO: Implement `TaskSerializer` to handle `Task` model data.
    - NOTE: Ensure the serializer handles the relationship with the `Project` model correctly.
TODO: Implement User registration serializer to create new users.

### Phase 3: API - Views and URLs
TODO: Create user registration and login views.
    - TODO: Implement a view for user registration (`/api/auth/register/`).
    - TODO: Use `djangorestframework-simplejwt` views for token acquisition (`/api/auth/token/`) and refresh (`/api/auth/token/refresh/`).
TODO: Implement `ModelViewSet` for Projects in `core/views.py`.
    - TODO: Ensure only authenticated users can create projects.
    - TODO: Implement permissions so users can only view, update, or delete their *own* projects.
    - HACK: Use `self.request.user` in the `perform_create` method to assign the project to the current user.
TODO: Implement `ModelViewSet` for Tasks.
    - TODO: Tasks should be nested under projects. The endpoint could look like `/api/projects/<project_id>/tasks/`.
    - TODO: Ensure a user can only add tasks to their own projects.
    - TODO: Ensure a user can only view/modify tasks belonging to their own projects.
TODO: Configure `urls.py` in the main project folder and create a `urls.py` in the `core` app to map all the API endpoints.

### Phase 4: Permissions & Validation
TODO: Create a custom permission class in a `permissions.py` file.
    - TODO: Implement `IsOwner` permission to check if `obj.user == request.user`.
    - TODO: Apply this custom permission to the `Project` and `Task` ViewSets.
TODO: Add validation to models or serializers.
    - TODO: For example, ensure the `status` field in the `Task` model only accepts predefined choices.
    - TODO: Ensure a task's `due_date` cannot be in the past.

### Phase 5: Advanced Features (Optional)
TODO: Implement task filtering in the `Task` view.
    - TODO: Allow filtering tasks by `status` (e.g., `/api/projects/<project_id>/tasks/?status=Done`).
    - TODO: Allow filtering tasks by `due_date`.
TODO: Implement project collaboration.
    - TODO: Add a ManyToManyField to the `Project` model for `members`.
    - TODO: Update permissions to allow project members to view/edit tasks.
    - TODO: Create an endpoint to add/remove members from a project.
TODO: Add a commenting feature to tasks.
    - TODO: Create a `Comment` model with a `ForeignKey` to `Task` and `User`.
    - TODO: Create a serializer and viewset for comments, nested under tasks.