from anime_parsers_ru import AnimegoParser, KodikParser, ShikimoriParser, errors
import os
import io
import contextlib


def parsers(anime_search):

    shiparser = ShikimoriParser()
    dataS = shiparser.search(anime_search)

    ids = list()
    for x in dataS:
        ids.append(x["shikimori_id"])

    with (
        contextlib.redirect_stdout(io.StringIO()),
        contextlib.redirect_stderr(io.StringIO()),
    ):
        kparser = KodikParser(token="56a768d08f43091901c44b54fe970049")
    aniparser = AnimegoParser()
    anime_infoK = list()
    anime_infoA = list()

    for id in ids:
        try:
            dataK = kparser.search_by_id(id=id, id_type="shikimori")
        except errors.NoResults:
            dataK = None
        if dataK:
            anime_infoK.append(dataK[0])
        else:
            continue

    dataA = aniparser.search(anime_search)
    if dataA:
        for data in dataA:
            anime_infoA.append(data)
    for anime in anime_infoK:
        print(f"{anime['title']} {anime['material_data']['poster_url']}")
    print()
    for anime in anime_infoA:
        print(f"{anime['title']} {anime['image']} ")


if __name__ == "__main__":
    os.system("clear")
    anime_search = input()

    parsers(anime_search)
