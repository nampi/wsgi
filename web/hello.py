def application(environ, start_response):
        status = '200 OK'
        headers = [
            ('Content-Type', 'text/plain')
        ]
        queryString = environ('QUERY_STRING').split('&')
        start_response(status, headers)
        body = ''
        for i in queryString:
            body += i + '\n'
        return body
