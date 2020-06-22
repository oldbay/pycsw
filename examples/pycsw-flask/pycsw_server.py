import logging
import json

from flask import Flask, request, send_file

from pycsw import __version__ as pycsw_version
from pycsw.server import Csw

with open("config.json", "r") as file_:
    pycsw_config = json.load(file_)

LOGGER = logging.getLogger(__name__)
APP = Flask(__name__)


@APP.route('/csw', methods=['GET', 'POST'])
def csw_wrapper():
    """CSW wrapper"""

    LOGGER.info('Running pycsw %s', pycsw_version)

    my_csw = Csw(pycsw_config, request.environ, version='2.0.2')

    # dispatch the request
    http_status_code, response = my_csw.dispatch_wsgi()

    return response, http_status_code, {'Content-type': my_csw.contenttype}

@APP.route('/img', methods=['GET'])
def res_img():
    filename = request.query_string.decode()
    try:
        with open("resources/img/{}".format(filename), "rb") as file_:
            output = file_.read()
    except FileNotFoundError:
        return b'File not Found', 404, {'Content-type': 'text/plain'}
    else:
        return output, 200, {'Content-type': 'image/png'}

@APP.route('/src', methods=['GET'])
def res_src():
    filename = request.query_string.decode()
    try:
        return send_file(
            "resources/src/{}".format(filename),
            as_attachment=True
        )
    except FileNotFoundError:
        return b'File not Found', 404, {'Content-type': 'text/plain'}

if __name__ == "__main__":
    APP.run(host="0.0.0.0", port=3700, debug=True, threaded=True)