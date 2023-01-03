from rest_framework import serializers
from .models import Country


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = "__all__"

    def to_representation(self, instance):
        data = super().to_representation(instance)
        del data["id"]

        if data["capital"]:
            capitals = data["capital"].split(",")
            data["capital"] = capitals if len(capitals) > 1 else capitals[0]
        else:
            del data["capital"]

        if data["largest_city"]:
            cities = data["largest_city"].split(",")
            data["largest_city"] = cities if len(cities) > 1 else cities[0]
        else:
            del data["largest_city"]

        if data["official_languages"]:
            languages = data["official_languages"].split(",")
            data["official_languages"] = (
                languages if len(languages) > 1 else languages[0]
            )
        else:
            del data["official_languages"]

        return data
