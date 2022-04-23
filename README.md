## CRUD_Django
###### https://learndjango.com/tutorials/official-django-rest-framework-tutorial-beginners

- Make model
- Register model
- Serialize model
- Make superuser
- python manage.py runserver
- writeviews- we need a view that handles the logic of combining a model, serializer, and eventually URL together
- Configure urls



#### Key Points:
- Django doesn’t hit the database until you explicitly call save().
- A model class represents a database table, and an instance of that class represents a particular record in the database table.
- To create an object, instantiate it using keyword arguments to the model class, then call save() to save it to the database. Django doesn’t hit the database until you explicitly call save().
#####  ref: https://docs.djangoproject.com/en/1.8/topics/db/queries/

- The generic views provided by REST framework allow you to quickly build API views that map closely to your database models.

#### ref: https://www.django-rest-framework.org/api-guide/generic-views/









