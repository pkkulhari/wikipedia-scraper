from bs4 import BeautifulSoup
import requests
import re


def get_country_info(country_name):
    url = f"https://en.wikipedia.org/wiki/{country_name}"
    html = requests.get(url).text
    soup = BeautifulSoup(html, "html.parser")

    # Scrape the data from the infobox on the right side of the Wikipedia page
    try:
        infobox = soup.find("table", {"class": "infobox"})
        rows = infobox.find_all("tr")
    except:
        raise Exception("Could not find the infobox on the Wikipedia page.")

    data = {}
    data["name"] = infobox.find("div", {"class": "fn org country-name"}).text.strip()

    flag_link = infobox.find("img").get("src")
    data["flag_link"] = f"https:{flag_link.split('.svg')[0].replace('thumb', '')}.svg"

    for index, row in enumerate(rows):
        try:
            heading = row.find("th").text.strip()

            if "capital" in heading.lower():
                key = "capital"
                links = row.find("td").find_all("a")

                value = []
                for link in links:
                    if link.get("title") is not None:
                        value.append(link.text.strip())

                if "largest city" in heading.lower():
                    data["largest_city"] = value

            elif "largest city" in heading.lower():
                key = "largest_city"
                links = row.find("td").find_all("a")

                value = []
                for link in links:
                    if link.get("title") is not None:
                        value.append(link.text.strip())

            elif heading == "GDP (nominal)":
                key = "gdp_nominal"
                value = re.split(r"\[\d+\]", rows[index + 1].find("td").text.strip())[0]

            elif heading == "Area":
                key = "area_total"
                value = rows[index + 1].find("td").contents[0].strip().replace("km", "")

            elif heading == "Population":
                key = "population"
                value = re.split(
                    r"\[\d+\]", rows[index + 1].find("td").text.strip().split(" ")[0]
                )[0]

            elif "official" in heading.lower() and "language" in heading.lower():
                key = "official_languages"
                links = row.find("td").find_all("a")

                value = []
                for link in links:
                    if link.get("title") is not None:
                        value.append(link.text.strip())

            else:
                continue

            data[key] = value
        except:
            pass

    return data
