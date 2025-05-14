#                                                ERROR CODES AND THEIR MEANING.


#                                                1XX(Informational Responses)
# This indicates that the request was received, and it's being processed.
# 100 (Continue): This means that the server received the request headers and is waiting for the body.
# 101 (Switching Protocols): This means that the client requested a protocol switch. E.g. HTTP to web socket.
# 102 (Processing): This means that the server is still working on the request.


#                                                2XX(Success)
# 200 (Okay): This means the request was successful and the server returned data.
# 201 (Created): This means that a new resource was successfully created. E.g. After a POST request.
# 202 (Accepted): This means that the request was accepted, but it's still being accessed.
# 204 (No content): This means that the request was successful, but there's no response body.


#                                                3XX (Redirection)
# This means that the client must take further action
# 301 (Moved Permanently): This means the request has been permanently moved to a new url.
# 302 (Found): This means that the request has been temporarily moved to a new url.
# 304 (Not Modified): This means the requested resource has not changed (Often used with Caching).


#                                                4XX (Client Errors)
# This means something is wrong with the request.
# 400 (Bad Request): This means that the request is invalid. E.g. Missing Parameters.
# 401 (Unauthorised): This means the authentication failed.
# 403 (Forbidden): This means that the client doesn't have the permission to access the result.
# 404 (Not Found): This means the requested resource does not exist.
# 405 (Not Allowed): This means that method used not allowed (get, post, etc. is not allowed)
# 408 (Request Timeout): This means the server took too long to respond.
# 429 (Too Many Requests): This means the client sent too many requests in a short time.


#                                                 5XX (Server Error)
# This means something is wrong on the server.
# 500 (Internal Server Error): It is usually a generic error from the server.
# 502 (Bad Gateway): This means the server received an invalid response from another server.
# 503 (Service Not Available): It means that the server is overloaded or under maintenance.
# 504 (Gateway timeout): This means that the server did not receive a response from another server in time.