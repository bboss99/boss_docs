from boss.ui_creator import UICreator, RectData, TextField, Boss_OT_base_ui


def onTextChanged(caller: TextField):
    print('textChanged', f'value - {caller.value}, text - {caller.text}')


def onValueChanged(caller: TextField):
    print('valueChanged', f'value - {caller.value}, text - {caller.text}')


def onEnterPressed(caller: TextField):
    print('enterPressed', f'value - {caller.value}, text - {caller.text}')


def ui_elements(op: Boss_OT_base_ui):
    # UICreator.deleteAllUi(op)  # to delete all existing ui
    btn_width, btn_height = 150, 40
    rd = RectData(
        op.uip.mouse_x,
        op.uip.mouse_y - btn_height,
        btn_width,
        btn_height
    )

    textField = UICreator.textField(
        op,
        rectData=rd,
        onTextChange=onTextChanged,
        onValueChange=onValueChanged,
        onEnterPress=onEnterPressed
    )
    # these are methods for adding callback after creation
    # textField.add_onTextChange(onTextChanged)
    # textField.add_onValueChange(onValueChanged)
    # textField.add_onEnterPress(onEnterPressed)
