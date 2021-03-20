.. _images_title:

Images
========

..  rubric:: Important points:

#.  After operator is invoked, any image that is imported will be deleted when the operator quits.

#.  Reloading images on every invoke doesn't feel right, even though there is no performance hit. When loading 50+
    images slight lag can be felt. It's doable for personal use some times.

#.  **In future updates** , user will have a choice to retain (not delete) an image that needs to be reused.
    eg. image used as a part of UI.

#.  While loading image ``use_existing`` flag is ``False``, so if you load an image, that already exists in some
    data block (eg. as a image texture) that will be re-imported again, because of *point 1*.

#.  Only **.png** is supported for now.

#.  **In future updates**\ , Handling images will require a lot of work when UV will be incorporated.

