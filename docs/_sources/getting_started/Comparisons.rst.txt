..  _comparisons:

Comparisons
=============

In this section, Boss's features will be compared so that you can understand various possibilities.

Lets take a hypothetical task of `creating a named cube`, that is, take input string from user and create a Cube with that name. simple.

Below are two code sections that perform the above mentioned task.

Following is a way using operator:

   .. code-block:: python
   
       import bpy
   
       class OBJECT_OT_create_named_cube(bpy.types.Operator):
           bl_idname = 'object.create_named_cube'
           bl_label = 'Create Named Cube'
           cubeName : bpy.props.StringProperty(name='cubeName',default='Cube')
   
           def invoke(self, context, event):        
               return context.window_manager.invoke_props_dialog(self, width=250)
   
           def execute(self, context):
               bpy.ops.mesh.primitive_cube_add(size=2)
               context.object.name = self.cubeName
               return {'FINISHED'}
   
           def draw(self, context):
               layout = self.layout
               layout.prop(self,'cubeName')
   
       def register():
           bpy.utils.register_class(OBJECT_OT_create_named_cube)
   
   
       def unregister():
           bpy.utils.unregister_class(OBJECT_OT_create_named_cube)
   
   
       if __name__ == "__main__":
           register()


And Following is way using boss script:

.. code-block:: python

    import bpy
    from boss.ui_creator import UICreator

    def onEnterPress(caller):
        bpy.ops.mesh.primitive_cube_add(size=2)
        bpy.context.object.name = caller.value
        caller.op.quit()  # to quit after the button is clicked.


    def ui_elements(op):
        rr = UICreator.rr(op)
        
        rd = (rr.width/2 - btn_width/2,rr.height/2 - btn_height/2,100,40)
        
        UICreator.textField(op,rd,text='Cube',onEnterPress=onEnterPress)
        


Addon vs Script
-----------------

.. list-table:: **Addon vs Script**
   :widths: 50 50
   :header-rows: 1

   * - Addon
     - Script     
   * - Always needs registration.
     - Can be an addon or can be a Script
   * - -
     - | is dynamic, scripts won't require reload, 
       | ui can be created/deleted while script 
       | is running
   * - -
     - New UIs can be created at any time.
   * - | isn't very flexible, user has limited way to
       | creating things, UI has limited option.
     - | is very flexible, you can create gui very 
       | precisely and add event in an easy way.

Operator vs Button
-------------------

| There will be time when when you simply want to create operator to call a function or 
| run a sequence of code. This is comparison of two the ways


.. list-table:: **Operator vs Button**
   :widths: 50 50
   :header-rows: 1

   * - Operator
     - Button
   * - No image.
     - Image
   * - No Image tool tip.
     - Image tooltip
   * - Looks and size isn't customizable.
     - Looks and size can be customized.
   * - na
     - Can be repositioned by dragging
   * - | Can be (needs to be) placed on other
       | Menu or Panel to exist in UI.
     - na 
   * - This is normal way of doing thing.
     - | It's basically a modal operator,
       | nothing much.
   * - | You can only define what happens when
       | clicked, or when a property is updated
     - | You can add onClick,onMouseEnter/Exit,
       | onMouseRollUp/Down, onDrag/Begin/End 

