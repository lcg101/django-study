from django.db import models

# Create your models here.
# python3 manage.py makemigrations 모델 바꾸면 필수적으로 해야됨
# python3 manage.py migrate 데이터베이스에 반영을 해줘야됨

class Fcuser(models.Model):
    username = models.CharField(max_length=32,
                                verbose_name='사용자명')
    useremail = models.EmailField(max_length=128,
                                verbose_name='사용자 이메일')
    password = models.CharField(max_length=64,
                                verbose_name='비밀번호')
    registered_dttm = models.DateTimeField(auto_now_add=True,
                                            verbose_name='등록시간')
    def __str__(self):
        return self.username
    
    class Meta:
        db_table = 'fastcampus_fcuser'
        verbose_name = 'Test 사용자'
        verbose_name_plural = 'Test 사용자'
