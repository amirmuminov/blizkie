# Generated by Django 3.0.4 on 2020-03-27 21:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myauth', '0001_initial'),
        ('patient', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='parent_user', serialize=False, to=settings.AUTH_USER_MODEL)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient.City')),
                ('lss', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient.LevelSelfServ')),
                ('meal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient.Meal')),
                ('mobility', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient.Mobility')),
                ('ms', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient.MentalState')),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient.Place')),
                ('toilet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient.Toilet')),
            ],
        ),
    ]
