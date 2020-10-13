import adsk.core, adsk.fusion, adsk.cam, traceback



def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui  = app.userInterface

        def extrudeFloxer(returnValue, FlowerNb5):
            try:
                app = adsk.core.Application.get()
                ui  = app.userInterface

                
                design = app.activeProduct
                rootComp = design.rootComponent
                
                if len(returnValue) > 9:
                    returnValue = returnValue[:9]
                if len(returnValue)%2 == 0:
                    returnValue = returnValue + ' '
                while len(returnValue) != 9:
                    returnValue = ' ' + returnValue + ' '
                j=0
                for i in range (FlowerNb5*10+14,FlowerNb5*10+23):#33

                    # Grab the sketch and first text entity
                    ChangeText = 'Sketch' + str(i)
                    sk = rootComp.sketches.itemByName(ChangeText) 
                    skText = sk.sketchTexts.item(0)

                    # Change the text.
                    #skText.height = 2
                    skText.text = returnValue[i-(FlowerNb5*10+14)]
                    #skText.fontName = 'Courier'            
                    #continue
                    #if it's a blank char, do nothing
                    if returnValue[i-(FlowerNb5*10+14)] == " ":
                        continue    # continue here

                    j=i-(FlowerNb5*10+14)
                    distance = 1.9#0.4 + j*0.15
                    if (j)%2 == 0:
                        #even
                        distance += 0.9
                    
                    mm100 = adsk.core.ValueInput.createByString("100 mm")
                    extent_distance = adsk.fusion.DistanceExtentDefinition.create(mm100) 
                    #extent_distance = adsk.fusion.DistanceExtentDefinition.create(mm10)
                    #Create an extrusion input
                    extrudes = rootComp.features.extrudeFeatures
                    extInput = extrudes.createInput(skText, adsk.fusion.FeatureOperations.CutFeatureOperation)
                    if (j)%2 == 0:
                        #even so bottom flower
                        #distance += 0.9
                        extInput.setOneSideExtent(extent_distance, adsk.fusion.ExtentDirections.NegativeExtentDirection) 
                    else:
                        #odd so top flower
                        extInput.setOneSideExtent(extent_distance, adsk.fusion.ExtentDirections.PositiveExtentDirection)
                    #extInput.startExtent = adsk.fusion.FromEntityStartDefinition.create(extrudes.item(0),0)
                    #extInput.setDistanceExtent(True, distance)
                    #extInput.setSymmetricExtent(adsk.core.ValueInput.createByReal(distance), True) 
                    extInput.isSolid = True

                    # Create the extrusion
                    ext = extrudes.add(extInput)
                    
                    
                    


            except:
                if ui:
                    ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))

                # Get the sketch named "ChangeText"
                #sk = rootComp.sketches.itemByName(ChangeText)
                
                # Get the first sketch text.
                #skText = sk.sketchTexts.item(0)


        (returnValue1, cancelled) = ui.inputBox('idk', 'idk2', )
        (returnValue2, cancelled) = ui.inputBox('idk', 'idk2', )
        (returnValue3, cancelled) = ui.inputBox('idk', 'idk2', )
        (returnValue4, cancelled) = ui.inputBox('idk', 'idk2', )
        (returnValue5, cancelled) = ui.inputBox('idk', 'idk2', )
        (returnValue6, cancelled) = ui.inputBox('idk', 'idk2', )

        extrudeFloxer(returnValue1, 1)
        extrudeFloxer(returnValue2, 2)
        extrudeFloxer(returnValue3, 3)
        extrudeFloxer(returnValue4, 4)
        extrudeFloxer(returnValue5, 5)
        extrudeFloxer(returnValue6, 6)
    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))

