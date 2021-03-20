from boss.ui_creator import UICreator, Boss_OT_base_ui, ButtonData, RectData


def onClicked():
    print('Button is Clicked')

def dragging(some_param):
    print(some_param)


def onWheel(caller, addby):
    caller.param += addby
    print('param is now', caller.param)


def ui_elements(op: Boss_OT_base_ui):
    UICreator.button(
        op=op,
        rectData=RectData(10, 110, 200, 100),
        text='ButtonText',
        buttonData=ButtonData(
            onClick=onClicked,
            onMouseEnter=lambda: print('mouse entered'),
            onMouseExit=lambda: print('mouse exited'),
            onWheelUp=(onWheel, 1),
            onWheelDown=(onWheel, -1),
            onDragBegin=(dragging, 'dragging is started'),
            onDrag=(dragging, "it's being dragged"),
            onDragEnd=(dragging, 'dragging is ended')
        ),
        ttt='tool tip text',
        tti='',
        canDrag=True,
        parent=None,
        rectIsLocal=False,
        param=100
    )
