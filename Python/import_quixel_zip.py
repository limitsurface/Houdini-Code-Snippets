# import quixel assets from fab
# select zip file
# fbx's end up in SOPs
# karma materials end up in solaris in the first existing material library or in a new one

import hou
import zipfile
import os
import json
from PySide2 import QtWidgets
from PySide2.QtWidgets import QFileDialog

def karma_material_builder(target_node, mat_name):
    # Code for karmamaterial
    karma_subnet = target_node.createNode("subnet", mat_name, run_init_scripts=False, load_contents=True, exact_type_name=True)
    karma_subnet.setDebugFlag(False)
    karma_subnet.setDetailLowFlag(False)
    karma_subnet.setDetailMediumFlag(False)
    karma_subnet.setDetailHighFlag(True)
    karma_subnet.bypass(False)
    karma_subnet.setCompressFlag(True)
    karma_subnet.hide(False)
    karma_subnet.setMaterialFlag(True)

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

    # Code for karmamaterial/folder1 parm 
    if locals().get("karma_subnet") is None:
        karma_subnet = hou.node("karmamaterial")
    hou_parm = karma_subnet.parm("folder1")
    hou_parm.lock(False)
    hou_parm.deleteAllKeyframes()
    hou_parm.set(0)
    hou_parm.setAutoscope(False)

    # Code for karmamaterial/inherit_ctrl parm 
    if locals().get("karma_subnet") is None:
        karma_subnet = hou.node("karmamaterial")
    hou_parm = karma_subnet.parm("inherit_ctrl")
    hou_parm.lock(False)
    hou_parm.deleteAllKeyframes()
    hou_parm.set(2)
    hou_parm.setAutoscope(False)

    # Code for karmamaterial/shader_referencetype parm 
    if locals().get("karma_subnet") is None:
        karma_subnet = hou.node("karmamaterial")
    hou_parm = karma_subnet.parm("shader_referencetype")
    hou_parm.lock(False)
    hou_parm.deleteAllKeyframes()
    hou_parm.set("inherit")
    hou_parm.setAutoscope(False)


    # Code for karmamaterial/shader_baseprimpath parm 
    if locals().get("karma_subnet") is None:
        karma_subnet = hou.node("karmamaterial")
    hou_parm = karma_subnet.parm("shader_baseprimpath")
    hou_parm.lock(False)
    hou_parm.deleteAllKeyframes()
    hou_parm.set("/__class_mtl__/`$OS`")
    hou_parm.setAutoscope(False)

    # Code for karmamaterial/tabmenumask parm 
    if locals().get("karma_subnet") is None:
        karma_subnet = hou.node("karmamaterial")
    hou_parm = karma_subnet.parm("tabmenumask")
    hou_parm.lock(False)
    hou_parm.deleteAllKeyframes()
    hou_parm.set("karma USD ^mtlxramp* ^hmtlxramp* ^hmtlxcubicramp* MaterialX parameter constant collect null genericshader subnet subnetconnector suboutput subinput")
    hou_parm.setAutoscope(False)

    # Code for karmamaterial/shader_rendercontextname parm 
    if locals().get("karma_subnet") is None:
        karma_subnet = hou.node("karmamaterial")
    hou_parm = karma_subnet.parm("shader_rendercontextname")
    hou_parm.lock(False)
    hou_parm.deleteAllKeyframes()
    hou_parm.set("kma")
    hou_parm.setAutoscope(False)

    # Code for karmamaterial/shader_forcechildren parm 
    if locals().get("karma_subnet") is None:
        karma_subnet = hou.node("karmamaterial")
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
    
    return karma_subnet

def select_zip_file():
    # Open a file dialog to Select the zip file
    file_dialog = QFileDialog()
    file_dialog.setFileMode(QFileDialog.ExistingFile)
    file_dialog.setNameFilter("Zip Files (*.zip)")
    if file_dialog.exec_():
        return file_dialog.selectedFiles()[0]
    return None

def extract_zip(zip_file, extract_dir):
    # Extract the zip file into the specified directory
    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        zip_ref.extractall(extract_dir)

def read_json(json_file):
    # Read JSON file and print the values of ["semanticTags"]["name"]
    with open(json_file, 'r') as file:
        data = json.load(file)
        name = data["semanticTags"]["name"]
        # print("Tag Name:", name)
        return name

