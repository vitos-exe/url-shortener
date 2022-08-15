import hashlib
from flask import request
from urllib.parse import urlparse 

def extract_first_element(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if result is not None:
            result = result[0]
        return result
    return wrapper

def get_redirect_url_for_fragment(fragment):
    return f'{request.host}/{fragment}'

def url_is_valid(url):
   return bool(urlparse(url).scheme)

# This is the most basic option, better use something more smart
def get_original_url_fragment(url):
    return hashlib.md5(url.encode()).hexdigest()[:6]
 
