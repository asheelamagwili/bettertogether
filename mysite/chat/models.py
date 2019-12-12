from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

class Message(models.Model):
    author = models.ForeignKey(User, related_name='author_messages', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author.username

    # Preloads last 15 messages
    def last_15_messages(self):
        # Returns last 15 Message objects in reverse order (most recent timestamps first)
        return Message.objects.order_by('-timestamp').all()[:15]
