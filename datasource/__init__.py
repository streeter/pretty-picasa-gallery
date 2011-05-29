from django.conf import settings
from google.appengine.ext import db
from google.appengine.api import memcache

import flickr
import logging
log = logging.getLogger('gallery.' + __name__)


class PhotoBackend(object):
    
    user_id = None
    thumb_size = 72
    imgmax = 640
    thumb_cropped = True
    
    def __init__(self, user):
        self.user_id = user.GetUsername()
        self.thumb_size = user.thumb_size
        self.imgmax = user.full_size
        self.thumb_cropped = user.thumb_cropped
        
    
    def GetAllAlbums(self):
        return []
    
    def GetFeaturedAlbums(self, featured=[]):
        albums = self.GetAllAlbums()
        featured_albums = []
        for album in albums:
            if album['title'] not in featured:
                continue
            
            featured_albums.append(album)
        
        # Sort by name
        featured_albums.sort(key=lambda a: a['title'])
        
        if 'all' in featured:
            featured_albums.append({'id': 'all', 'title': 'all'})
        
        return featured_albums
    
    def GetPhotosInAlbum(self, album, featured=[]):
        return []
    
    def GetSinglePhoto(self, album, photo_id):
        return None
    
    def CacheGet(self, key):
        if not settings.MEMCACHE_ENABLED or not key:
            return None
        return memcache.get(key)
    
    def CacheSet(self, key, value):
        if not settings.MEMCACHE_ENABLED or not key:
            return True
        return memcache.set(key, value)
    
    def CacheClear(self):
        pass
    

class PicasaBackend(PhotoBackend):
    gdata = None
    
    ALBUM_FEED_URI = '/data/feed/api/user/%s/album/%s?kind=photo&thumbsize=%s&imgmax=%s'
    
    def __init__(self, user):
        PhotoBackend.__init__(self, user)
        
        import gdata.photos.service
        import gdata.alt.appengine
        
        self.gdata = gdata.photos.service.PhotosService()
        gdata.alt.appengine.run_on_appengine(self.gdata)
    
    def GetAllAlbums(self):
        logging.info('GetAllAlbums called')
        
        # check memcache
        key = 'picasa_albums'
        albums = self.CacheGet(key)
        if albums:
            return albums
        
        albums = []
        albums_feed = self.gdata.GetUserFeed(user=self.user_id, kind='album')
        for album in albums_feed.entry:
            albums.append({
                'id': album.gphoto_id.text,
                'title': album.title.text,
            })
        
        albums.sort(key=lambda a: a['title'])
        
        # set memcache
        self.CacheSet(key, albums)
        
        return albums
    
    def GetPhotosInAlbum(self, album, featured=[]):
        logging.info('GetPhotosInAlbum called')
        if self.thumb_cropped:
            thumb_size = "%dc" % self.thumb_size
        else:
            thumb_size = "%du" % self.thumb_size
        
        # check memcache
        key = "picasa_album_%s_%s_%s" % (album, thumb_size, self.imgmax)
        photos = self.CacheGet(key)
        if photos:
            return photos
        
        photos = []
        albums = []
        if album == 'all':
            all_albums = self.GetFeaturedAlbums(featured)
            for a in all_albums:
                albums.append(a['title'])
        else:
            albums.append(album)
        
        logging.info('Got albums %s' % str(albums))
        
        for a in albums:
            feed = self.ALBUM_FEED_URI % (self.user_id, a, thumb_size, self.imgmax)
            logging.info('GetPhotosInAlbum feed is %s' % feed)
            try:
                photos_feed = self.gdata.GetFeed(feed)
                for photo in photos_feed.entry:
                    pic = {
                        'id': photo.gphoto_id.text,
                        'height': photo.width.text,
                        'width': photo.height.text,
                        'thumb_url': photo.media.thumbnail[0].url,
                        'url': photo.media.content[0].url,
                        'name': photo.title.text,
                    }
                    photos.append(pic)
            except:
                pass
            
        # set memcache
        self.CacheSet(key, photos)
        
        return photos
    
    def CacheClear(self):   
        keys = []
        albums = self.GetAllAlbums()
        for a in albums:
            keys.append("picasa_album_%s_%sc_%s" % (album['title'], self.thumb_size, self.imgmax))
            keys.append("picasa_album_%s_%su_%s" % (album['title'], self.thumb_size, self.imgmax))
        albums.append('picasa_albums')
        memcache.delete_multi(keys)

class FlickrBackend(PhotoBackend):
    flickr = None
    
    def __init__(self, user):
        PhotoBackend.__init__(self, user)
        
        flickr.API_KEY = '36fbcb5322bdab1866dff9622f161400'
        
        self.flickr = flickr.User(self.user_id)
    
    def GetAllAlbums(self):
        logging.info('GetAllAlbums called')
        
        # check memcache
        key = 'flickr_albums'
        albums = self.CacheGet(key)
        if albums:
            return albums
        
        albums = []
        sets = self.flickr.getPhotosets()
        for s in sets:
            albums.append({
                'id': s.id,
                'title': s.title,
            })
        
        # set memcache
        self.CacheSet(key, albums)
        
        return albums
    
    def GetPhotosInAlbum(self, album, featured=[]):
        logging.info('GetPhotosInAlbum called')
        if self.thumb_cropped:
            thumb_size = "Square"
        else:
            thumb_size = "Thumbnail"
        
        if self.imgmax < 600:
            img_size = "Medium"
        else:
            img_size = "Large"
        
        # check memcache
        key = "album_%s_%s_%s" % (album, thumb_size, img_size)
        photos = self.CacheGet(key)
        if photos:
            return photos
        
        photos = []
        sets = self.GetAllAlbums()
        set_id = None
        for s in sets:
            if s['title'] == album:
                set_id = s['id']
                break
        if not set_id:
            return photos
        logging.info('Found photoset %s with id %s' % (album, set_id))
        photoset = flickr.Photoset(set_id, album, False)
        for photo in photoset.getPhotos():
            pic = {
                'id': photo.id,
                'height': 480,
                'width': 640,
                'thumb_url': photo.getURL(size=thumb_size, urlType='source'),
                'url': photo.getURL(size=img_size, urlType='source'),
                'name': photo.title,
            }
            photos.append(pic)
        
        # set memcache
        self.CacheSet(key, photos)
        
        return photos
    
    def CacheClear(self):   
        keys = []
        albums = self.GetAllAlbums()
        #for a in albums:
        #   keys.append("album_%s_%sc_%s" % (album['title'], self.thumb_size, self.imgmax))
        #   keys.append("album_%s_%su_%s" % (album['title'], self.thumb_size, self.imgmax))
        #albums.append('albums')
        #memcache.delete_multi(albums)
