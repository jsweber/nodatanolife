from flask import jsonify

def forbidden(message):
    resp = jsonify({error:'forbidden', message:message})
    resp.status_code = 403
    return resp
