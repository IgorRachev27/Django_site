# Generated by Django 3.2.4 on 2021-07-09 14:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0002_auto_20210709_1417'),
    ]

    operations = [
        migrations.CreateModel(
            name='ComentCrm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coment_text', models.TextField(verbose_name='Текст комментария')),
                ('coment_dt', models.DateTimeField(auto_now=True, verbose_name='Дата создания')),
                ('coment_bimding', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.order', verbose_name='Заявка')),
            ],
            options={
                'verbose_name': 'Комментарий',
                'verbose_name_plural': 'Комментарии',
            },
        ),
    ]
