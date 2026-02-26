# READER: rhtml
"""
rhtml.py - HTML reader
Part of the reader library
developed by StarShot Studios
"""

import urllib.request
import webbrowser
from . import rfiles

def get(url):
    """
    Returns the raw HTML content of the given URL.
    
    Args:
        url (str): URL of the website to read
        
    Returns:
        str: Raw HTML content, or None if URL is invalid
    """
    try:
        with urllib.request.urlopen(url) as response:
            html = response.read().decode('utf-8', errors='ignore')
    except:
        try:
            with urllib.request.urlopen("https://"+url) as response:
                html = response.read().decode('utf-8', errors='ignore')
        except:
            try:
                with urllib.request.urlopen("http://"+url) as response:
                    html = response.read().decode('utf-8', errors='ignore')
            except:
                return None
    return html

def browse(url):
    """
    Opens URL in preferred browser

    Args:
        url (str): URL of the site you would like to open
        
    Returns:
        bool: True if successful, False if unsuccessful
    """
    try:
        webbrowser.open(url)
        return True
    except:
        try:
            webbrowser.open("https://"+url)
            return True
        except:
            try:
                webbrowser.open("http://"+url)
                return True
            except:
                return False

def browseget(url):
    """
    Opens a new tab and returns raw HTML from URL

    Args:
        url (str): URL of the site you would like to access

    Returns:
        str: Raw HTML content, or None if URL is invalid
    """
    browse(url)
    return get(url)

def openjs(filename):
    """
    Attempts to run a .js (JavaScript) file

    Args:
        filename (str): Name of the file to open

    Returns:
        bool: True if successful, False if unsuccessful
    """
    if filename.endswith('.js'):
        rfiles.create("temp.html", content=f'<!DOCTYPE html><html><head><body><h3>Use inspect to see console</h3><script>{rfiles.read(filename)}</script></body></html>')
    else:
        rfiles.create("temp.html", content=f'<!DOCTYPE html><html><head><body><h3>Use inspect to see console</h3><script>{rfiles.read(filename)}.js</script></body></html>')
    try:
        webbrowser.open('temp.html')
        try:
            rfiles.run(filename)
        except:
            try:
                rfiles.run(filename+".js")
            except:
                pass
        rfiles.delete("temp"+".html")  # Because why not?
        return True
    except:
        return False

def openhtml(filename):
    """
    Attempts to run a .html (Web Site) file in a browser

    Args:
        filename (str): Name of the file to open

    Returns:
        bool: True if successful, False if unsuccessful
    """
    try:
        webbrowser.open(filename)
        return True
    except:
        try:
            webbrowser.open(filename+".html")
            return True
        except:
            return False
