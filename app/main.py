from flask import Flask, render_template, request
from headerparse import headerParse
from httpstatus import httpStatus

app = Flask(__name__)



@app.route('/results', methods=['POST', 'GET'])
@app.route('/', methods=['POST', 'GET'])
def main():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        url_protocol = request.form.get('protocol')
        url_base =request.form.get('url')
        url_submitted = url_protocol + url_base
        
        dns_result = httpStatus.try_dns(url_base)
        
        if dns_result[0].isdigit():
            return_http = httpStatus.http_response(url_submitted)
            header_return = headerParse(return_http[2])
            return render_template(
                                'index.html',
                                url_submitted=url_submitted,
                                dns_result=dns_result,
                                http_code = return_http[0],
                                http_reason = return_http[1],
                                h_sts = header_return.parse_sts(),
                                h_xcto = header_return.parse_xcto(),
                                h_xfo = header_return.parse_xfo(),
                                h_csp = header_return.parse_csp(),
                                )
        else:
            return render_template(
                                'index.html',
                                url_submitted="invalid URL",
                                )


