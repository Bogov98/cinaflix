from django.contrib.auth.models import User

def crear_usuarios():
    for i in range(1, 672):
        User.objects.create_user(username=f'usuario{i}', 
                                 password='1234', 
                                 email=f'email{i}@gmail.com', 
                                 first_name=f'user{i}', 
                                 last_name=f'user{i}')