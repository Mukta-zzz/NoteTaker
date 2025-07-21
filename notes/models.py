from django.db import models
from django.contrib.auth.models import User

class Note(models.Model):
    NOTE_TYPE_CHOICES = [
        ('normal', 'Normal'),
        ('movies', 'Movies'),
        ('books', 'Books'),
        ('songs', 'Songs'),
        ('random', 'Random'),
    ]

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    note_type = models.CharField(max_length=10, choices=NOTE_TYPE_CHOICES, default='normal')
    title = models.CharField(max_length=100, blank=True, null=True)
    content = models.TextField(help_text="For bullets, use one item per line.")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title or f"{self.note_type.capitalize()} note"
