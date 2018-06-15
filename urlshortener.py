#!/usr/bin/env python3
import base64
import redis
from hashlib import md5
import config

class UrlShortener:    
    def __init__(self):
        self.r = redis.StrictRedis(host = config.REDIS_HOST,
                                   port = config.REDIS_PORT,
                                   db = config.REDIS_DB)

    
    def urlShorten(self, fullUrl):
        h = md5()
        h.update(fullUrl.encode('ascii'))
        hexDigest = h.hexdigest()
        shortUrl = base64.urlsafe_b64encode(hexDigest.encode('ascii'))[:8].decode('ascii')
        return shortUrl


    # input: shortUrl to lookup
    # return False if not exists or fullUrl if exists
    def findEntry(self, target):
        #val = self.r.exists(target)
        if self.r.exists(target):
            val = self.r.hmget(target, 'fullUrl')        
            return str(val[0].decode('ascii'))
        else:
            return False

    #if key increment and return hit, else create with hit = 1 
    def newUrl(self, url):
        d = {}
        shortUrl = self.urlShorten(url)
        entryExists = self.findEntry(shortUrl)
        if entryExists: 
            d['hits'] = self.r.hincrby(shortUrl, 'hits', '1')   
        else: 
            d['hits'] = 1
            self.r.hmset(shortUrl, {'fullUrl': url, 'hits': 1})
            #return 1
        d['shortUrl'] = shortUrl
        return d

# x = UrlShortener()
# x.newUrl('http://google.com/foobare.html')
# print(x.findEntry('OWZmMjY0'))