.. _boss_ot_base_ui_title:

Boss_OT_base_ui
====================

This is a blender operator class.

You can create Operator by inheriting from this class.

Check the Following Code


*   ``CreateCubeOperator``  inherits from ``Boss_OT_base_ui``

*   a method ``ui_elements`` is defined, its actually overridden from base class.

*   ``ui_elements`` method is used to create UIs


.. literalinclude:: ../codes/CreateCubeOperator.py
    :language: python


..  rubric:: Notes:


#.  Every UI created (Panel/Button) contains a reference to operator, it's in the variable **op**

#.  In future updates, there will be more base operators for other needs. I will try to add as many features as possible
    in this base class and avoid creating many base classes with minor differences.
