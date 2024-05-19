from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
def get_default_superuser_id():
    User = get_user_model()
    superuser = User.objects.filter(is_superuser=True).first()
    return superuser.id if superuser else None

class Post(models.Model):
  title = models.CharField(max_length=100)
  date = models.DateTimeField(auto_now_add=True)
  description = models.CharField(max_length=100)
  content = models.TextField()
  user = models.ForeignKey(
      get_user_model(),
      on_delete=models.CASCADE,
      default=get_default_superuser_id
    )

  def __str__(self):
      return self.title
  