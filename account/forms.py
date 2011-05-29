from django import forms
from account.models import Account
from app import (BACKENDS,
    THUMB_SIZES, THUMB_SIZE_DEFAULT, THUMB_CROPPED_DEFAULT,
    FULL_SIZES, FULL_SIZE_DEFAULT, HOMEPAGE_SIZE_DEFAULT, )

class AccountForm(forms.Form):
    photo_backend = forms.ChoiceField(label="Photo Provider", choices=map(lambda b: (b, b.title()), BACKENDS))
    site_title = forms.CharField(max_length="100")
    site_header = forms.CharField(max_length="100")
    thumb_size = forms.ChoiceField(label="Thumbnail size", choices=map(lambda s: (s, s), THUMB_SIZES))
    thumb_cropped = forms.ChoiceField(label="Thumbnails are cropped", choices=((True, 'True'), (False, 'False')))
    full_size = forms.ChoiceField(label="Lightbox size", choices=map(lambda s: (s, s), FULL_SIZES))
    homepage_size = forms.ChoiceField(choices=map(lambda s: (s, s), FULL_SIZES))
    homepage_album = forms.ChoiceField(choices=[])
    featured_albums = forms.MultipleChoiceField(choices=[])
    service_username = forms.CharField(max_length="100")
    merchant_id = forms.CharField(label="Google Checkout Merchant ID", max_length="25")
    analytics_id = forms.CharField(label="Google Analytics ID", max_length="25")
    
    def set_albums(self, albums):
        album_choices = map(lambda a: (a, a), albums)
        self.fields['homepage_albums'].choices = album_choices
        self.fields['featured_albums'].choices = album_choices
