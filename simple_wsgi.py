def hello_page(env, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [b"""
                <html><h1>Help</h1>
                    <p>Hello world!</p>
                        <ul>
                            <li>
                                <a href="/">Main page</a>
                            </li>    
                            <li>
                                <a href="/hello/help">Help for Hello world</a>
                            </li>
                       </ul>                                             
                </html>"""
            ]


def help_page(env, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [b"""
                <html><h1>Help</h1>
                    <p>Help page for Hello world</p>
                        <ul>
                            <li>
                                <a href="/">Main page</a>
                            </li>    
                            <li>
                                <a href="/hello">Hello world</a>
                            </li>
                       </ul>                                             
                </html>"""
            ]


def main_page(env, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [b"""
                <html><h1>Main</h1>
                    <p>The main page</p>
                        <a href="/hello">Hello world</a>
                </html>"""
            ]


def not_found(env, start_response):
    start_response('404 Not Found', [('content-type', 'text/html')])
    return [b"""
                <html><h1>Page not Found</h1>
                    <p>
                        This url is not supported. 
                        Return to the <a href="/">Main page</a>
                    </p>
                 </html>"""
            ]


routes = [('/hello', hello_page),
          ('/hello/help', help_page),
          ('/', main_page)
          ]


def application(env, start_response):
    for path, app in routes:
        if env['PATH_INFO'].endswith(path):
            return app(env, start_response)

    return not_found(env, start_response)


