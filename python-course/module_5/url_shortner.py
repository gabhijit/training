from base62_encoding import shorten_url

from flask import Flask, request, redirect, render_template

all_urls = dict()

app = Flask(__name__)

def validate_url(str):
    ### implement validate URL -
    ### Perform simple validation
    return True

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/shorten', methods=['GET', 'POST'])
def shorten():
    if request.method == 'POST':
        url = request.form['url']
        if not validate_url(url):
            return "Invalid Url {}".format(url), 400
        print url, type(url)
        shortened_url = shorten_url(url)

        all_urls[shortened_url] = url

        full_url = 'http://localhost:5000/' + shortened_url
        return  ("shortened url is {}".format(full_url), 200)
    else:
        return render_template('shorten.html')

@app.route('/<string:url_id>', methods=['GET'], strict_slashes=False)
def redir(url_id):
    try:
        to_url = all_urls[url_id]
    except KeyError:
        return ("Url {} Not found".format(request.url), 404)

    return redirect(to_url, code=302)

if __name__ == '__main__':
    app.run()
