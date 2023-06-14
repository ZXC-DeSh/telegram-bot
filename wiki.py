import wikipedia

def get_wiki_artile(article):
    wikipedia.set_lang('ru')

    try:
        return f'{wikipedia.summary(article)} {wikipedia.page(article).links}'[:4000]
    except wikipedia.WikipediaException:
        return 'Не удалось найти информацию по данному запросу'