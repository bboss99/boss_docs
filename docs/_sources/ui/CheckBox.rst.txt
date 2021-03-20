.. _checkBox_title:

CheckBox
==========

CheckBox gives functionality of a Boolean or Toggle.

When state is 1 or ON  or True  or Checked  : its Greenish,  

When state is 0 or OFF or False or UnChecked: its Reddish

.. code-block:: python

   from boss.ui_creator import UICreator, RectData, Boss_OT_base_ui, CheckBox

   def onValueChanged(caller: CheckBox):
       print('valueChanged', f'value - {caller.value}')

   def ui_elements(op: Boss_OT_base_ui):
       # op.uip.deleteAllUi()  # to delete all existing ui
       btn_width, btn_height = 150, 40
       rd = RectData(
           op.uip.mouse_x,
           op.uip.mouse_y - btn_height,
           btn_width,
           btn_height
       )
       checkBox = UICreator.checkBox(
           op,
           rectData=rd,
           text='BoolLabel',
           value=True,
           onValueChange=onValueChanged,
           param='This can be any python object'
       )
       # method for adding callback after creation
       # checkBox.add_onValueChange(onValueChanged)

Notes
--------

* In Future update, when images are added, maybe it can be made to look like *tick* sign,
  which will require :ref:`Images <images_title>`   
* In Future update, may be text expression, that evaluates to boolean, can be supported.
  CheckBox now makes use of Button class, maybe another class that uses TextField can be created for that.
