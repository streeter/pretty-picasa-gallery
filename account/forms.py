from django import forms
from account.models import Account
from app import (BACKENDS,
    THUMB_SIZES, THUMB_SIZE_DEFAULT, THUMB_CROPPED_DEFAULT,
    FULL_SIZES, FULL_SIZE_DEFAULT, HOMEPAGE_SIZE_DEFAULT, )

class AccountForm(forms.Form):
    photo_backend = forms.ChoiceField(label="Photo Provider", choices=map(lambda b: (b, b.title()), BACKENDS))
    site_title = forms.CharField(max_length="100")
    site_header = forms.CharField(max_length="100")
    thumb_size = forms.TypedChoiceField(label="Thumbnail size", choices=map(lambda s: (s, s), THUMB_SIZES), coerce=lambda s: int(s))
    thumb_cropped = forms.TypedChoiceField(label="Thumbnails are cropped", choices=((True, 'True'), (False, 'False')), coerce=lambda s: s != u'False')
    full_size = forms.TypedChoiceField(label="Lightbox size", choices=map(lambda s: (s, s), FULL_SIZES), coerce=lambda s: int(s))
    homepage_size = forms.TypedChoiceField(choices=map(lambda s: (s, s), FULL_SIZES), coerce=lambda s: int(s))
    homepage_album = forms.ChoiceField(choices=[], required=False)
    featured_albums = forms.MultipleChoiceField(choices=[], widget=forms.CheckboxSelectMultiple, required=False)
    service_username = forms.CharField(max_length="100", required=False)
    merchant_id = forms.CharField(label="Google Checkout Merchant ID", max_length="25", required=False)
    analytics_id = forms.CharField(label="Google Analytics ID", max_length="25", required=False)
    
    def set_albums(self, albums):
        album_choices = [(a, a) for a in albums]
        self.fields['homepage_album'].choices = album_choices
        self.fields['featured_albums'].choices = album_choices + [('all', 'all')]
