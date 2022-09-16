from tabnanny import verbose
from django.db import models
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel
from common.models import BaseModel, UseChoices


class Group(BaseModel):
    group_id = models.CharField(
        max_length=10, primary_key=True, verbose_name="메뉴그룹아이디")
    group_nm = models.CharField(max_length=30, verbose_name="메뉴그룹명")
    group_desc = models.CharField(max_length=1000, verbose_name="메뉴그룹설명")
    ord_seq = models.IntegerField(verbose_name="순번")
    use_yn = models.CharField(
        max_length=1, verbose_name="사용여부", choices=UseChoices.choices)

    class Meta:
        verbose_name = '그룹정보'
        verbose_name_plural = '그룹정보'

    def __str__(self):
        return self.group_nm


class Menu(MPTTModel, BaseModel):
    menu_id = models.CharField(
        max_length=10, primary_key=True, verbose_name="메뉴아이디")
    parent = TreeForeignKey('self', verbose_name=(
        '상위아이디'), blank=True, null=True, related_name='children', db_index=True, on_delete=models.CASCADE)
    menu_nm = models.CharField(max_length=500, verbose_name="메뉴명")
    icon = models.CharField(max_length=20, blank=True,
                            null=True, verbose_name="메뉴 아이콘")
    menu_url = models.CharField(max_length=1000, verbose_name="메뉴 URL")
    level = models.IntegerField(verbose_name="메뉴레벨")
    ord_seq = models.IntegerField(verbose_name="순번")
    use_yn = models.CharField(
        max_length=1, verbose_name="사용여부", choices=UseChoices.choices)

    class Meta:
        verbose_name = '메뉴정보'
        verbose_name_plural = '메뉴정보'
        ordering = ['tree_id', 'lft']

    class MPTTMeta:
        order_insertion_by = ['menu_nm']

    def __str__(self):
        return self.menu_nm


class MenuAuth(BaseModel):
    menu = models.ForeignKey(
        Menu, related_name="menu_set", on_delete=models.CASCADE, verbose_name="메뉴아이디")
    group = models.ForeignKey(
        Group, related_name="menu_group_set", on_delete=models.CASCADE, verbose_name="메뉴그룹아이디")

    class Meta:
        db_table = "menu_auth"
        constraints = [
            models.UniqueConstraint(
                fields=["menu", "group"],
                name="menu_group_ux"
            ),
        ]

    class Meta:
        verbose_name = '메뉴권한정보'
        verbose_name_plural = '메뉴권한정보'
