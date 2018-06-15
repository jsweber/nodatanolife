from flask import render_template, jsonify
import os 
import sys

parentDir = os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
sys.path.insert(0, parentDir)
from main import main

@main.app_errorhandler(404)
def page_not_found(e):
    if request.accept_mimeTypes.accept_json and not request.accept_mimeTypes.accept_html:
        resp = jsonify({error: 'not found'})
        resp.status_code = 404
        return resp

    return render_template('404.html'), 404

@main.app_errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

if __name__ == '__main__':
    pass

