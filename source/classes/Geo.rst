.. _geo_title:

Geo
======

* **User need not be concerned with Geo class.**

* This class is base class of RectGeo, EllipseGeo and other kinds of Geo classes.

* This class is responsible for drawing of UI.

* Every Panel/Button has a Geo instance.

* Its functions and properties will change for optimization and to include more geometry types.

..  _optimized_settings:


optimized
-----------

..  note::

    tldr: there is setting file  ``boss/settings/op_settings.json``. In that file, ``draw_mode`` is set to
    blank ``''``. You can set it to ``optimized`` to optimize drawing. Sorting (among other things) is not handled
    in this mode for optimization.


This explanation is a bit technical so you can safely skip it if you have read the above note. OTOH, if you are expert
or know some bgl/opengl stuff, you can suggest some solution/answer for future.

Since, this class is responsible for drawing, this class uses shaders, batches and images and makes use of gpu and
bgl modules to draw geometries.

This project doesn't require expert level knowledge of opengl and examples code given in blender documentation is enough
for drawing rect or drawing an image. This project needs only that at the moment.

I am no expert in opengl and am reading it to gain enough knowledge to decide how to properly batch geometries and order
them to efficiently draw all the gui stuff as well as texts.

I have to take into account many things to decide a proper way doing it. Changing colors, disabling/enabing geometries,
deleting geometries, sorting and all the future use case that I have in mind.



``draw_mode == 'optimized'`` is a temporary quick fix to draw geometries. This does following things:

    1.  Instead of calling draw method of geo class of each panel/button, draws them in a loop, trying to keep shader binding
        to minimum and opengl state changes to minimum before drawing each geometry. If shader is same it simply sets the
        uniform and draws the geometry.(which I think blender does anyway at C level, so it might be unnecessary)

    2.  Makes use of global settings for drawing all texts and ignores custom settings of each panel/button. So, you can't
        draw one textfield that is red and sized 20 and another that is white and sized 15. (It don't know how costly
        changing fonts and colors are)

    3.  First, draws all the rectangles(polygons) in a loop, and, then draws all the texts in a loop. (This causes sorting issue)
        (Usually, in other ui systems, things are not drawn on top of each other, so this way drawing geo in loop
        and then drawing texts in a loop won't cause any issue. There is no such constraint in BOSS and if you won't
        draw overlapping geometries this would work just fine.)

A lot of the above mentioned lack of features is not much of importance for now because geometry/text features
are not added to ``ui_creater.py`` or ``UICreator`` class. Moreover, these features are about aesthetics and not
functionality.


.. note::

    At the moment, to draw partial geometry(clipping) there is shader that takes four floats and clips the geometry in
    fragment shader. I don't think, it's good. To make things worse, it does the same thing for texts too.

    To solve that, geometries can be batched in on geometry (which is already working partially) and text can simply be
    shortened/removed.

    In future, may be a stencil can be used for both rectangle and texts.




