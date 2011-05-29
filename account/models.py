from google.appengine.ext import db
from app import (BACKENDS, PICASA_BACKEND, FLICKR_BACKEND,
    THUMB_SIZES, THUMB_SIZE_DEFAULT, THUMB_CROPPED_DEFAULT,
    FULL_SIZES, FULL_SIZE_DEFAULT, HOMEPAGE_SIZE_DEFAULT, )


class Account(db.Model):
    user = db.UserProperty(required=True)
    
    photo_backend = db.StringProperty(choices=BACKENDS, default=PICASA_BACKEND,
        required=True)
    
    site_title = db.StringProperty(default='photo')
    site_header = db.StringProperty(default='photo')
    
    thumb_size = db.IntegerProperty(choices=THUMB_SIZES, default=THUMB_SIZE_DEFAULT, required=True)
    thumb_cropped = db.BooleanProperty(default=THUMB_CROPPED_DEFAULT, required=True)
    
    full_size = db.IntegerProperty(choices=FULL_SIZES, default=FULL_SIZE_DEFAULT, required=True)
    
    homepage_size = db.IntegerProperty(choices=FULL_SIZES, default=HOMEPAGE_SIZE_DEFAULT, required=True)
    homepage_album = db.StringProperty()
    
    featured_albums = db.StringListProperty()
    
    picasa_id = db.StringProperty(default='default')
    flickr_id = db.StringProperty()
    
    merchant_id = db.StringProperty()
    analytics_id = db.StringProperty()
    
    def _get_service_username(self):
        if self.photo_backend == PICASA_BACKEND:
            return self.picasa_id
        elif self.photo_backend == FLICKR_BACKEND:
            return self.flickr_id
        else:
            return None
    def _set_service_username(self, id):
        if self.photo_backend == PICASA_BACKEND:
            self.picasa_id = id
        elif self.photo_backend == FLICKR_BACKEND:
            self.flickr_id = id
        else:
            return None
    service_username = property(_get_service_username, _set_service_username)
    
    def _backend(self):
        if not hasattr(self, '_cached_backend'):
            import datasource
            if self.photo_backend == PICASA_BACKEND:
                self._cached_backend = datasource.PicasaDataSource(self)
            elif self.photo_backend == FLICKR_BACKEND:
                self._cached_backend = datasource.FlickrDataSource(self)
            else:
                self._cached_backend = None
        return self._cached_backend
    backend = property(_backend)
    
    def __repr__(self):
        return unicode(self)
    
    def __unicode__(self):
        return u'Account for %s' % self.user