def convert_to_houdini_path(path, job_dir):
    """Convert absolute path to a Houdini path relative to $JOB"""
    if path.startswith(job_dir):
        relative_path = path.replace(job_dir, "$JOB", 1).replace("\\", "/")
        return relative_path
    return path

def find_asset_files(extract_path, job_dir):
    # Dictionary for texture files
    texture_keywords = {
        "_BaseColor": None,
        "_Displacement": None,
        "_Metalness": None,
        "_Normal": None,
        "_Roughness": None
    }
    
    fbx_file = None  # Variable to store FBX file path
    
    # Walk through the extracted folder
    for root, dirs, files in os.walk(extract_path):
        for file in files:
            # Split the file name and extension
            filename, ext = os.path.splitext(file)
            if ext.lower() in ['.png', '.jpg', '.jpeg', '.tiff', '.tga', '.exr']:  # Check for common image extensions
                for keyword in texture_keywords.keys():
                    if filename.endswith(keyword):
                        abs_path = os.path.join(root, file)
                        texture_keywords[keyword] = convert_to_houdini_path(abs_path, job_dir)
                        break
            elif ext.lower() == '.fbx':  # Check for FBX files
                abs_path = os.path.join(root, file)
                fbx_file = convert_to_houdini_path(abs_path, job_dir)

    # Print the dictionary of found textures
    print("Found the following texture files (with $JOB paths):")
    for key, value in texture_keywords.items():
        if value:
            # print(f"{key}: {value}")
            print(f"{key}")
        else:
            print(f"{key}: Not found")
    
    # Print the FBX file path if found
    if fbx_file:
        # print(f"FBX File Found: {fbx_file}")
        print(f"FBX File Found")
    else:
        print("No FBX file found.")
    
    return texture_keywords, fbx_file

def delete_unwanted_files(extract_path):
    """Delete files whose names end with _Bump or _Gloss"""
    for root, dirs, files in os.walk(extract_path):
        for file in files:
            filename, ext = os.path.splitext(file)
            if filename.endswith('_Bump') or filename.endswith('_Gloss') or filename.endswith('_Specular'):
                file_to_delete = os.path.join(root, file)
                try:
                    os.remove(file_to_delete)
                    print(f"Deleted: {file_to_delete.split('_')[-1]}")
                except OSError as e:
                    print(f"Error deleting file {file_to_delete}: {e}")

def create_file_node(sop, fbx_file, name):
    file_node = sop.createNode("file", name)
    file_node.parm("file").set(fbx_file)
    name_node = sop.createNode("name", name)
    name_node.parm("name1").set(name)
    attrib_del = sop.createNode("attribdelete", "clean_attribs")
    attrib_del.parm("ptdel").set("fbx*")
    attrib_del.parm("primdel").set("shop*")
    attrib_del.parm("dtldel").set("*")
    group_del = sop.createNode("groupdelete", "clean_groups")
    group_del.parm("group1").set("*")
    out_null = sop.createNode("null", "OUT_"+name)
    xform = sop.createNode("xform", "fix_scale")
    xform.parm("scale").set(0.01)
    xform.setInput(0, file_node, 0)
    attrib_del.setInput(0, xform, 0)
    group_del.setInput(0, attrib_del, 0)
    name_node.setInput(0, group_del, 0)
    out_null.setInput(0, name_node, 0)
    out_null.setDisplayFlag(True)
    out_null.setRenderFlag(True)
    sop.layoutChildren()

