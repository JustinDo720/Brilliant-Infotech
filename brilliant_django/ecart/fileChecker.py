from django.db.models import FileField
from django import forms
from django.template.defaultfilters import filesizeformat

class ContentTypeRestrictedFileField(FileField):
    def __init__(self, *args, **kwargs):
        # Define content types and max upload size from kwargs
        self.content_types = kwargs.pop("content_types", [])
        self.max_upload_size = kwargs.pop("max_upload_size", 0) 
        
        super(ContentTypeRestrictedFileField, self).__init__(*args, **kwargs)

    def clean(self, *args, **kwargs):
        data = super(ContentTypeRestrictedFileField, self).clean(*args, **kwargs)
        file = data.file

        try:
            content_type = file.content_type
            if content_type in self.content_types:
                if file.size > self.max_upload_size:
                    raise forms.ValidationError(
                        'Please keep filesize under %s. Current filesize %s' % 
                        (filesizeformat(self.max_upload_size), filesizeformat(file.size))
                    )
            else:
                raise forms.ValidationError('Filetype not supported.')
        except AttributeError:
            # Fallback in case file object does not have expected attributes
            pass

        return data
