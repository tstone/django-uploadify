from django import template
from uploadify import settings

register = template.Library()

# -----------------------------------------------------------------------------
#   multi_file_upload
# -----------------------------------------------------------------------------
@register.inclusion_tag('uploadify/multi_file_upload.html', takes_context=True)
def multi_file_upload(context, upload_complete_url):
    """
    Displays a Flash-based interface for uploading multiple files.
    When all files have been uploaded, the given URL is POSTed to.  The returned
    page replaces (AJAX) the upload interface.

    * filesUploaded - The total number of files uploaded
    * errors - The total number of errors while uploading
    * allBytesLoaded - The total number of bytes uploaded
    * speed - The average speed of all uploaded files
    """
    return { 
        'upload_complete_url' : upload_complete_url,
        'uploadify_path' : settings.UPLOADIFY_PATH,
        'upload_path' : settings.UPLOADIFY_UPLOAD_PATH,
    }