def attach_maps(karma_subnet, texture_dict):
    basecolor_texture = texture_dict.get("_BaseColor")
    metalness_texture = texture_dict.get("_Metalness")
    roughness_texture = texture_dict.get("_Roughness")
    normal_texture = texture_dict.get("_Normal")
    displacement_texture = texture_dict.get("_Displacement")

    karma_surface_node = karma_subnet.children()[2]
    karma_displacement_node = karma_subnet.children()[3]
    
    if basecolor_texture:
        basecolor_node = karma_subnet.createNode("mtlximage", "base_color")
        basecolor_node.parm("file").setValueFromData(basecolor_texture)
        basecolor_cc = karma_subnet.createNode("mtlxcolorcorrect", "base_color_CC")
        basecolor_cc.setInput(0, basecolor_node, 0)
        karma_surface_node.setInput(1, basecolor_cc, 0)
    
    if metalness_texture:
        metalness_node = karma_subnet.createNode("mtlximage", "metalness")
        metalness_node.parm("file").setValueFromData(metalness_texture)
        metalness_node.parm("signature").set("default")
        karma_surface_node.setInput(3, metalness_node, 0)

    if roughness_texture:
        roughness_node = karma_subnet.createNode("mtlximage", "roughness")
        roughness_node.parm("file").setValueFromData(roughness_texture)
        roughness_node.parm("signature").set("default")
        roughness_ramp = karma_subnet.createNode("kma_rampconst", "roughness_ramp")
        roughness_ramp.parm("signature").set("float")
        roughness_ramp.setInput(0, roughness_node, 0)
        karma_surface_node.setInput(6, roughness_ramp, 0)

    if normal_texture:
        normal_node = karma_subnet.createNode("mtlximage", "normal")
        normal_node.parm("file").setValueFromData(normal_texture)
        normal_node.parm("signature").set("vector3")
        normal_intensity = karma_subnet.createNode("mtlxnormalmap", "normal_intensity")
        normal_intensity.setInput(0, normal_node, 0)
        karma_surface_node.setInput(40, normal_intensity, 0)
    
    if displacement_texture:
        # print("disp")
        displacement_node = karma_subnet.createNode("mtlximage", "displacement")
        displacement_node.parm("file").setValueFromData(displacement_texture)
        displacement_node.parm("signature").set("default")
        displacement_range = karma_subnet.createNode("mtlxrange", "fit_range")
        displacement_range.parm("outlow").set(-0.5)
        displacement_range.parm("outhigh").set(0.5)
        karma_displacement_node.parm("scale").set(0.001)
        karma_displacement_node.setInput(0, displacement_range, 0)
        displacement_range.setInput(0, displacement_node, 0)

    karma_subnet.layoutChildren()

    return

def main():
    # Get the current Houdini $JOB directory
    job_dir = hou.getenv('JOB')
    
    if not job_dir:
        hou.ui.displayMessage("$JOB is not set. Please set it before running the script.")
        return
    
    # Define the destination path for extracted assets inside $JOB
    asset_dir = os.path.join(job_dir, 'imported', 'quixel_assets')
    
    # Create the directory if it doesn't exist
    if not os.path.exists(asset_dir):
        os.makedirs(asset_dir)
    
    # Ask the user to select a zip file
    zip_file = select_zip_file()
    if zip_file is None:
        hou.ui.displayMessage("No zip file selected.")
        return
    
    # Create a unique folder name for the asset inside quixel_assets
    asset_folder_name = os.path.splitext(os.path.basename(zip_file))[0]
    extract_path = os.path.join(asset_dir, asset_folder_name)
    
    if not os.path.exists(extract_path):
        os.makedirs(extract_path)
    
    # Extract the zip file into the asset folder
    extract_zip(zip_file, extract_path)
    
    # Look for a JSON file in the extracted folder
    json_file = None
    for root, dirs, files in os.walk(extract_path):
        for file in files:
            if file.endswith('.json'):
                json_file = os.path.join(root, file)
                break
    
    if not json_file:
        hou.ui.displayMessage("No JSON file found in the extracted folder.")
    

    # Find and store paths of specific texture files and the FBX file
    texture_dict, fbx_file = find_asset_files(extract_path, job_dir)
    
    # Delete unwanted files (_Bump and _Gloss)
    delete_unwanted_files(extract_path)
    
    # get asset name
    asset_name = read_json(json_file).replace(" ", "_")

    # Get first material library in the stage
    stage = hou.node("/stage")
    children = stage.children()
    material_library = None
    for child in children:
        if child.type().name() == "materiallibrary":
            material_library = child
            break
    if not material_library:
        material_library = stage.createNode("materiallibrary", "material_library")

    # Create the material
    karma_subnet = karma_material_builder(material_library, asset_name)
    attach_maps(karma_subnet, texture_dict)
    print("Created "+karma_subnet.name()+" in "+material_library.path())

    if fbx_file:
        root = hou.node("/obj/")
        sop = root.createNode("geo", asset_name)
        create_file_node(sop, fbx_file, asset_name)

# Run the main function
main()