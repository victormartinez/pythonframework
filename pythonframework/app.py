from typing import Any, Callable, Dict, Iterable


def application(environ: Dict[str, Any], start_response: Callable) -> Iterable[bytes]:
    """
    Returns an iterable of bytes that represent the server response.
        Parameters:
            environ (dict): dictionary with request metadata
            start_response (callable): callback responsible for processing response

        Returns:
            response (iterable[bytes]): binary string of the response
    """
    HELLO_WORLD = b"HELLO, WORLD!"

    status = "200 OK"
    response_headers = [
        ("Content-type", "text/plain"),
        ("Content-Length", str(len(HELLO_WORLD))),
    ]
    start_response(status, response_headers)
    yield HELLO_WORLD
