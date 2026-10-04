from anime_parsers_ru import AnimegoParser, KodikParser, ShikimoriParser


anime_search="Re:Zero"

kparser=KodikParser(token="56a768d08f43091901c44b54fe970049")
Aniparser=AnimegoParser()
shiparser=ShikimoriParser()

dataS=shiparser.search(anime_search)

for anime in dataS:
    print(f"{anime["title"]}")
