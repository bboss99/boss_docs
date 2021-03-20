..  _panel_title:

Panel
========

It's a class

This is the most basic UI that can be created. Its so basic that you can't interact with it, meaning, you can't add any kind of event to it.

Panel defines how any UI Element looks. It's color, image, text, shape and size etc.

A Simple rectangle with default settings can be created using following code.

..  code-block:: python

    from boss.ui_creator import UICreator

    def ui_elements(op):
        UICreator.panel(op, (200,200,200,100))

A Panel with more parameter look like this:

..  code-block:: python

    from boss.ui_creator import UICreator
    def ui_elements(op):
        UICreator.panel(
            op=op,
            rectData=(200,200,200,100),
            text='Panel Text',
            ttt = 'ToolTip Text',
            tti = 'ToolTip Image',
            canDrag = True,
            parent = None,
            param='This can any python object'
        )


..  _panel_parameters:

..  rubric:: Parameters

*   op:
        type: :ref:`Boss_OT_base_ui <boss_ot_base_ui_title>`

        It's reference of the operator, inherited from Boss_OT_base_ui

*   rectData:
        type: :ref:`RectData <rectData_title>`

        Rectangle of the panel.

*   text:
        type:str

        It's label

*   ttt:
        possible parameter types:
            *   str: eg. 'this is tooltip'
            *   list of str: eg. ['this is tooltip','this is also tooltip']
            *   func (callable): any function that returns str or list of str.

        tooltip text

*   tti:
        possible parameter types:
            *   str: representing path of an image.
            *   func (callable): any function that returns str as path of an image.

        tooltip image path, it should be full path, not relative path.

*   canDrag:
        type: bool

        True if UI is draggable.

*   parent:
        type: :ref:`Panel <panel_title>` or :ref:`Button <button_title>`

        This panel will be child of passed parameter.

*   param:
        type: any python object

        This is optional parameter that can be passed.

A Panel object is not very useful on its own. Its base class of :ref:`Button <button_title>`, which completes it by
making it intractable. Since Button adds more functionality to Panel, Panel's properties will be discussed along with
Button class, read about that :ref:`Button <button_title>`.


.. rubric:: Footnotes

#.  ``canDrag`` property is defined in Panel, but create :ref:`Button <button_title>` Object to make it draggable.
#.  **Ques.** If Panel is so useless, Shouldn't always :ref:`Button <button_title>` be created?
    Ans. Yes, but Panel is good for Labels(text or Image),Image_tooltip is shown using Panel. If you decided to use some
    non-visible helper ui component, Panel can be used.
