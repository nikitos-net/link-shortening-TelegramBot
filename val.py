import validators

def check_valid_url(url):
    return validators.url(url)
