#!/usr/bin/env python3
from flask import Flask, redirect, request, render_template, make_response
from urlshortener import UrlShortener
import config
from urllib.parse import urlparse


app = Flask(__name__)
app.config['DEBUG'] = config.FLASK_DEBUG
app.config['ENV'] = config.FLASK_ENV

shorty = UrlShortener()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/<shortUrl>')
def redir(shortUrl):
    fullUrl = shorty.findEntry(shortUrl)
    if not fullUrl:
        return redirect('/404')
    else:
        return redirect(fullUrl)


@app.route('/404')
def notFound():
    return render_template('notFound.html')


@app.route('/400')
def badRequest():
    return render_template('badRequest.html')

###
# todo: improve URL validation
###


@app.route('/', methods=['POST'])
def shortenUrl():
    if request.form and 'url' in request.form:
        originalUrl = urlparse(request.form['url'])
        if any([originalUrl.scheme, originalUrl.netloc, originalUrl.path]):
            if originalUrl.netloc == '':
                url = 'http://' + request.form['url']
            else: url = request.form['url']
            response = shorty.newUrl(url)
            response['originalUrl'] = request.form['url']
            return render_template('shortened.html', result=response)
        else: return redirect('/400')
    else: return redirect('/400')

if __name__ == '__main__':
    app.run(host = config.FLASK_HOST, 
            port = config.FLASK_PORT)
    