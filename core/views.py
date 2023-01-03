from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import CountrySerializer
from .models import Country
from .scrape import get_country_info


class CountryViewSet(viewsets.ViewSet):
    def list(self, request):
        country_name = request.query_params.get("country_name")

        if not country_name:
            return Response({"error": "Please provide a country name."})

        try:
            country_info = get_country_info(country_name)
        except Exception as e:
            return Response({"error": str(e)})

        # Create a Country object with the scraped data
        capital = (
            ",".join(country_info["capital"]) if country_info.get("capital") else None
        )
        largest_city = (
            ",".join(country_info["largest_city"])
            if country_info.get("largest_city")
            else None
        )
        official_languages = (
            ",".join(country_info["official_languages"])
            if country_info.get("official_languages")
            else None
        )
        area_total = float(country_info["area_total"].replace(",", ""))
        population = int(country_info["population"].replace(",", ""))

        country = Country(
            name=country_info["name"],
            flag_link=country_info["flag_link"],
            capital=capital,
            gdp_nominal=country_info["gdp_nominal"],
            area_total=area_total,
            population=population,
            largest_city=largest_city,
            official_languages=official_languages,
        )

        serializer = CountrySerializer(country)
        return Response(serializer.data)
