# Generated by Django 4.1 on 2022-09-14 16:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0004_alter_menu_options_alter_group_group_desc_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='group',
            options={'verbose_name': '그룹정보'},
        ),
        migrations.AlterModelOptions(
            name='menu',
            options={'ordering': ['tree_id', 'lft'], 'verbose_name': '메뉴정보'},
        ),
        migrations.AlterModelOptions(
            name='menuauth',
            options={'verbose_name': '메뉴권한정보'},
        ),
        migrations.RemoveConstraint(
            model_name='menuauth',
            name='menu_group_ux',
        ),
        migrations.AlterModelTable(
            name='menuauth',
            table=None,
        ),
    ]