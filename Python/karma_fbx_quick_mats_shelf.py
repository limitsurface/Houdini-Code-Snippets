def karma_material_builder(target_node, mat_name):
    # target_node = hou.selectedNodes()[0]

    # Code for /obj/geo1/matnet1/karmamaterial
    karma_subnet = target_node.createNode("subnet", mat_name, run_init_scripts=False, load_contents=True, exact_type_name=True)
    karma_subnet.setDebugFlag(False)
    karma_subnet.setDetailLowFlag(False)
    karma_subnet.setDetailMediumFlag(False)
    karma_subnet.setDetailHighFlag(True)
    karma_subnet.bypass(False)
    karma_subnet.setCompressFlag(True)
    karma_subnet.hide(False)

    hou_parm_template_group = hou.ParmTemplateGroup()
    # Code for parameter template
    hou_parm_template = hou.FolderParmTemplate("folder1", "Karma Material Builder", folder_type=hou.folderType.Collapsible, default_value=0, ends_tab_group=False)
    hou_parm_template.setTags({"group_type": "collapsible", "sidefx::shader_isparm": "0"})
    # Code for parameter template
    hou_parm_template2 = hou.IntParmTemplate("inherit_ctrl", "Inherit from Class", 1, default_value=([2]), min=0, max=10, min_is_strict=False, max_is_strict=False, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.Base1, menu_items=(["0","1","2"]), menu_labels=(["Never","Always","Material Flag"]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal, menu_use_token=False)
    hou_parm_template.addParmTemplate(hou_parm_template2)
    # Code for parameter template
    hou_parm_template2 = hou.StringParmTemplate("shader_referencetype", "Class Arc", 1, default_value=(["n = hou.pwd()\nn_hasFlag = n.isMaterialFlagSet()\ni = n.evalParm('inherit_ctrl')\nr = 'none'\nif i == 1 or (n_hasFlag and i == 2):\n    r = 'inherit'\nreturn r"]), default_expression=(["n = hou.pwd()\nn_hasFlag = n.isMaterialFlagSet()\ni = n.evalParm('inherit_ctrl')\nr = 'none'\nif i == 1 or (n_hasFlag and i == 2):\n    r = 'inherit'\nreturn r"]), default_expression_language=([hou.scriptLanguage.Python]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.Regular, menu_items=(["none","reference","inherit","specialize","represent"]), menu_labels=(["None","Reference","Inherit","Specialize","Represent"]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal)
    hou_parm_template2.setTags({"sidefx::shader_isparm": "0", "spare_category": "Shader"})
    hou_parm_template.addParmTemplate(hou_parm_template2)
    # Code for parameter template
    hou_parm_template2 = hou.StringParmTemplate("shader_baseprimpath", "Class Prim Path", 1, default_value=(["/__class_mtl__/`$OS`"]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.Regular, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal)
    hou_parm_template2.setTags({"script_action": "import loputils\nloputils.selectPrimsInParm(kwargs, False)", "script_action_help": "Select a primitive in the Scene Viewer or Scene Graph Tree pane.\nCtrl-click to select using the primitive picker dialog.", "script_action_icon": "BUTTONS_reselect", "sidefx::shader_isparm": "0", "sidefx::usdpathtype": "prim", "spare_category": "Shader"})
    hou_parm_template.addParmTemplate(hou_parm_template2)
    # Code for parameter template
    hou_parm_template2 = hou.SeparatorParmTemplate("separator1")
    hou_parm_template.addParmTemplate(hou_parm_template2)
    # Code for parameter template
    hou_parm_template2 = hou.StringParmTemplate("tabmenumask", "Tab Menu Mask", 1, default_value=(["karma USD ^mtlxramp* ^hmtlxramp* ^hmtlxcubicramp* MaterialX parameter constant collect null genericshader subnet subnetconnector suboutput subinput"]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.Regular, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal)
    hou_parm_template2.setTags({"spare_category": "Tab Menu"})
    hou_parm_template.addParmTemplate(hou_parm_template2)
    # Code for parameter template
    hou_parm_template2 = hou.StringParmTemplate("shader_rendercontextname", "Render Context Name", 1, default_value=(["kma"]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.Regular, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal)
    hou_parm_template2.setTags({"sidefx::shader_isparm": "0", "spare_category": "Shader"})
    hou_parm_template.addParmTemplate(hou_parm_template2)
    # Code for parameter template
    hou_parm_template2 = hou.ToggleParmTemplate("shader_forcechildren", "Force Translation of Children", default_value=True)
    hou_parm_template2.setTags({"sidefx::shader_isparm": "0", "spare_category": "Shader"})
    hou_parm_template.addParmTemplate(hou_parm_template2)
    hou_parm_template_group.append(hou_parm_template)
    karma_subnet.setParmTemplateGroup(hou_parm_template_group)

    # Code for /obj/geo1/matnet1/karmamaterial/folder1 parm 
    if locals().get("karma_subnet") is None:
        karma_subnet = hou.node("/obj/geo1/matnet1/karmamaterial")
    hou_parm = karma_subnet.parm("folder1")
    hou_parm.lock(False)
    hou_parm.deleteAllKeyframes()
    hou_parm.set(0)
    hou_parm.setAutoscope(False)

    # Code for /obj/geo1/matnet1/karmamaterial/inherit_ctrl parm 
    if locals().get("karma_subnet") is None:
        karma_subnet = hou.node("/obj/geo1/matnet1/karmamaterial")
    hou_parm = karma_subnet.parm("inherit_ctrl")
    hou_parm.lock(False)
    hou_parm.deleteAllKeyframes()
    hou_parm.set(2)
    hou_parm.setAutoscope(False)

    # Code for /obj/geo1/matnet1/karmamaterial/shader_referencetype parm 
    if locals().get("karma_subnet") is None:
        karma_subnet = hou.node("/obj/geo1/matnet1/karmamaterial")
    hou_parm = karma_subnet.parm("shader_referencetype")
    hou_parm.lock(False)
    hou_parm.deleteAllKeyframes()
    hou_parm.set("inherit")
    hou_parm.setAutoscope(False)

    # Code for first keyframe.
    # Code for keyframe.
    hou_keyframe = hou.StringKeyframe()
    hou_keyframe.setTime(0)
    hou_keyframe.setExpression("n = hou.pwd()\nn_hasFlag = n.isMaterialFlagSet()\ni = n.evalParm('inherit_ctrl')\nr = 'none'\nif i == 1 or (n_hasFlag and i == 2):\n    r = 'inherit'\nreturn r", hou.exprLanguage.Python)
    hou_parm.setKeyframe(hou_keyframe)

    # Code for last keyframe.
    # Code for keyframe.
    hou_keyframe = hou.StringKeyframe()
    hou_keyframe.setTime(0)
    hou_keyframe.setExpression("n = hou.pwd()\nn_hasFlag = n.isMaterialFlagSet()\ni = n.evalParm('inherit_ctrl')\nr = 'none'\nif i == 1 or (n_hasFlag and i == 2):\n    r = 'inherit'\nreturn r", hou.exprLanguage.Python)
    hou_parm.setKeyframe(hou_keyframe)

    # Code for keyframe.
    hou_keyframe = hou.StringKeyframe()
    hou_keyframe.setTime(0)
    hou_keyframe.setExpression("n = hou.pwd()\nn_hasFlag = n.isMaterialFlagSet()\ni = n.evalParm('inherit_ctrl')\nr = 'none'\nif i == 1 or (n_hasFlag and i == 2):\n    r = 'inherit'\nreturn r", hou.exprLanguage.Python)
    hou_parm.setKeyframe(hou_keyframe)

    # Code for keyframe.
    hou_keyframe = hou.StringKeyframe()
    hou_keyframe.setTime(0)
    hou_keyframe.setExpression("n = hou.pwd()\nn_hasFlag = n.isMaterialFlagSet()\ni = n.evalParm('inherit_ctrl')\nr = 'none'\nif i == 1 or (n_hasFlag and i == 2):\n    r = 'inherit'\nreturn r", hou.exprLanguage.Python)
    hou_parm.setKeyframe(hou_keyframe)

    # Code for /obj/geo1/matnet1/karmamaterial/shader_baseprimpath parm 
    if locals().get("karma_subnet") is None:
        karma_subnet = hou.node("/obj/geo1/matnet1/karmamaterial")
    hou_parm = karma_subnet.parm("shader_baseprimpath")
    hou_parm.lock(False)
    hou_parm.deleteAllKeyframes()
    hou_parm.set("/__class_mtl__/`$OS`")
    hou_parm.setAutoscope(False)


    # Code for /obj/geo1/matnet1/karmamaterial/tabmenumask parm 
    if locals().get("karma_subnet") is None:
        karma_subnet = hou.node("/obj/geo1/matnet1/karmamaterial")
    hou_parm = karma_subnet.parm("tabmenumask")
    hou_parm.lock(False)
    hou_parm.deleteAllKeyframes()
    hou_parm.set("karma USD ^mtlxramp* ^hmtlxramp* ^hmtlxcubicramp* MaterialX parameter constant collect null genericshader subnet subnetconnector suboutput subinput")
    hou_parm.setAutoscope(False)

    # Code for /obj/geo1/matnet1/karmamaterial/shader_rendercontextname parm 
    if locals().get("karma_subnet") is None:
        karma_subnet = hou.node("/obj/geo1/matnet1/karmamaterial")
    hou_parm = karma_subnet.parm("shader_rendercontextname")
    hou_parm.lock(False)
    hou_parm.deleteAllKeyframes()
    hou_parm.set("kma")
    hou_parm.setAutoscope(False)

    # Code for /obj/geo1/matnet1/karmamaterial/shader_forcechildren parm 
    if locals().get("karma_subnet") is None:
        karma_subnet = hou.node("/obj/geo1/matnet1/karmamaterial")
    hou_parm = karma_subnet.parm("shader_forcechildren")
    hou_parm.lock(False)
    hou_parm.deleteAllKeyframes()
    hou_parm.set(1)
    hou_parm.setAutoscope(False)
    
    karma_subnet.setExpressionLanguage(hou.exprLanguage.Hscript)
    if hasattr(karma_subnet, "syncNodeVersionIfNeeded"):
        karma_subnet.syncNodeVersionIfNeeded("20.0.547")
    
    subinput_node = karma_subnet.createNode("subinput", mat_name+"_inputs")
    suboutput_node = karma_subnet.createNode("suboutput", mat_name+"_Outputs_and_AOVs")
    surface_node = karma_subnet.createNode("mtlxstandard_surface", mat_name+"_surface")
    displacement_node = karma_subnet.createNode("mtlxdisplacement", mat_name+"_displacement")
    properties_node = karma_subnet.createNode("kma_material_properties", mat_name+"_properties")


    suboutput_node.setInput(0, surface_node)
    suboutput_node.setInput(1, displacement_node)
    suboutput_node.setInput(2, properties_node)

    suboutput_node.parm("name1").set("surface")
    suboutput_node.parm("name2").set("displacement")
    suboutput_node.parm("name3").set("properties")

    karma_subnet.moveToGoodPosition()
    karma_subnet.layoutChildren()

    surface_preview = karma_subnet.createNode("mtlxsurface_unlit", "surface_preview")
    surface_preview.setPosition(suboutput_node.position() + hou.Vector2(0,3))

# example call
# karma_material_builder("test_name")


# majority of code generated using:
# https://github.com/NCCA/ScriptingForDCC/blob/master/houAsCode.py


import numpy as np

target_node = hou.selectedNodes()[0]
parent = target_node.parent()
geo = target_node.geometry()
mat_list = geo.findPrimAttrib("shop_materialpath").strings()
matnet = parent.createNode("matnet", node_name=str(target_node)+"_matnet")

pos = target_node.position()
matnet.setPosition(pos + hou.Vector2(3,0))

new_mats = []
for mat in mat_list:
    clean_name = "".join(ch for ch in str(mat) if ch.isalnum())
    new_mat = karma_material_builder(matnet, clean_name)
    new_mats.append(new_mat)
    karma_surface_node = new_mat.children()[2]
    karma_surface_node.setParms({"base_color":np.clip(np.random.rand(3), 0.05, 0.7)})
    karma_surface_node.setParms({"specular_roughness":np.clip(np.random.rand(1)[0], 0.1, 0.7)})

matnet.layoutChildren()

# material_node = parent.createNode("material", node_name=str(target_node)+"_mats")
# material_node.setInput(0, target_node)
# material_node.setParms({"num_materials":len(new_mats)})
# material_node.moveToGoodPosition(relative_to_inputs=True)

# for count, mat in enumerate(new_mats):
#     mat_parm_name = "shop_materialpath"+str(count+1)
#     group_parm_name = "group"+str(count+1)
#     group_val = "@shop_materialpath=\""+str(mat_list[count])+"\""
#     material_node.setParms({mat_parm_name:mat.path()})
#     material_node.setParms({group_parm_name:group_val})

# material_node.setDisplayFlag(True)
# material_node.setRenderFlag(True)
