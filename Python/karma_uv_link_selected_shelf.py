target_nodes = hou.selectedNodes()
parent_node = target_nodes[0].parent()

uv_node = parent_node.createNode("mtlxtexcoord", "uv_coords")
xform_node = parent_node.createNode("usdtransform2d", "xform")
xform_node.setInput(0, uv_node)

x_pos = 0
y_pos = 0

for target_node in target_nodes:
    target_node.setNamedInput("texcoord",xform_node,0)
    x_pos += target_node.position()[0]
    y_pos += target_node.position()[0]

x_pos /= len(target_nodes)
y_pos /= len(target_nodes)
x_pos -= 5
new_pos = hou.Vector2(x_pos,y_pos)

xform_node.setPosition(new_pos)
uv_node.setPosition(new_pos - hou.Vector2(-3,0))
