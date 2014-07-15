__author__ = 'rm'

from google.appengine.ext import ndb


class Site(ndb.Model):
    site = ndb.StringProperty()
    url = ndb.StringProperty()


class Country(ndb.Model):
    country = ndb.StringProperty(indexed=True)


class Rate(ndb.Model):
    country = ndb.KeyProperty(kind=Country)
    cost = ndb.FloatProperty(indexed=False)
    cost_vat = ndb.FloatProperty(indexed=False)
    type = ndb.StringProperty(indexed=False)
    currency = ndb.StringProperty(indexed=False, default='USD')
    created = ndb.DateTimeProperty(auto_now_add=True, indexed=True)