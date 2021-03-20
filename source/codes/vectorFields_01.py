from boss.ui_creator import UICreator,Boss_OT_base_ui,RectData


def onTextChanged(caller):
    print(type(caller).__name__, f'value - {caller.value}, text - {caller.text}')


def onValueChanged(caller):
    print(type(caller).__name__, f'value - {caller.value}, text - {caller.text}')


def onEnterPressed(caller):
    print(type(caller).__name__, f'value - {caller.value}, text - {caller.text}')


def ui_elements(op: Boss_OT_base_ui):
    # UICreator.deleteAllUi(op)  # to delete all existing ui
    btn_width, btn_height = 150, 40
    space = 10

    rd = RectData(
        op.uip.mouse_x,
        op.uip.mouse_y - btn_height,
        btn_width,
        btn_height
    )

    vbf = UICreator.vectorBooleanField(
        op,
        rectData=rd,
        value=(True, False, True),
        onValueChange=onValueChanged,
        param='This can be any python object'
    )
    # can also be used
    # vbf.add_onValueChange(onValueChanged)

    rd = rd.getBottom(space)

    vff = UICreator.vectorFloatField(
        op,
        rectData=rd,
        value=(0.0, 0.0, 0.0),
        onValueChange=onValueChanged,
        onTextChange=onTextChanged,
        onEnterPress=onEnterPressed,
        param='This can be any python object'
    )
    # can also be used
    # vff.add_onTextChange(onTextChanged)
    # vff.add_onValueChange(onValueChanged)
    # vff.add_onEnterPress(onEnterPressed)

    rd = rd.getBottom(space)

    vif = UICreator.vectorIntField(
        op,
        rectData=rd,
        value=(0, 0, 0),
        # can also be used
        # onValueChange=onValueChanged,
        # onTextChange=onTextChanged,
        # onEnterPress=onEnterPressed,
        param='This can be any python object'
    )
    vif.add_onTextChange(onTextChanged)
    vif.add_onValueChange(onValueChanged)
    vif.add_onEnterPress(onEnterPressed)
