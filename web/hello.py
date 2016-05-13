def application(environ, start_response):
        status = '200 OK'
        headers = [
            ('Content-Type', 'text/plain')
        ]
        start_response(status, headers)
        body = ''
        for i in queryStrig:
            rbody += i + '\n'
        return body
