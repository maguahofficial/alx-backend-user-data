#!/usr/bin/env python3
""" The Module of Index views
"""
from flask import jsonify, abort
from api.v1.views import app_views


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status() -> str:
    """ GET /api/v1/status
    Function returns:
      - the status of the API
    """
    return jsonify({"status": "OK"})


@app_views.route('/unauthorized', methods=['GET'], strict_slashes=False)
def unauthorized() -> str:
    """ The endpoint to testing (unauthorized) 401 error handler """
    abort(401)


@app_views.route('/forbidden', methods=['GET'], strict_slashes=False)
def forbidden() -> str:
    """ The endpoint to testing (forbidden) 403 error handler """
    abort(403)


@app_views.route('/stats/', strict_slashes=False)
def stats() -> str:
    """ Function GET /api/v1/stats
    This Returns:
      - the number of each objects
    """
    from models.user import User
    stats = {}
    stats['users'] = User.count()
    return jsonify(stats)
