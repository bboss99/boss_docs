.. _rectData_title:

RectData
==========

It's a class. 

It basically defines Rectangle's dimension.

..
    EDITME Take a screenshot.


Every Panel/Button has a RectData instance. It's the RectData object, that is checked if it's under the cursor,
for all the events.


..  admonition:: technical detail

    Its functions and properties will change for optimization. This class will benefit from ctypes/cython.

..  code-block:: python

    def __init__ (self, xMin=0, yMin=0, width=0, height=0):
        ...
        ...


xMin, yMin are distance from left and bottom side of area/region respectively. ``(xMin,yMin)`` is bottom-left point.


..  rubric:: Methods:


..  note::

    This class has many methods and static methods that do basic things, like scaling, union,
    intersection etc, they will be documented later

I am writing about 4 methods, ``getBottom`` , ``getTop`` , ``getLeft`` , ``getRight`` . They are used to create and
return new ``RectData`` instance in the direction suggested by their name.

..  code-block:: python

    def getBottom(space=0):
        ...
        ...

    def getTop(space=0):
        ...
        ...

    def getRight(space=0):
        ...
        ...

    def getLeft(space=0):
        ...
        ...

all 4 work similar and even though it has many parameters, ``space`` is only parameter kind of final yet.
You can find it's example in :ref:`Boss UI tutorial <qr:tut_boss_ui>`



..  rubric:: Notes:

*   because every UI is drawn in screen space, ``xMin,yMin,width,height`` should mostly be integers, though you can pass
    float as well.

*   To get mouse position you can use ``mouse_x, mouse_y = UICreator.mouse_xy(op)``

