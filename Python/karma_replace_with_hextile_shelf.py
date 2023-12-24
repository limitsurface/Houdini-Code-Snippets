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
    hex_node = parent_node.createNode("kma_hextiled_triplanar", target_node.name())
    # hex_node.setParms({"signature":signature})
    hex_node.setParms({"file":file_path})
    
    if signature == "color3":
        hex_node.setParms({"sourceColorSpace":"sRGB"})
    else:
        hex_node.setParms({"sourceColorSpace":"raw"})

    output_node = target_node.outputConnectors()[0][0].outputNode()
    output_index = target_node.outputConnectors()[0][0].inputIndex()
    output_node.setInput(output_index, hex_node)
    
    hex_node.setPosition(target_node.position())
    hex_node.setNamedInput("position",xform_node,0)
    target_node.destroy() # delete tex node

x_pos /= len(target_nodes)
y_pos /= len(target_nodes)
x_pos -= 5
new_pos = hou.Vector2(x_pos,y_pos)

xform_node.setPosition(new_pos)
position_node.setPosition(new_pos - hou.Vector2(3,0))
