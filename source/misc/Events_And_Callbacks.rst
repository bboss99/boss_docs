..  _events_and_callbacks_title:

Events and Callbacks
=========================

In this page you will find general idea and syntex for adding callbacks. This is applicable for all UI types.

Simply speaking, **events** are things like mouse click (onClick), mouse entering or exiting UI, 
some keyboard key getting pressed etc. 


**Callback** or callback function, is the function, you can pass to the UI (Button, TextFields etc) as parameter,
for any particular event. When that event occurs that function will be called.


Callbacks for all UI types are described in their respective pages. This page only explains the way 
parameters(functions) need to be passed.

..  rubric:: In boss you can add callbacks using two ways:


#. When creating UI, there will be a way to add callback as a parameter. For :ref:`Button<button_title>`,
   there is a :ref:`ButtonData<buttonData_title>` class, which is a separate class because Button has so many events.

#. Every UI class, for every event, also defines, corresponding method to add callback,
   that can be used after the UI object is created.

Example will make it more clear, I will take example of Button's onClick event, but it's applicable for 
all event types (eg onTextChange of TextField):

Below is the code which is followed by explanation:

..  literalinclude:: ../codes/event_callback.py
    :language: python
    :linenos:
    :emphasize-lines: 4,5,8,9,12,13,16,17,25,30-33

*   Code related to callback is highlighted.

*   At line 4,8,12 and 16, you can see 4 callback functions, ``onClicked``, ``onClicked1``, ``onClicked2``, ``onClicked3``
    respectively and each has different signature(parameter list).

*   ``onClicked``, which has no parameter, is passed to ButtonData's ``onClick`` parameter (line 25) while Button creation
    using ``buttonData=ButtonData(onClick=onClicked),``

*   You can add multiple callbacks to a button, but while creating ButtonData/UI object you can pass only one callback. [#f1]_

*   Button instance has ``add_onClick`` method, similarly you'll find ``add_eventName`` for all event for all UIs. [#f2]_

*   ``onClicked1`` definition has three parameters, ``p_one,p_two,p_three``. To add callback after the button is created use
    ``button.add_onClick(onClicked1, 1,'two', 3.0)`` with first argument being the function and following arguments being
    function arguments. So, in order to call a function with 3 parameters, You passed 4 arguments to ``add_onClick``.
    In case you had wanted to add this callback during Button creation, you could have used
    ``buttonData=ButtonData(onClick=(onClicked1, 1,'two', 3.0))``, i.e. those 4 parameters in a tuple. [#f3]_

*   Next function is ``onClicked2``, it has a parameter named ``caller`` , which is a special argument, read about it
    :ref:`here <caller_title>`

*   Next function is ``onClicked3`` , which combines the features of ``onClicked1`` and ``onClicked2`` , so, yes, ``caller`` and
    other parameters can also be used together.

*   Last is ``button.add_onClick(lambda caller: print('lambda-',caller,caller.param))`` , lambda works, caller with lambda works too.


..  _caller_title:

caller
---------

When first argument in the callback function is named `caller` (it doesn't have to be first though) ,
it is a special argument. It's value is the instance of UI
element that called this function. So, if the function is callback of Button's `onclick`, caller's value will be the Button
instance, if function is callback of TextField's `onTextChanged`, caller's value will be the instance of TextField. 

..  NOTE::
        its ``caller``, all small, not Caller or CALLER


*   You don't need to pass any value for caller parameter, while adding callback, eg. ``ButtonData(onClick = onClicked2)``
    or ``button.add_onClick(onClick=onClicked2)``

*   Since all UI have param parameter, ``caller`` in conjunction with param, makes it very flexible. With caller as
    first parameter in the callback, You can create logic so that same function can be callback of many events.

*   Using caller is enough in most cases and syntax is very clean.

*   If creating several buttons that call same function with different parameter, `caller` syntax is encouraged.

*   Using caller is always encouraged. [#f5]_


..  rubric:: Footnotes:



..  [#f1] Maybe later I will add code, so that a list of callbacks can be added while creating UI object. It's rare but can be handy.

..  [#f2] One function could be enough, with type of event also being passed, but since, Most people use VSCode or
   other ide that supports code suggestion, code completion, writing method of each event is more readable.

..  [#f3] I know  ``functools.partial`` is one way, one could use and pass one variable, this is just for convenience so
    that you won't have to
    import ``partial`` in every file.

..  [#f4] It wasn't intentional but instead of ``button.add_onClick(onClicked1, 1,'two', 3.0)``,
    ``button.add_onClick((onClicked1, 1,'two', 3.0))`` also works. i.e. you can pass one argument only,
    the tuple that contains those 4 elements.

..  [#f5] It will be optimized in future updates.

