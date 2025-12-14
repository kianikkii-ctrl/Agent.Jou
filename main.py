import urllib.request
import xml.etree.ElementTree as ET

# RSS-feed (XML)
RSS_URL = "https://www.demorgen.be/rss.xml"

def haal_nieuws_op():
    """
    Haalt artikels op uit de RSS XML-feed
    """
    with urllib.request.urlopen(RSS_URL) as response:
        data = response.read()

    root = ET.fromstring(data)
    items = []

    for item in root.findall(".//item"):
        titel = item.findtext("title", "")
        beschrijving = item.findtext("description", "")
        items.append({
            "titel": titel,
            "beschrijving": beschrijving
        })

    return items

# -------------------------------
# Custom GPT / GEM simulatie
# -------------------------------
def custom_gpt_samenvatting(nieuws_items, max_items=5):
    """
    Simuleert een Custom GPT of GEM.
    Selecteert belangrijkste items en genereert een journalistieke samenvatting.
    """
    samenvatting = []

    for item in nieuws_items[:max_items]:
        titel = item['titel']
        beschrijving = item['beschrijving']

        # Simuleer journalistieke relevantie
        kern = ""
        if "overeenkomst" in beschrijving.lower() or "akkoord" in beschrijving.lower():
            kern = "Belangrijk politiek nieuws, impact op beleid."
        elif "staking" in beschrijving.lower():
            kern = "Direct effect op burgers, praktisch relevant."
        elif "klimaat" in beschrijving.lower() or "energie" in beschrijving.lower():
            kern = "Milieu en toekomst van belang, relevant voor onderzoek."
        elif "technologie" in beschrijving.lower() or "AI" in beschrijving.lower():
            kern = "Innovatie en trends, interessant voor tech-lezers."
        else:
            kern = "Algemeen nieuws."

        samenvatting.append(f"- {titel}\n  Kern: {kern} ({beschrijving})")

    return samenvatting

def maak_nieuwsbrief(samenvatting):
    """
    Maakt een leesbare nieuwsbrief
    """
    nieuwsbrief = "DAGELIJKSE REDACTIENIEUWSBRIEF\n"
    nieuwsbrief += "=" * 50 + "\n\n"
    nieuwsbrief += "Selectie van het belangrijkste nieuws:\n\n"

    for punt in samenvatting:
        nieuwsbrief += punt + "\n\n"

    nieuwsbrief += "Automatisch samengesteld met Custom GPT/GEM-simulatie.\n"
    return nieuwsbrief

def main():
    nieuws = haal_nieuws_op()
    samenvatting = custom_gpt_samenvatting(nieuws)
    nieuwsbrief = maak_nieuwsbrief(samenvatting)

    # Print naar console
    print(nieuwsbrief)

    # Optioneel: opslaan als bestand
    with open("nieuwsbrief.txt", "w", encoding="utf-8") as f:
        f.write(nieuwsbrief)
    print("Nieuwsbrief opgeslagen als nieuwsbrief.txt")

if __name__ == "__main__":
    main()
