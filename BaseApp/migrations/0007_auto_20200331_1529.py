# Generated by Django 3.0.3 on 2020-03-31 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BaseApp', '0006_question_responders'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='responders',
            field=models.ManyToManyField(related_name='questions', to='BaseApp.UserProfile'),
        ),
    ]