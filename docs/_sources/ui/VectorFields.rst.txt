.. _vectorFields_title:


.. |FloatField| replace:: :ref:`FloatField <floatField_title>`
.. |IntField| replace:: :ref:`IntField <intField_title>`
.. |CheckBox| replace:: :ref:`CheckBox <checkBox_title>`

VectorFields
=====================

|FloatField|, |IntField|, and |CheckBox|  have their Vector form as well. They are named ``VectorFloatField`` ,
``VectorIntField`` , ``VectorBooleanField`` respectively.

These classes simply create 3 instances of their regular fields.

Following is the code to create all three of VectorFields:

..  literalinclude:: ../codes/vectorFields_01.py
    :language: python
    :linenos:



#.  These are presented together, since they all inherit from same class ``_VectorField`` internally.

#.  You can see they have similar events to their *one value* counterpart, i.e. ``onValueChanged`` , ``onTextChange`` and ``onEnterPress``.

#.  Since Checkbox is just a Button, it only has ``onValueChange``. Because of that, ``onTextChange`` and ``onEnterPress`` will raise exception,
    but these methods are still available(since it inherit from same class ``_VectorField``).
