from enum import unique
from gc import DEBUG_COLLECTABLE
from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.core.mail import send_mail
from django.core.validators import RegexValidator
from django.template.loader import render_to_string
from django.shortcuts import resolve_url
from common.models import BaseModel, UseChoices
from menu.models import Group


class User(AbstractUser):
    class GenderChoices(models.TextChoices):
        MALE = "M", "남성"
        FEMALE = "F", "여성"

    follower_set = models.ManyToManyField('self', blank=True)
    following_set = models.ManyToManyField('self', blank=True)

    website_url = models.URLField(blank=True)
    bio = models.TextField(blank=True)
    phone_number = models.CharField(max_length=13,
                                    blank=True, validators=[
                                        RegexValidator(r"^010-?[1-9]\d{3}-?\d{4}$")],
                                    )

    gender = models.CharField(max_length=1, blank=True,
                              choices=GenderChoices.choices)
    avatar = models.ImageField(
        blank=True,
        upload_to="accounts/avatar/%Y/%m%d",
        help_text="48px * 48px 크기의 png/jpg 파일을 업로드해주세요",
    )

    @property
    def name(self):
        return f"{self.first_name} {self.last_name}".strip()

    @property
    def avatar_url(self):
        if self.avatar:
            return self.avatar_url
        else:
            return resolve_url("pydenticon_image", self.username)

    def send_welcome_email(self):
        subject = render_to_string(
            "accounts/welcome_email_subject.txt", {"user": self, }
        )

        content = render_to_string(
            "accounts/welcome_email_content.txt", {"user": self, }
        )
        sender_email = settings.WELCOME_EMAIL_SENDER
        send_mail(subject, content, sender_email, [
                  self.email], fail_silently=False)


class Group(BaseModel):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='accounts_user_set', on_delete=models.CASCADE, verbose_name='사용자아이디')
    group = models.ForeignKey(
        Group, related_name="accounts_group_set", on_delete=models.CASCADE, verbose_name='그룹아이디')
    use_yn = models.CharField(
        max_length=1, verbose_name='사용여부', choices=UseChoices.choices)

    class Meta:
        verbose_name = '계정그룹정보'
        verbose_name_plural = '계정그룹정보'
        constraints = [
            models.UniqueConstraint(
                fields=["user", "group"],
                name="accounts_group_ux"
            ),
        ]
