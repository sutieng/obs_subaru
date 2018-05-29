import lsst.afw.cameraGeom.cameraConfig
assert type(config) == lsst.afw.cameraGeom.cameraConfig.CameraConfig, 'config is of type %s.%s instead of lsst.afw.cameraGeom.cameraConfig.CameraConfig' % (
    type(config).__module__, type(config).__name__)
# Plate scale of the camera in arcsec/mm
# Based on pixel scale of 0.23 arcsec/pix
config.plateScale = 41.818
config.transformDict.nativeSys = 'FocalPlane'



config.transformDict.transforms = {}
config.transformDict.transforms['FieldAngle'] = lsst.afw.geom.transformConfig.TransformConfig()
config.transformDict.transforms['FieldAngle'].transform['multi'].transformDict = None
# x, y translation vector
config.transformDict.transforms['FieldAngle'].transform['affine'].translation = [0.0, 0.0]

# 2x2 linear matrix in the usual numpy order;
#             to rotate a vector by theta use: cos(theta), sin(theta), -sin(theta), cos(theta)
config.transformDict.transforms['FieldAngle'].transform['affine'].linear = [1.0, 0.0, 0.0, 1.0]
# Coefficients for the radial polynomial; coeff[0] must be 0
print ("CAMERA.PY WARNING: Pupil transform currently set to 'radial', coeff are not sure now.")
config.transformDict.transforms['FieldAngle'].transform['radial'].coeffs = [0.0, 1.0] ###not sure the coeff now, just set it to [0,1] # radial distortion coefficients (c_0 + c_1 r + c_2 r^2 + ...)

config.transformDict.transforms['FieldAngle'].transform.name = 'radial'

'''
config.transformDict.transforms['Pupil'] = lsst.afw.geom.transformConfig.TransformConfig()
config.transformDict.transforms['Pupil'].transform['hsc'].skyToCcdOrder = 9
config.transformDict.transforms['Pupil'].transform['hsc'].ccdToSkyOrder = 9
config.transformDict.transforms['Pupil'].transform['hsc'].yCcdToSky = [-2.27525408678e-05, 0.999850561443607, 1.47288649136e-09, -1.07681558891e-10, -4.52745194926e-17, 5.33446374932e-21, 1.59765278412e-25, -1.35281754124e-28, -2.58952055468e-34, 1.18384181522e-37, -1.54279888831e-05, 5.10149451107e-09, -2.20369366154e-12, -8.12440053288e-17, 3.16674570469e-20, 2.36720490323e-25, -1.54887554063e-28, -2.18878587707e-34, 2.42019175449e-37, -1.36641013138e-09, -1.08210753878e-10, 3.24065404366e-17, 2.21741676333e-20, -3.30404486918e-25, -4.7223051146e-28, 8.48620744583e-34,
                                                                      5.84549240581e-37, 1.65013522193e-12, -2.04698537311e-16, 1.36596617211e-20, 8.77160647683e-25, -1.36731060152e-28, -1.43968368509e-33, 4.00898492827e-37, -2.27951193984e-17, 1.16796604208e-20, -6.53927583976e-25, -4.41168731276e-28, 1.38404520921e-33, 8.26267449077e-37, -1.75167734408e-20, 1.35671719277e-24, -5.56167978363e-29, -2.43608580718e-33, 9.3744233119e-38, 8.31436843296e-26, -1.73569476217e-28, 1.90770699097e-33, 4.98143401516e-37, 6.57627509385e-29, -2.64064071957e-33, 1.56461570921e-37, -1.50783715462e-34, 1.98549941035e-37, -8.74305862185e-38]
config.transformDict.transforms['Pupil'].transform['hsc'].maxIter = 10
config.transformDict.transforms['Pupil'].transform['hsc'].plateScale = 1.0
config.transformDict.transforms['Pupil'].transform['hsc'].xCcdToSky = [-0.00047203560468, -1.5427988883e-05, -5.95865625284e-10, 2.22594651446e-13, -1.51583805989e-17, -6.08317204253e-21, 8.06561200947e-26, 3.10689047143e-29, -1.2634302141e-34, -4.78814991762e-38, 0.999789566962328, 4.66142798084e-09, -1.0957097072e-10, -4.6906678848e-17, 4.22216001121e-20, 1.87541306804e-25, -3.11027701152e-28, -1.25424492312e-34, 3.70673801604e-37, -6.85371734365e-09, -1.26203995922e-14, -5.4517702042e-17, -9.94551136649e-22, 9.09298367647e-25, 2.45558081417e-29, -1.92962666077e-33, -
                                                                      6.7994922883e-38, -1.04551853816e-10, -1.95257983584e-17, 2.66068980901e-20, 2.05500547863e-25, -7.00557780822e-28, -1.27106133492e-33, 1.17427552052e-36, 5.48308544761e-17, -6.6977079558e-21, -3.88079500249e-26, -1.12430203404e-29, -2.3228732246e-33, 5.83996936659e-38, -2.55808760342e-20, -5.51546375606e-26, -4.43037636885e-28, 3.26328244851e-34, 1.30831113179e-36, -2.3965595459e-25, 7.38850410175e-29, 6.31709084288e-34, -5.69997824021e-38, -3.49962832225e-30, 9.21035992064e-35, 4.48010296471e-37, 2.36522390769e-34, -1.7686068989e-37, -8.6880691822e-38]
config.transformDict.transforms['Pupil'].transform['hsc'].ySkyToCcd = [-0.00243520601215, 1.000147893495017, -1.37763224595e-09, 1.07833848918e-10, 4.62596775002e-17, 2.80575848534e-20, -1.65367128388e-25, 1.54820423917e-28, 3.22741961727e-34, 7.08058901535e-39, 1.29459993973e-05, -5.75758775598e-09, 2.59566096648e-12, 8.89501051555e-17, -3.98215173203e-20, -2.42815205576e-25, 2.11105473817e-28, 2.17987210027e-34, -3.57655925495e-37, 1.71046572758e-09, 1.08416040618e-10, -5.39914444014e-17, 4.3772487775e-20, 5.39490871566e-25, 5.37804304106e-28, -1.33522335425e-33, -
                                                                       1.00922213245e-37, -1.61692503254e-12, 2.37001625897e-16, -1.87396962399e-20, -1.01303057487e-24, 1.88379875457e-28, 1.74279811617e-33, -5.95775054508e-37, 1.73901668516e-17, 2.03868624457e-20, 9.5148136402e-25, 4.98415367039e-28, -2.07693213639e-33, -7.27517738702e-38, 1.71531399232e-20, -1.65907556613e-24, 9.02531724098e-29, 3.06533133333e-33, -1.43492096446e-37, -4.32749987233e-26, 2.04328665654e-28, -2.81367089917e-33, 1.74213007753e-38, -6.279347973e-29, 3.45559728633e-33, -2.637596961e-37, 9.34962455855e-35, -1.03493809035e-37, 8.09745928121e-38]
config.transformDict.transforms['Pupil'].transform['hsc'].tolerance = 0.005
config.transformDict.transforms['Pupil'].transform['hsc'].xSkyToCcd = [0.00365271948353, 1.70911115723e-05, 1.5204217229e-10, -3.08715201043e-13, 2.39597939294e-17, 7.81157081952e-21, -1.29621716896e-25, -4.16263764639e-29, 2.15552971078e-34, 6.82597059998e-38, 1.000209404097794, -4.75019821106e-09, 1.10190607837e-10, 4.93339497018e-17, -1.85924839513e-20, -1.95896472784e-25, 3.88256510948e-28, 9.69693004122e-35, -3.47706701826e-37, 6.71381011215e-09, -9.50158088079e-14, 7.93173879809e-17, 1.60828614399e-21, -1.21754098187e-24, -2.62579677501e-29, 2.74663158936e-33,
                                                                      7.59945998098e-38, 1.04498582488e-10, 1.74134310921e-17, 3.24251148641e-20, -2.26265099203e-25, 8.70112786558e-28, 1.68537897358e-33, -9.78020507263e-37, -5.13651337215e-17, 1.04041291095e-20, -7.65133837619e-26, 3.53907656972e-30, 3.47366147648e-33, -8.85077550431e-38, 6.30556215478e-20, 9.43999734447e-26, 5.33882127553e-28, -3.92799329224e-34, -8.4676694827e-37, 2.185067016e-25, -1.09047001782e-28, -4.39266689902e-34, 1.31099098133e-37, -5.78460936624e-30, -1.38369955347e-34, 3.92691778634e-38, -1.23086882478e-34, 2.67441530618e-37, 2.76078356876e-37]
config.transformDict.transforms['Pupil'].transform['multi'].transformDict = None
config.transformDict.transforms['Pupil'].transform['affine'].translation = [0.0, 0.0]
config.transformDict.transforms['Pupil'].transform['affine'].linear = [1.0, 0.0, 0.0, 1.0]
config.transformDict.transforms['Pupil'].transform['radial'].coeffs = None
config.transformDict.transforms['Pupil'].transform.name = 'hsc'
'''
config.detectorList = {}



