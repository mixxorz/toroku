web: sed -i "s/PORT/${PORT}/g" tor/torrc; tor -f tor/torrc; waitress-serve --port=$PORT toroku.wsgi:application
