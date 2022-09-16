# Generated by Django 4.1 on 2022-09-14 16:30

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0003_menu_lft_menu_rght_menu_tree_id'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='menu',
            options={'ordering': ['tree_id', 'lft']},
        ),
        migrations.AlterField(
            model_name='group',
            name='group_desc',
            field=models.CharField(max_length=1000, verbose_name='메뉴그룹설명'),
        ),
        migrations.AlterField(
            model_name='group',
            name='group_id',
            field=models.CharField(max_length=10, primary_key=True, serialize=False, verbose_name='메뉴그룹아이디'),
        ),
        migrations.AlterField(
            model_name='group',
            name='group_nm',
            field=models.CharField(max_length=30, verbose_name='메뉴그룹명'),
        ),
        migrations.AlterField(
            model_name='group',
            name='ord_seq',
            field=models.IntegerField(verbose_name='순번'),
        ),
        migrations.AlterField(
            model_name='group',
            name='use_yn',
            field=models.CharField(max_length=1, verbose_name='사용여부'),
        ),
        migrations.AlterField(
            model_name='menu',
            name='icon',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='메뉴 아이콘'),
        ),
        migrations.AlterField(
            model_name='menu',
            name='level',
            field=models.IntegerField(verbose_name='메뉴레벨'),
        ),
        migrations.AlterField(
            model_name='menu',
            name='menu_id',
            field=models.CharField(max_length=10, primary_key=True, serialize=False, verbose_name='메뉴아이디'),
        ),
        migrations.AlterField(
            model_name='menu',
            name='menu_nm',
            field=models.CharField(max_length=500, verbose_name='메뉴명'),
        ),
        migrations.AlterField(
            model_name='menu',
            name='menu_url',
            field=models.CharField(max_length=1000, verbose_name='메뉴 URL'),
        ),
        migrations.AlterField(
            model_name='menu',
            name='ord_seq',
            field=models.IntegerField(verbose_name='순번'),
        ),
        migrations.AlterField(
            model_name='menu',
            name='parent',
            field=mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='menu.menu', verbose_name='상위아이디'),
        ),
        migrations.AlterField(
            model_name='menu',
            name='use_yn',
            field=models.CharField(max_length=1, verbose_name='사용여부'),
        ),
        migrations.AlterField(
            model_name='menuauth',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='menu_group_set', to='menu.group', verbose_name='메뉴그룹아이디'),
        ),
        migrations.AlterField(
            model_name='menuauth',
            name='menu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='menu_set', to='menu.menu', verbose_name='메뉴아이디'),
        ),
    ]
