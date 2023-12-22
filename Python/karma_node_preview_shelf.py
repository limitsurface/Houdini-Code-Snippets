target_node = hou.selectedNodes()[0]
parent = target_node.parent()
parent_nodes = parent.children()

subnet_output = None
unlit_shader = None

for node in parent_nodes:
    type_name = node.type().name()
    if type_name == "mtlxsurface_unlit":
        unlit_shader = node
    if type_name == "suboutput":
        subnet_output = node

if not unlit_shader:
    unlit_shader = parent.createNode("mtlxsurface_unlit", "surface_preview")
    unlit_shader.setPosition(subnet_output.position() + hou.Vector2(0,3))

target_node_type = target_node.type().name()

if target_node_type == "mtlxstandard_surface":
    subnet_output.setInput(0, target_node)
    unlit_shader.setInput(1, None)
elif target_node_type == "mtlxmix":
    input_list = target_node.inputs()
    test = 0
    for ins in input_list:
        type_name = ins.type().name()
        if type_name == "mtlxstandard_surface":
            test = 1
            break
    if test == 1:
        subnet_output.setInput(0, target_node)
        unlit_shader.setInput(1, None)
    else:
        subnet_output.setInput(0, unlit_shader)
        unlit_shader.setInput(1, target_node)
else:
    subnet_output.setInput(0, unlit_shader)
    unlit_shader.setInput(1, target_node)