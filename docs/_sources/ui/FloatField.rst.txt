.. _floatField_title:

FloatField
===========

This is a class.

It is used to create FloatField. 


*   It inherits from :ref: `TextField <textField_title>` and overrides a few methods so that it's
    `value` is of type `float`
*   Everything valid for ``TextField`` is valid for ``FloatField``, it has same events.


Following code is very similar to the code of TextField.

code:

.. code-block:: Python

   from boss.ui_creator import UICreator, RectData

   def onTextChanged(caller):
       print('textChanged', f'value - {caller.value}, text - {caller.text}')

   def onValueChanged(caller):
       print('valueChanged', f'value - {caller.value}, text - {caller.text}')

   def onEnterPressed(caller):
       print('enterPressed', f'value - {caller.value}, text - {caller.text}')

   def ui_elements(op):
       btn_width, btn_height = 150, 40
       rd = RectData(
           op.uip.mouse_x,
           op.uip.mouse_y - btn_height,
           btn_width,
           btn_height
       )

       floatField = UICreator.floatField(
           op,
           rectData=rd,
           value=100,
           onTextChange=onTextChanged,
           onValueChange=onValueChanged,
           onEnterPress=onEnterPressed,
           param='This can be any python object'
       )
       # these are methods for adding callback after creation
       # floatField.add_onTextChange(onTextChanged)
       # floatField.add_onValueChange(onValueChanged)
       # floatField.add_onEnterPress(onEnterPressed)


*   By default ``onWheelUp`` and ``onWheelDown`` callbacks are added. So rolling mouse will change the value by .1
*   You can type simple math expression.
    eg, ``1+2``, value = 3.0 , ``9/2``, value = 4.5
*   by default, value has precision of 3. So, for 3.12345 becomes 3.123
