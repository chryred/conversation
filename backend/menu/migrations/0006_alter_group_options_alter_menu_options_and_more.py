# Generated by Django 4.1 on 2022-09-14 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0005_alter_group_options_alter_menu_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='group',
            options={'verbose_name': '그룹정보', 'verbose_name_plural': '그룹정보'},
        ),
        migrations.AlterModelOptions(
            name='menu',
            options={'ordering': ['tree_id', 'lft'], 'verbose_name': '메뉴정보', 'verbose_name_plural': '메뉴정보'},
        ),
        migrations.AlterModelOptions(
            name='menuauth',
            options={'verbose_name': '메뉴권한정보', 'verbose_name_plural': '메뉴권한정보'},
        ),
        migrations.AlterField(
            model_name='group',
            name='use_yn',
            field=models.CharField(choices=[('Y', '예'), ('N', '아니오')], max_length=1, verbose_name='사용여부'),
        ),
        migrations.AlterField(
            model_name='menu',
            name='use_yn',
            field=models.CharField(choices=[('Y', '예'), ('N', '아니오')], max_length=1, verbose_name='사용여부'),
        ),
    ]