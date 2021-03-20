
Introduction
================

BOSS  (Blender Operator Scripting Solution)
----------------------------------------------------

.. image:: ../imgs/boss_home.png
   :alt: 'boss feature image'


This is alternate way of creating blender addons and scripts. This is open-source, object oriented, easy and dynamic way of creating UI and HUDs.

You can create addon just fine, inheriting from :ref:`BOSS_OT_base_ui<boss_ot_base_ui_title>` for dedicated tasks and install it like a
regular Blender addon. Moreover, you can also use this package with one of the :ref:`Launchers (Quick Run)<launchers_title>`
Addons. There are two addons at the moment. I will write more like other types of Menus in future.


..  note::

    You should read this documentation along with  :ref:`Quick Run<qr:qr_index>`


..  rubric:: Main Points:

*   You won't have to touch a single line of code to define shader, text, opengl stuff like bgl, blf. Everything happens
    behind the scene.


*   You won't have to handle or track mouse coordinates, it also happens behind the scene.


*   all you need to do is add age-old callbacks like ``onClick, onMouseEnter, onDrag`` etc, in the simplest way possible.


*	It's not just UI, it's a **general-purpose-base-class-modal-operator**, so, you can create interactive interfaces that is integrated in 3D view or any other panel.


..  note::

    Like BOSS project(coding part) this documentation project also is WIP, I will be updating it and adding more content
    to it in near future.

