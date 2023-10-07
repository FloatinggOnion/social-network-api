import uuid
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from core.abstract.models import AbstractModel, AbstractManager


class UserManager(BaseUserManager, AbstractManager):

    def create_user(self, username, email, password=None, **kwargs):
        if username is None:
            raise TypeError('Users must have a username.')
        if email is None:
            raise TypeError('Users must have an email.')
        if password is None:
            raise TypeError('User must have an email.')
        

        user = self.model(username=username, email=self.normalize_email(email), **kwargs)
        user.set_password(password)
        user.save(using=None)

        return user


    def create_superuser(self, username, email, password, **kwargs):
        if password is None:
            raise TypeError('Superusers must have a password.')
        if email is None:
            raise TypeError('Superusers must have an email.')
        if username is None:
            raise TypeError('Superusers must have an username.')
        
        user = self.create_user(username, email, password, **kwargs)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        
        return user


class User(AbstractModel, AbstractBaseUser, PermissionsMixin):
    username = models.CharField(db_index=True, max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    bio = models.TextField(editable=True, blank=True)
    avatar = models.ImageField(verbose_name='avatar', upload_to=None, height_field=None, width_field=None, max_length=100, blank=True)
    email = models.EmailField(db_index=True, unique=True)
    posts_liked = models.ManyToManyField('core_post.Post', related_name='liked_by')
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def __str__(self):
        return f'{self.email}'
    
    @property
    def name(self):
        return f'{self.first_name} {self.last_name}'
    
    def like(self, post):
        '''Like a post if it hasn't been liked yet'''
        return self.posts_liked.add(post)
    
    def unlike(self, post):
        '''Remove a like from a post'''
        return self.posts_liked.remove(post)

    def has_liked(self, post):
        '''Check if a post has been liked'''
        return self.posts_liked.filter(pk=post.pk).exists() # Check is the post is in the list of liked