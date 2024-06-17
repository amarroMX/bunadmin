from bunadmin.settings import LANGUAGES


def supported_languages(request):
    languages = {'languages': [lang[1] for lang in LANGUAGES]}
    return languages