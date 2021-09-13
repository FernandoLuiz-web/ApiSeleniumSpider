from flask import Flask, request, jsonify
from Webdriver.webservices import WebService


app = Flask(__name__)


@app.route("/teste")
def test():
    return jsonify({
        'Success': 'working API!'
    }), 200


@app.route("/selenium")
def Selenium_search():
    site = request.headers['site']
    response = WebService.Selenium_site(site)
    return jsonify({
        'Website_information': response
    })


@app.route("/playwright")
def Playwright_search():
    site = request.headers['site']
    response = WebService.Playwright_site(site)
    return jsonify({
        'Website_information': response
    })


if __name__ == "__main__":
    app.run(debug=True)