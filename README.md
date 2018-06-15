The purpose of this project is to learn and practice.
As this was my first time using Python3 and Flask to build a small application I've took some ideas from: [pyr/url-shortener]

# tURL

Simple URL shortener using:
* [Python3] 
* [Flask]
* [Redis]

## How it works?
1. Calculate MD5 of the original URL
2. Convert it to base64. Taking care of using only URL-valid characters.
3. Crop the base64 (actually not 64 because not all characters are URL-valid) to 8 characters. This gives 64⁸  ≃ 280 trillion possible combinations.

### Flaws
Collisions are not detected/managed ~~, yet~~.

## Running it

### 1. Setup Redis:
Fastest way is to use [Docker]:
```
$ docker run -itd -p 6379:6379 redis:alpine
```
So now we have a Redis DB listening on `localhost:6379`. 
By default no credentials are set. So you can acces the DB with 
```
$ redis-cli 
127.0.0.1:6379> 
```
### 2. Start the server:
```
$ ./turl.py
```
By default ``FLASK_PORT = 5001``. Update it in ``config.py`` or set the set the env var ``FLASK_PORT`` to change it.

### 3. Access:
Access ``localhost:5001`` (or ``FLASK_HOST:FLASK_PORT``) with a browser.

License
----

GNU GPLv3

[Python3]: <https://www.python.org/download/releases/3.0/>
[Redis]: <https://redis.io/>
[Flask]: <http://flask.pocoo.org/>
[pyr/url-shortener]: <https://github.com/pyr/url-shortener>
[Docker]: <https://www.docker.com/>