config.detectorList[0] = lsst.afw.cameraGeom.cameraConfig.DetectorConfig()

# y0 of pixel bounding box
config.detectorList[0].bbox_y0 = 0

# y1 of pixel bounding box
#config.detectorList[0].bbox_y1 = 4395
config.detectorList[0].bbox_y1 = 4383

#config.detectorList[0].bbox_x1 = 6600
config.detectorList[0].bbox_x1 = 6575

config.detectorList[0].bbox_x0 = 0

config.detectorList[0].name = 'superbitccd'  ##read superbitccd.fits

# Pixel size in the x dimension in mm
config.detectorList[0].pixelSize_x = 0.055
config.detectorList[0].transformDict.nativeSys = None
config.detectorList[0].transformDict.transforms = None

# x position of the reference point in the detector in pixels in transposed coordinates.
config.detectorList[0].refpos_x = 3288

# y position of the reference point in the detector in pixels in transposed coordinates.
config.detectorList[0].refpos_y = 2192

# Pixel size in the y dimension in mm
config.detectorList[0].pixelSize_y = 0.0055

# Detector type: SCIENCE=0, FOCUS=1, GUIDER=2, WAVEFRONT=3
config.detectorList[0].detectorType = 0

# x offset from the origin of the camera in mm in the transposed system.
#config.detectorList[0].offset_x =-185.59199999999998
config.detectorList[0].offset_x =0   ###not sure now

# y offset from the origin of the camera in mm in the transposed system.
#config.detectorList[0].offset_y =  -63.748000000000005
config.detectorList[0].offset_y =0  ###not sure now

# Transpose the pixel grid before orienting in focal plane?
config.detectorList[0].transposeDetector = None

# yaw (rotation about z) of the detector in degrees. This includes any
# necessary rotation to go from detector coordinates to camera coordinates
# after optional transposition.
config.detectorList[0].yawDeg = 0.00

# roll (rotation about x) of the detector in degrees
config.detectorList[0].rollDeg = 0.0

config.detectorList[0].serial = 'KAI-29050'
# pitch (rotation about y) of the detector in degrees
config.detectorList[0].pitchDeg = 0
config.detectorList[0].id = 1



config.radialCoeffs = None
config.name = 'SuperBIT'
