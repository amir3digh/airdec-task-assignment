Django Task Assignment Report

Task Details
Find and Fix Errors:

    1. All created_on fields names in models and serializers changed to created_at
    2. Fake migrations applied for keeping database data and maintain migration flow
    3. Setting bugs fixed

Improvements:

    1. Project structure improved
    2. Modular setting files applied and settings catalog added to core.py file
    3. Custom api library added far making more representative api for frontend and making apis more scalable
    4. EstimateSerializer modified in order to write created_at and created_on automatically without user access in api
    5. EstimateListView added to provide list of available estimates for user enabling them to better handle them
    6. EquipmentListView added to enable user choice them by calling the list
    7. Some performance improvement tips added by analysing codebase 
    8. OpenApi, swagger and redoc added for api documentation
    9. Global code refactors applied and redundant codes removed

Add Authentication:

    1. django-allauth and dj-rest-auth added for integrated django authentication
    2. Email verification, password reset, user profile and user login endpoints added for user auth
    3. Social account oauth infrastructure added for later use of Google OAuth or other oauth
    4. IsAdminOrReadOnly permission added to user.permissions to limit Create, Update, Delete actions to is_staff users

Write Tests:

    Unit tests added using rest_framework APIClient class for Create, Update and Delete Estimate objects 



