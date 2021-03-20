.. _textField_title:

TextField
============

It's a class and is used to create TextFields. 

This is base class for :ref:`IntField <intField_title>` and :ref:`FloatField <floatField_title>`

code:

..  literalinclude:: ../codes/textField_01.py
    :language: python


*   TextField has two properties, ``text`` and ``value``. ``text`` is always of ``str`` type and is equal to displayed text.
    In case of TextField ``value`` is also of type ``str``.

*   ``value`` is committed ``text``. You commit by pressing Enter.

*   When user clicks on the TextField, input mode changes and is listening for keyboard Input instead of mouse input.
    *You can come out of Keyboard input mode by pressing either Enter or Escape.*

*   When you press **Enter** , you commit ``text`` to ``value``, meaning, displayed text becomes new value.

*   When you press **Escape** , you cancel ``text`` and old ``value`` remains.


..  warning::

    When typing in textfield, you should remember to exit out of it by pressing ESC or ENTER. (Mouse right click don't
    work)


..  rubric:: Events:

#.  onTextChange:
        this is called whenever user types something to change text.
        eg. search suggestion feature, filtering the result as user types.

#.  onEnterPress:
        when user presses Enter key, this event is called.
        eg. load something when user had done typing.

#.  onValueChange:
        this is called when user presses Enter and new text value is different from old text.


..  rubric:: Notes:

*   Its based on Blender's operator events, so all the keys are checked for press. HOME, END, CTRL+V (Paste) and normal
    navigation like arrow keys work to some extent but there are some known bugs.

*   *Just for curious people* , Cursor blinking is implemented using `wm.event_timer_add` as described in python
    templates examples. So a Panels visibility is toggled in a interval. (There are no Threads or Timer yet)



..  rubric:: Footnotes:


#. In future updates, this will be modified a lot, the way it works now, gets the Job done.
