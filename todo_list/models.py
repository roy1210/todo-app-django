from django.db import models

'''
Creating database stuff is sort of a three step process. 
Django will take Python Class to SQLite database format.

1: Creating our class. 
2: Creating a migration. 
< python3 manage.py makemigrations >

3: Pushing that migration into the database and then making the whole thing live.
< python3 manage.py migrate >
'''

class List(models.Model):
    # CharField, BooleanField = Data type
    item = models.CharField(max_length = 200)
    completed = models.BooleanField(default = False)

    # Return object information in admin page
    def __str__(self):
        return self.item + " " + str(self.completed)
