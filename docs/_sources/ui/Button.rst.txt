..  _button_title:


Button
===========

It's a class. 

Button is the most important *complete* UI that can be created. *Complete* , 
means all other UI types are created using Button only, either by inheritance or by creating it's instance. 

Therefore, TextField, IntField, CheckBox etc are all child of Button or have Button instance. 
Their Vector counterpart eg. VectorIntField has three Button instances.


..  note::

    This page and :ref:`Event and Callback<events_and_callbacks_title>` are very important, read carefully with patience


Simplest button requires two non-optional parameter:


*   op:
        type: :ref:`Boss_OT_base_ui <boss_ot_base_ui_title>`

        It's reference of the operator, inherited from Boss_OT_base_ui



*   rectData:
        type: :ref:`RectData <rectData_title>`

        Rectangle of the panel.


..  literalinclude:: ../codes/button_01.py
    :language: python
    :linenos:


..  rubric:: Default behaviour:


*   By default button is draggable.
*   By default button can't be dragged outside the view region.
*   By default button adds callback to change color ``onEnter`` and ``onExit``.

Above code does nothing when clicked, a more usable Button can be created using following code:

..  code-block:: python

    from boss.ui_creator import UICreator, Boss_OT_base_ui

    def createCube():
        import bpy
        bpy.ops.mesh.primitive_cube_add(size=2)

    def ui_elements(op:Boss_OT_base_ui):
        UICreator.button(op, (10, 10, 200, 100), 'Cube', createCube)

Above code Creates a Button near bottom left, when clicked, a Cube is created.

..  code-block:: python

    from boss.ui_creator import UICreator

    def ui_elements(op):
        UICreator.button(op, (10, 60, 100, 50), 'Cube',
                         lambda : exec('\n'.join(('import bpy',"bpy.ops.mesh.primitive_cube_add(size=2)"))))

Above code does the same but uses lambda function. This way you can create several buttons without explicitly
defining function.


..  rubric:: Here is how a button will look with all the supported parameters


..  literalinclude:: ../codes/button_all_params.py
    :language: python
    :linenos:


*   You can think of Button as, **Button = It's Shape and Size + Interectivity**, where Shape and Size is 
    defined by the parameters that are part of creating a :ref:`Panel <panel_title>` and Interactivity is
    provided using ``ButtonData`` object.

*   So, Button inherits from Panel, and :ref:`ButtonData<buttonData_title>` is only extra parameter that is required.
    You can compare :ref:`Panel Parameters <panel_parameters>` with above code and see the 
    :ref:`ButtonData<buttonData_title>` is the extra parameter.


..  _buttonData_title:

ButtonData
----------------

It's a class.

This class object is used to pass :ref:`callback function <events_and_callbacks_title>` for button events.

This is part of the above code, that first creates ButtonData object, then uses this *buttonData* to create Button.


..  literalinclude:: ../codes/button_all_events.py
    :language: python
    :linenos:


From the above code you can see, Several buttons can be created using same *buttonData*.


..  rubric:: Notes:


*   You can create buttons in a loop with the same buttonData, in different locations (using different RectData list).

*   Button doesn't store reference to buttonData.

*   Obviously, You don't need all the callbacks in one Button, this example is just for demonstration, add callback only
    for what you need.


.. note::
    You must have read :ref:`event and callbacks <events_and_callbacks_title>` by now.


.. rubric:: Button Events


*   onClick         : called when button is clicked
*   onHover         : onHover isn't implemented.
*   onMouseEnter    : when mouse entered the rect of button
*   onMouseExit     : when mouse exited the rect of button
*   onWheelUp       : mouse wheel (middle button) rolled up
*   onWheelDown     : mouse wheel (middle button) rolled down.
*   onDragBegin     : when mouse (LMB) is pressed.
*   onDrag          : when mouse (LMB) move moves, being pressed.
*   onDragEnd       : when mouse (LMB) if lifted

Following code shows all the ``add_eventName`` method of Button object.


..  literalinclude:: ../codes/button_add_eventName.py
    :language: python
    :linenos:


..  rubric:: Notes:


#.  Every button added needs to be checked whether mouse cursor is within its rect. It happens whenever mouse moves.
    More buttons you add, more time it would take. Generally, 10 to 20 buttons, are required for creating any
    simple functionality.But, create 100,200 buttons is still doable. In future updates, as project will grow,
    there will be some way to accelerate this using trees, hashing, area partitioning etc.

#.  Since Panel isn't interactive, it has very few uses. During development, a ``Panel`` was enough to be draggable
    and change it's color. To keep all the interactivity and callbacks in one class, all code for callback was
    removed from ``Panel`` to ``Button``. Now a Button is required to change ``Panel`` properties of ``canDrag`` and color.

#.  **What is Click?** , If mouse is down and up in the same co-ordinate position, the up event becomes the click.
    If mouse moved, even by 1 px, when held down, its **NOT** a click. (its a Drag). Some times click doesn't work,
    this could be the reason.

