# Django Task Assignment Report

### Find and Fix Errors

1. All `created_on` field names in models and serializers changed to `created_at`.
2. Fake migrations applied to preserve database data and maintain migration flow.
3. Fixed bugs in settings.

### Improvements

1. Project structure improved.
2. Modular setting files implemented, and the settings catalog added to the `core.py` file.
3. Custom API library added to create a more representative API for the frontend and make the APIs more scalable.
4. `EstimateSerializer` modified to automatically set `created_at` and `created_by` without user access in the API.
5. `EstimateListView` added to provide a list of available estimates for users, enabling them to better manage estimates.
6. `EquipmentListView` added to allow users to choose equipment by calling the list.
7. Performance improvement tips added after analyzing the codebase.
8. OpenAPI, Swagger, and Redoc added for API documentation.
9. Global code refactoring applied, and redundant code removed.

### Add Authentication

1. `django-allauth` and `dj-rest-auth` added for integrated Django authentication.
2. Email verification, password reset, user profile, and user login endpoints added for user authentication.
3. Social account OAuth infrastructure added for future use of Google OAuth or other OAuth services.
4. `IsAdminOrReadOnly` permission added to `user.permissions` to restrict Create, Update, and Delete actions to `is_staff` users.

### Write Tests

- Unit tests added using the `rest_framework`'s `APIClient` class for creating, updating, and deleting Estimate objects.
