.. _ui_creator_title:


ui_creator.py
===================

``ui_creator.py`` is the only file/module you have to import to create UIs.

This module has two purposes:

#. Convenience_
#. Compatibility_

Convenience
-------------

This module presents a nice interface for user,
and all the important classes
and modules have already been imported in
this module for convenience. This module also defines/wraps a lot of function
so that you can find all important functions in one place.

.. code-block:: python

   from boss.operators.Boss_OT_base_ui import Boss_OT_base_ui
   from boss.ui.base_ui.PanelData import PanelData
   from boss.ui.Panel import Panel
   from boss.ui.Button import ButtonData, Button
   from boss.Geo.RectData import RectData
   from boss.Geo.RectGeo import RectGeo, RectGeoData
   from boss.Alignment import Align
   from boss.Text import TextData, Text
   from boss.Color import Color
   from boss.ui.CheckBox import CheckBox
   from boss.ui.TextField import TextField
   from boss.ui.IntField import IntField
   from boss.ui.FloatField import FloatField
   from boss.ui.VectorField import VectorIntField, VectorFloatField, VectorBooleanField
   from boss.ui.ColorField import ColorField

you can import only the things you need


.. code-block:: python

   from boss.ui_creator import Button,ButtonData,Panel,PanelData,RectData


or you can import everything

.. code-block:: python

   from boss.ui_creator import *


Even though ``import *`` is discouraged but if you want to create a few different types of UI, you can use it.

or you can import ``UICreator``

.. code-block:: python

   from boss.ui_creator import UICreator

.. note::

   UICreator is most import class to import


Compatibility
----------------

TL;DR; :ref:`Conclusion <conclusion_compability>`

Since *boss* package is in early development and will be in continuous development, new features will be added and
existing things may be improved. File, functions, classes will be deleted, moved and renamed, and the code you have
written may break in future.

For eg to create a Button there are around 40 parameters(at the moment) that can be set as you can see in following code:

.. literalinclude:: ..\codes\snip_button_all_params.py
    :language: python

In future, some of these parameters will be moved and removed and new parameters will be added.

In order to deal with it, I have written `UICreator <#uicreator-class>`_ class, which contains static methods that creates UI.

for eg, this is static method ``floatField`` that just creates and returns instance of :ref:`FloatField <floatField_title>`.


.. literalinclude:: ..\codes\snip_floatField.py
    :language: python

..  _conclusion_compability:

Conclusion
-------------


*   Use `UICreator <#uicreator-class>`_'s functions whenever possible. This is enough for all the basic tasks.

*   If you don't see things in UICreator, maybe its not final yet, eg. geometry classes, colors,images etc.

*   Things that aren't ready can still be used, but your code may require minor adjustment with future updates.

*   If you are writing addon use everything and when writing boss scripts, use only `UICreator <#uicreator-class>`_

*   eg. Instead of using ``Button(op,RectData(0,0,10,10))`` to create a Button use ``UICreator.button(op,(0,0,10,10))``

*   In documentation, I will be using ``UICreator`` class.


     
UICreator (class)
-------------------

UICreator is a class that contains all the functions in one place to create UI. 

.. code-block:: python

   import bpy
   from boss.ui_creator import UICreator


   def ui_elements(op):    
       # Create Cube
       b = UICreator.button(op,(0,0,100,50),'Cube',lambda :bpy.ops.mesh.primitive_cube_add(size=2))

More functions will be added in this class as project grows.

Currently, Other Functions are:


.. code-block:: python

   UICreator.button(..)
   UICreator.checkBox(..)
   UICreator.textField(..)
   UICreator.floatField(..)
   UICreator.intField(..)
   UICreator.vectorIntField(..)
   UICreator.vectorFloatField(..)
   UICreator.vectorBooleanField(..)

   UICreator.rr(op)
   UICreator.deleteAllUi(op)
   UICreator.mouse_xy(op)


..  note::

    Check out :ref:`Tutorial section in Quick Run Docs<qr:tut_basics>` to see practical examples.


..  note::

    #.  ColorField and DropDown are working and will be added soon in UICreator.
    #.  Layout is there but will be removed.


..  admonition:: technical detail

    In future more time saving functions will be written in this module and a lot of things
    (for eg. layout functionality, mesh-combining, some panel/button creation parameters) may be moved from boss
    package to this module.

    Even though performance is not an issue now, some classes may benefit from ctypes or cython. (for eg. RectData
    and Geo). Acceleration mechanism for cursor insided-ness, kd-tree, bvh-tree from mathutils package
    can be used when number of ui increases. All that can be written as a part of ui_creator.


..  rubric:: Notes


#.  `ui_creator.py`, since it's not essential to *boss* , should be and can be placed outside of boss package.
    It can be part of the addon or you can **write your own** functions to simplify the process or avoid repetitions and typing.
    It can be part of utils in some extra folder in modules, (like there is blender's bpy_extra and gpu_extra python modules).
    At the moment. It's one file, but soon it will become multifile package.

