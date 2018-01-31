from __future__ import unicode_literals

from django.db import models
import re

email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


class Users_manager(models.Manager):
    def validator(self, postData):
        errors = {}
        if len(postdata['first_name']) < 1:
            errors['first_name'] = "Name cannot be empty."
        if len(postdata['last_name']) < 1: 
            errors['last_name'] = "Name cannot be empty."
        if len(postdata['email']) < 1:
            errors['email1'] = "E-mail cannot be empty."
        if not email_regex.match(request.form['email']):
            errors['email2'] = "E-mail is not valid."
        x = Users.objects.filter(email = request.POST['email'])
        if len(x) > 0
            errors['email3'] = "E-mail already exists."
        return errors

class Users(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = Users_manager()


