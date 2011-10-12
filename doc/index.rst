.. django-uploadify documentation master file, created by
   sphinx-quickstart on Wed Oct 12 06:28:49 2011.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.
  
django-uploadify
================

A Django_ re-usable app to integrate Uploadify_


===========================
Installing django-uploadify
===========================

        1. Add ``uploadify`` to your ``INSTALLED_APPS`` in the project's settings.py file.
        2. Add a reference to uploadify in your urls.py file

.. code-block:: python

        (r'^uploadify/', include('uploadify.urls')),
        
====================
Installing Uploadify
====================

        1. Download Uploadify.
        2. Copy the contents of the Uploadify distribution into your static files diretory (``STATIC_ROOT``/js/uploadify/)
        3. Rename the ``jquery.uploadify.vx.x.x.min.js`` file to ``jquery.uploadify.js``
           
======================
Using django-uploadify
======================

------------
How It Works
------------

django-uploadify works by providing a template tag that takes a single parameter.  The template tag will render the Uploadify jQuery/Flash multi-file interface on the page.  For each file a user uploads, a Django signal is fired, containing the file data. After all the uploads have been completed, JavaScript within the template tag will fetch the page at the the value passed in (``upload_complete_url``) and replace the Uploadify GUI elements with the contents returned (a jQuery $.load).

-------------
Code Examples
-------------

Inserting the tag::

        {% load uploadify_tags %}
        {% multi_file_upload 'your/url/upload/complete/' %}

Using the tag with a reverse URL::

        {% url my_upload_complete_url as upload_complete %}
        {% multi_file_upload upload_complete %}
        
Creating a signal receiver:

.. code-block:: python

        def upload_received_handler(sender, data, **kwargs):
                // save the file here, or pass it to a model with a FileField.
        upload_received.connect(upload_received_handler, dispatch_uid='yourapp.upload_received')
        

------------------
Making it all work
------------------

More than likely the ideal use is to tie the upload_received signal to automatically create a new object with Django’s ORM. If you’re planning on having an edit interface of any sort for the users after upload is complete (ideally what would be in ‘upload_complete_url’), an additional object property to keep track of this would work well.

Say we want to make a photo sharing app where users can upload several photos. In our media manager app, we could have a model like so…

.. code-block:: python

    class Media(models.Model):
        file = models.FileField(upload_to=‘upload’)
        new_upload = models.BooleanField()
        
Whenever a signal is received, we can have the signal handler create a new instance of the object…

.. code-block:: python

        def upload_received_handler(sender, data, **kwargs):
            new_media = Media.objects.create(
                file = data,
                new_upload = True,
            )
            new_media.save()

        upload_recieved.connect(upload_received_handler, dispatch_uid=‘happenings.models.upload_received’)

        
Finally, the value of ‘upload_complete_url’ sends the users to a view which finds all of the files with new_upload = True. (I’ll leave it up to you to figure out how you want to associate media objects with users).


=========
Reference
=========

------------------------------------
JavaScript Event: allUploadsComplete
------------------------------------

On the client side, a javascript event is provided to capture when all uploads have been completed. It can be bound with the following jQuery code

.. code-block:: javascript

        $(‘#uploadify’).bind(‘allUploadsComplete’, function(e, data){

             // This code executes on AllUploadsComplete event…

        }
        
-------------------
upload_complete_url
-------------------

When this page is fetched by the client-side javascript, the following Uploadify values are POST’ed to it:

        * filesUploaded – The total number of files uploaded
        * errors – The total number of errors while uploading
        * allBytesLoaded – The total number of bytes uploaded
        * speed – The average speed of all uploaded files

Contents:

.. toctree::
   :maxdepth: 2



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

.. _Django: https://www.djangoproject.com
.. _Uploadify: http://www.uploadify.com/
