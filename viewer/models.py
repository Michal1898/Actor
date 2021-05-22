from django.db.models import (
    DO_NOTHING, CharField, DateField, DateTimeField, ForeignKey, IntegerField,
    Model, TextField, DateField, BooleanField
)

class Genre(Model):
    name = CharField(max_length=128)

    def __str__(self):
        return f'{self.name}'

class Movie(Model):
  title = CharField(max_length=128)
  genre = ForeignKey(Genre, on_delete=DO_NOTHING)
  rating = IntegerField()
  released = DateField()
  description = TextField()
  created = DateTimeField(auto_now_add=True)

  def __str__(self):
      return f'Tento film je {self.title} - {self.rating}'

class Actor(Model):
    firstname = CharField(max_length=50, default='Andy')
    surname = CharField(max_length= 40, default='Anonymus')
    was_born = DateField(default='1900-1-1')
    deceased = BooleanField(default=False)
    died= DateField(default='1900-1-1')
    nationality = CharField(max_length=35, default='USA')
    curriculum = TextField(default='lorem ipsum')

    def __str__(self):
      return f'Actor {self.firstname}  {self.surname} from {self.nationality}.'