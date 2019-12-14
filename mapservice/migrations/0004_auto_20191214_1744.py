# Generated by Django 3.0 on 2019-12-14 16:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_post_likes'),
        ('mapservice', '0003_eatingplace_posts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eatingplace',
            name='posts',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='EatingPlace', to='blog.Post'),
        ),
    ]