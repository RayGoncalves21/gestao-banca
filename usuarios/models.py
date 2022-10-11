from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,
                                        PermissionsMixin)
from django.db import models


class UsuarioManager(BaseUserManager):

    def create_user(self, email, password):
        usuario = self.model(

            email=self.normalize_email(email),
            password=password,
        )

        usuario.is_active = True
        usuario.is_staff = False
        usuario.is_superuser = False

        usuario.set_password(password)

        usuario.save()

        return usuario

    def create_superuser(self, email, password):
        usuario = self.create_user(

            email=self.normalize_email(email),
            password=password,
        )

        usuario.is_active = True
        usuario.is_staff = True
        usuario.is_superuser = True

        usuario.set_password(password)

        usuario.save()

        return usuario


class Usuario(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(
        verbose_name="E-mail do usuário",
        max_length=194,
        unique=True,
    )

    is_active = models.BooleanField(
        verbose_name="O usuário está ativo",
        default=True,
    )
    is_staff = models.BooleanField(
        verbose_name="O usuário é do desenvolvimento",
        default=False,
    )
    is_superuser = models.BooleanField(
        verbose_name="É um super usuário",
        default=False,
    )

    USERNAME_FIELD = 'email'

    objects = UsuarioManager()

    class Meta:
        verbose_name = "Usuário",
        verbose_name_plural = "Usuários",
        db_table = "usuario"

    def __str__(self):
        return self.email
