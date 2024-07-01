from django.db import models

# Create your models here.
def user_directoty_path(instance, filemane):
    # путь, куда будет осуществлена загрузка MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id, filemane)

class User(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class UploadFiles(models.Model):
    title = models.CharField(max_length=200)
    type = models.CharField(max_length=10)
    file = models.FileField(null=True, blank=True, upload_to=user_directoty_path)
    access_link = models.CharField(max_length=350)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='files')

    def __str__(self):
        return self.title
