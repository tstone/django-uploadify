from django.conf import settings

# Uploadify root folder path, relative to MEDIA_ROOT
UPLOADIFY_PATH = settings.UPLOADIFY_PATH = getattr(settings, 'UPLOADIFY_PATH', '%s%s' % (MEDIA_URL, 'js/uploadify/'))

# Upload path that files are sent to
UPLOADIFY_UPLOAD_PATH = settings.UPLOADIFY_PATH = getattr(settings, 'UPLOADIFY_UPLOAD_PATH', '%s%s' % (STATIC_ROOT, 'uploads/'))
