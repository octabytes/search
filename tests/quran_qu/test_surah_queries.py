from search.nlp.quran_qu import QuranQU

# Queries
#
# user_query = "surah al-baqarah ayat 1"
# user_query = "surah baqra ayat 1"
# user_query = "surah-al-baqarah ayah 1"
# user_query = "al-baqarah ayah 1"
# user_query = "surat-ul-baqarah ayah 1"
# user_query = "surah al-baqarah ayah from 1 to 5"


def test_query1():
    user_query = "surah al-baqarah ayat 1"
    quran_qu = QuranQU()
    result = quran_qu.analyze(user_query)

    assert result['collection'] == "quran"
    assert result["score"] >= 100
    if result['filters'][0]['name'] == "surah":
        assert result['filters'][0]['name'] == "surah"
        assert result['filters'][0]['number'] == 2
        assert result['filters'][1]['name'] == "ayah"
        assert result['filters'][1]['number'] == 1
    else:
        assert result['filters'][0]['name'] == "ayah"
        assert result['filters'][0]['number'] == 1
        assert result['filters'][1]['name'] == "surah"
        assert result['filters'][1]['number'] == 2


def test_query2():
    user_query = "surah baqra ayat 1"
    quran_qu = QuranQU()
    result = quran_qu.analyze(user_query)

    assert result['collection'] == "quran"
    assert result["score"] >= 100
    if result['filters'][0]['name'] == "surah":
        assert result['filters'][0]['name'] == "surah"
        assert result['filters'][0]['number'] == 2
        assert result['filters'][1]['name'] == "ayah"
        assert result['filters'][1]['number'] == 1
    else:
        assert result['filters'][0]['name'] == "ayah"
        assert result['filters'][0]['number'] == 1
        assert result['filters'][1]['name'] == "surah"
        assert result['filters'][1]['number'] == 2


def test_query3():
    user_query = "surah-al-baqarah ayah 1"
    quran_qu = QuranQU()
    result = quran_qu.analyze(user_query)

    assert result['collection'] == "quran"
    assert result["score"] >= 100
    if result['filters'][0]['name'] == "surah":
        assert result['filters'][0]['name'] == "surah"
        assert result['filters'][0]['number'] == 2
        assert result['filters'][1]['name'] == "ayah"
        assert result['filters'][1]['number'] == 1
    else:
        assert result['filters'][0]['name'] == "ayah"
        assert result['filters'][0]['number'] == 1
        assert result['filters'][1]['name'] == "surah"
        assert result['filters'][1]['number'] == 2


def test_query4():
    user_query = "al-baqarah ayah 1"
    quran_qu = QuranQU()
    result = quran_qu.analyze(user_query)

    assert result['collection'] == "quran"
    assert result["score"] >= 100
    if result['filters'][0]['name'] == "surah":
        assert result['filters'][0]['name'] == "surah"
        assert result['filters'][0]['number'] == 2
        assert result['filters'][1]['name'] == "ayah"
        assert result['filters'][1]['number'] == 1
    else:
        assert result['filters'][0]['name'] == "ayah"
        assert result['filters'][0]['number'] == 1
        assert result['filters'][1]['name'] == "surah"
        assert result['filters'][1]['number'] == 2


def test_query5():
    user_query = "surat-ul-baqarah ayah 1"
    quran_qu = QuranQU()
    result = quran_qu.analyze(user_query)

    assert result['collection'] == "quran"
    assert result["score"] >= 100
    if result['filters'][0]['name'] == "surah":
        assert result['filters'][0]['name'] == "surah"
        assert result['filters'][0]['number'] == 2
        assert result['filters'][1]['name'] == "ayah"
        assert result['filters'][1]['number'] == 1
    else:
        assert result['filters'][0]['name'] == "ayah"
        assert result['filters'][0]['number'] == 1
        assert result['filters'][1]['name'] == "surah"
        assert result['filters'][1]['number'] == 2


def test_query6():
    user_query = "surah al-baqarah ayah from 1 to 5"
    quran_qu = QuranQU()
    result = quran_qu.analyze(user_query)

    assert result['collection'] == "quran"
    assert result["score"] >= 100
    assert result['filters'][0]['name'] == "surah"
    assert result['filters'][0]['number'] == 2
    assert result['range']["from"] == 1
    assert result['range']["to"] == 5
