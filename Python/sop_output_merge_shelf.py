target_nodes = hou.selectedNodes()
parent = target_nodes[0].parent()

for target_node in target_nodes:
    target_name = target_node.name()
    if target_name.startswith("OUT_"):
        target_name = target_name[4:]
    else:
        target_node.setName("OUT_"+target_name)
    merge_name = "MERGE_"+target_name

    new_merge = parent.createNode("object_merge", merge_name)
    new_merge.setPosition(target_node.position() + hou.Vector2(0,-2))


    new_merge.setParms({"objpath1":target_node.path()})