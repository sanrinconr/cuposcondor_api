import datetime

SECRET_KEY = "weofijweofj34wfjw8uf29fuw9"
JSON_SORT_KEYS = False
JWT_SECRET_KEY = "t1NP63m4wnBg6nyHYKfmc2TpCOGI4nss"
JWT_ACCESS_TOKEN_EXPIRES = datetime.timedelta(seconds=1800)
JWT_REFRESH_TOKEN_EXPIRES = datetime.timedelta(days=2)
JWT_ACCESS_CSRF_HEADER_NAME = "X-CSRF-TOKEN-ACCESS"
JWT_REFRESH_CSRF_HEADER_NAME = "X-CSRF-TOKEN-REFRESH"
PROPAGATE_EXCEPTIONS = True
