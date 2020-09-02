from django.contrib.auth.models import User
from django.db import models

# models represent database tables and schema
class ApplicationUser(User):
    
    class Meta:
        db_table = 'accounts-user'
        verbose_name = 'AppUser'
        verbose_name_plural = 'AppUsers'

