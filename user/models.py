from django.db import models

# Create your models here.
class User(models.Model):
    id_user=models.IntegerField(primary_key=True)
    avatar=models.CharField(max_length=1000,default='https://www.google.com/imgres?imgurl=https%3A%2F%2Fupload.wikimedia.org%2Fwikipedia%2Fcommons%2Fthumb%2F5%2F57%2FOOjs_UI_icon_userAvatar-progressive.svg%2F1024px-OOjs_UI_icon_userAvatar-progressive.svg.png&tbnid=-b9IPfu7OOdz3M&vet=12ahUKEwj_yqOS4Jb-AhWMP3AKHbM8DG4QMygFegQIARBQ..i&imgrefurl=https%3A%2F%2Fvi.wiktionary.org%2Fwiki%2FT%25E1%25BA%25ADp_tin%3AOOjs_UI_icon_userAvatar-progressive.svg&docid=299hQiK9bu73zM&w=1024&h=1024&q=anhr%20user&ved=2ahUKEwj_yqOS4Jb-AhWMP3AKHbM8DG4QMygFegQIARBQ')
    fullname=models.CharField(max_length=200)
    username=models.CharField(max_length=200)
    password=models.CharField(max_length=100)
    def __str__(self):
        return self.id_user
    def set_avatar(self, avatar):
        self.avatar = avatar
    def set_fullname(self, fullname):
        self.fullname = fullname
    
    