# Generated by Django 4.1.5 on 2023-02-25 04:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0002_place_category_description_place_facilities_and_more'),
        ('itinerary', '0002_agenda_remove_itinerary_co_travellers_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agenda',
            name='place',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='agenda_place', to='places.place'),
        ),
    ]
