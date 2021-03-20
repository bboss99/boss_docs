@staticmethod
def floatField(op: Boss_OT_base_ui,
               rectData: rectDataType,
               value: fieldType = None,
               onValueChange: callbackType = None,
               onTextChange: callbackType = None,
               onEnterPress: callbackType = None,
               ttt: str = '',
               tti: str = '',
               canDrag: bool = True,
               parent: uiType = None,
               rectIsLocal: bool = False,
               param=None
               ) -> FloatField:

    if isinstance(value, FieldValue):
        val = value.value
        minValue = value.min
        maxValue = value.max
        changeBy = value.changeBy if value.changeBy else .1
    else:
        val = value
        minValue = None
        maxValue = None
        changeBy = .1

    return FloatField(op, rectData if isinstance(rectData, RectData) else RectData(*rectData),
                      panelData=PanelData(toolTipText=ttt, toolTipImagePath=tti, canDrag=canDrag,
                                          parent=parent, rectIsLocal=rectIsLocal),
                      value=val,
                      minValue=minValue,
                      maxValue=maxValue,
                      changeBy=changeBy,
                      onTextChange=onTextChange,
                      onValueChange=onValueChange,
                      onEnterPress=onEnterPress,
                      param=param
                      )
