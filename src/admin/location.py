from wtforms.validators import DataRequired

from src.admin.commons.base import BaseAdmin
from src.location.models import City, Country, Region


class CountryAdmin(BaseAdmin, model=Country):
    category = "Локації"
    name_plural = "Країни"
    icon = "fa-solid fa-earth-europe"

    column_list = form_columns = column_details_list = [
        Country.name,
    ]
    column_labels = {
        Country.name: "Країна",
    }


class RegionAdmin(BaseAdmin, model=Region):
    category = "Локації"
    name_plural = "Області та регіони"
    icon = "fa-solid fa-map-location-dot"

    column_list = form_columns = [
        Region.country,
        Region.name,
    ]
    column_labels = {
        Region.country: "Країна",
        Region.name: "Область",
        Region.cities: "Міста / Поселення",
    }
    column_details_list = [
        Region.country,
        Region.name,
        # Region.cities,
    ]
    form_args = {
        "country": {
            "validators": [DataRequired()],
        },
    }
    form_ajax_refs = {
        "country": {
            "fields": ("name",),
            "order_by": "name",
        },
    }
    column_searchable_list = [
        Region.name,
    ]


class CityAdmin(BaseAdmin, model=City):
    category = "Локації"
    name_plural = "Міста та поселення"
    icon = "fa-solid fa-location-dot"

    column_labels = {
        City.country: "Країна",
        City.region: "Область",
        City.name: "Населений пункт",
        City.latitude: "Широта",
        City.longitude: "Довгота",
        City.administrative_code: "Адміністративний код",
    }
    column_list = column_details_list = form_columns = [
        City.country,
        City.region,
        City.name,
        City.latitude,
        City.longitude,
        City.administrative_code,
    ]
    form_args = {
        "country": {
            "validators": [DataRequired()],
        },
        "region": {
            "validators": [DataRequired()],
        },
        "latitude": {
            "validators": [DataRequired()],
        },
        "longitude": {
            "validators": [DataRequired()],
        },
    }
    form_ajax_refs = {
        "country": {
            "fields": ("name",),
            "order_by": "name",
        },
        "region": {
            "fields": ("name",),
            "order_by": "name",
        },
    }
    column_searchable_list = [
        City.name,
    ]
