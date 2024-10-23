import re
import math
target_nodes = hou.selectedNodes()
stage = root = hou.node("/stage")

for target_node in target_nodes:
    if target_node.type().name() != "cam":
        target_node.setColor(hou.Color((1,0,0)))
        node_name = target_node.name()
        if not node_name.startswith("SOLARIS_"):
            new_name = "SOLARIS_" + node_name
            target_node.setName(new_name)
            
        name = re.findall(r'_(.*)$', target_node.name())[-1]
        sop_import = stage.createNode("sopimport", name)
        sop_import.setParms({"soppath":target_node.path()})
        sop_import.setParms({"pathprefix":"/geo/"+name})
        sop_import.parm("enable_partitionattribs").setValueFromData(1)
        sop_import.parm("enable_prefixpartitionsubsets").setValueFromData(1)
        sop_import.parm("prefixpartitionsubsets").setValueFromData(0)
        sop_import.parm("partitionattribs").setValueFromData("subset")
        sop_import.parm("enable_packedhandling").setValueFromData(1)
        sop_import.parm("packedhandling").setValueFromData("pointinstancer")
        sop_import.moveToGoodPosition()
        
    elif target_node.type().name() == "cam":
        result = hou.ui.displayMessage(
            "Link Cameras?", 
            buttons=("Yes", "No"), 
            default_choice=1,  # default selected option (0 for Yes)
            close_choice=1     # option to choose if user closes the dialog (1 for No)
        )
        if result == 0:
            target_node.setName("LINKED_"+target_node.name())
            stage_cam = stage.createNode("sceneimport::2.0", "LINKED_"+target_node.name())
            stage_cam.parm("objdestpath").setValueFromData("/cameras/")
            stage_cam.parm("filter").setValueFromData("!!OBJ/CAMERA!!")
            stage_cam.parm("objects").setValueFromData(target_node.path())
            stage_cam.parm("flatten").setValueFromData(1)
        else:
            stage_cam = stage.createNode("camera", target_node.name())
            stage_cam.parmTuple("t").setValueFromData(target_node.parmTuple("t").valueAsData())
            stage_cam.parmTuple("r").setValueFromData(target_node.parmTuple("r").valueAsData())
            stage_cam.parm("focalLength").setValueFromData(target_node.parm("focal").valueAsData())
            stage_cam.parm("horizontalAperture").setValueFromData(target_node.parm("aperture").valueAsData())
            stage_cam.parm("clippingRange1").setValueFromData(0.1)

            # aspect = target_node.parm("resy").eval()/target_node.parm("resx").eval()
            # aspect = math.floor(aspect * 30)/30
            # stage_cam.parmTuple("aspectratio").setValueFromData([target_node.parm("resx").asData(),target_node.parm("resy").asData()])
            stage_cam.parm("aspectratiox").setValueFromData(target_node.parm("resx").asData())
            stage_cam.parm("aspectratioy").setValueFromData(target_node.parm("resy").asData())
            stage_cam.moveToGoodPosition()

