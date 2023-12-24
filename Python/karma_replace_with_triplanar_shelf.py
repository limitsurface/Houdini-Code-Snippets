target_nodes = hou.selectedNodes()
parent_node = target_nodes[0].parent()

position_node = parent_node.createNode("mtlxposition", "rest_position")
xform_node = parent_node.createNode("usdtransform2d", "xform")
xform_node.setInput(0, position_node)

x_pos = 0
y_pos = 0

for target_node in target_nodes:
    x_pos += target_node.position()[0]
    y_pos += target_node.position()[1]

    file_path = target_node.evalParm("file")
    signature = target_node.evalParm("signature")
    triplanar_node = parent_node.createNode("mtlxtriplanarprojection", target_node.name())
    triplanar_node.setParms({"signature":signature})
    triplanar_node.setParms({"filex":file_path})
    triplanar_node.setParms({"filey":triplanar_node.parm("filex")})
    triplanar_node.setParms({"filez":triplanar_node.parm("filex")})

    output_node = target_node.outputConnectors()[0][0].outputNode()
    output_index = target_node.outputConnectors()[0][0].inputIndex()
    output_node.setInput(output_index, triplanar_node)
    
    triplanar_node.setPosition(target_node.position())
    triplanar_node.setNamedInput("position",xform_node,0)
    target_node.destroy() # delete tex node

x_pos /= len(target_nodes)
y_pos /= len(target_nodes)
x_pos -= 5
new_pos = hou.Vector2(x_pos,y_pos)

xform_node.setPosition(new_pos)
position_node.setPosition(new_pos - hou.Vector2(3,0))
