def iniList():
	# Section, Item, Object Name
	iniList = []
	iniList.append(['EMC', 'VERSION', 'versionLE'])
	iniList.append(['EMC', 'MACHINE', 'configName'])
	iniList.append(['EMC', 'DEBUG', 'debugCombo'])

	iniList.append(['HOSTMOT2', 'DRIVER', 'driverCB'])
	iniList.append(['HOSTMOT2', 'IPADDRESS', 'ipAddressCB'])
	iniList.append(['HOSTMOT2', 'BOARD', 'boardCB'])
	iniList.append(['HOSTMOT2', 'STEPGENS', 'stepgensSB'])
	iniList.append(['HOSTMOT2', 'ENCODERS', 'encodersSB'])
	iniList.append(['HOSTMOT2', 'SSERIAL_PORT', 'sserialSB'])

	iniList.append(['DISPLAY', 'DISPLAY', 'guiCB'])
	iniList.append(['DISPLAY', 'POSITION_OFFSET', 'positionOffsetCB'])
	iniList.append(['DISPLAY', 'POSITION_FEEDBACK', 'positionFeedbackCB'])
	iniList.append(['DISPLAY', 'MAX_FEED_OVERRIDE', 'maxFeedOverrideSB'])

	iniList.append(['EMCMOT', 'SERVO_PERIOD', 'servoPeriodSB'])

	iniList.append(['TRAJ', 'LINEAR_UNITS', 'linearUnitsCB'])
	iniList.append(['TRAJ', 'COORDINATES', 'coordinatesLB'])
	iniList.append(['TRAJ', 'MAX_LINEAR_VELOCITY', 'maxLinearVelocity'])

	for i in range(5):
		iniList.append(['JOINT_{}'.format(i), 'AXIS', 'axisCB_{}'.format(i)])
		iniList.append(['JOINT_{}'.format(i), 'STEPLEN', 'stepTime_{}'.format(i)])
		iniList.append(['JOINT_{}'.format(i), 'STEPSPACE', 'stepSpace_{}'.format(i)])
		iniList.append(['JOINT_{}'.format(i), 'DIRSETUP', 'dirSetup_{}'.format(i)])
		iniList.append(['JOINT_{}'.format(i), 'DIRHOLD', 'dirHold_{}'.format(i)])
		iniList.append(['JOINT_{}'.format(i), 'MIN_LIMIT', 'minLimit_{}'.format(i)])
		iniList.append(['JOINT_{}'.format(i), 'MAX_LIMIT', 'maxLimit_{}'.format(i)])
		iniList.append(['JOINT_{}'.format(i), 'MAX_VELOCITY', 'maxVelocity_{}'.format(i)])
		iniList.append(['JOINT_{}'.format(i), 'MAX_ACCELERATION', 'maxAccel_{}'.format(i)])
		iniList.append(['JOINT_{}'.format(i), 'SCALE', 'scale_{}'.format(i)])
		iniList.append(['JOINT_{}'.format(i), 'HOME', 'home_{}'.format(i)])
		iniList.append(['JOINT_{}'.format(i), 'HOME_OFFSET', 'homeOffset_{}'.format(i)])
		iniList.append(['JOINT_{}'.format(i), 'HOME_SEARCH_VEL', 'homeSearchVel_{}'.format(i)])
		iniList.append(['JOINT_{}'.format(i), 'HOME_LATCH_VEL', 'homeLatchVel_{}'.format(i)])
		iniList.append(['JOINT_{}'.format(i), 'HOME_USE_INDEX', 'homeUseIndex_{}'.format(i)])
		iniList.append(['JOINT_{}'.format(i), 'HOME_IGNORE_LIMITS', 'homeIgnoreLimits_{}'.format(i)])
		iniList.append(['JOINT_{}'.format(i), 'HOME_SEQUENCE', 'homeSequence_{}'.format(i)])
		iniList.append(['JOINT_{}'.format(i), 'P', 'p_{}'.format(i)])
		iniList.append(['JOINT_{}'.format(i), 'I', 'i_{}'.format(i)])
		iniList.append(['JOINT_{}'.format(i), 'D', 'd_{}'.format(i)])
		iniList.append(['JOINT_{}'.format(i), 'FF0', 'ff0_{}'.format(i)])
		iniList.append(['JOINT_{}'.format(i), 'FF1', 'ff1_{}'.format(i)])
		iniList.append(['JOINT_{}'.format(i), 'FF2', 'ff2_{}'.format(i)])
		iniList.append(['JOINT_{}'.format(i), 'DEADBAND', 'deadband_{}'.format(i)])
		iniList.append(['JOINT_{}'.format(i), 'BIAS', 'bias_{}'.format(i)])
		iniList.append(['JOINT_{}'.format(i), 'MAX_OUTPUT', 'maxOutput_{}'.format(i)])
		iniList.append(['JOINT_{}'.format(i), 'MAX_ERROR', 'maxError_{}'.format(i)])

	iniList.append(['SPINDLE', 'SPINDLE_TYPE', 'spindleTypeCB'])
	iniList.append(['SPINDLE', 'SCALE', 'spindleScale'])
	iniList.append(['SPINDLE', 'PWM_FREQUENCY', 'pwmFrequencySB'])
	iniList.append(['SPINDLE', 'MAX_RPM', 'spindleMaxRpm'])
	iniList.append(['SPINDLE', 'MIN_RPM', 'spindleMinRpm'])
	iniList.append(['SPINDLE', 'DEADBAND', 'deadband_s'])
	iniList.append(['SPINDLE', 'P', 'p_s'])
	iniList.append(['SPINDLE', 'I', 'i_s'])
	iniList.append(['SPINDLE', 'D', 'd_s'])
	iniList.append(['SPINDLE', 'FF0', 'ff0_s'])
	iniList.append(['SPINDLE', 'FF1', 'ff1_s'])
	iniList.append(['SPINDLE', 'FF2', 'ff2_s'])
	iniList.append(['SPINDLE', 'BIAS', 'bias_s'])
	iniList.append(['SPINDLE', 'MAX_ERROR', 'maxError_s'])

	iniList.append(['INPUTS', 'INPUT_0', 'input_0'])
	iniList.append(['INPUTS', 'INPUT_1', 'input_1'])
	iniList.append(['INPUTS', 'INPUT_2', 'input_2'])
	iniList.append(['INPUTS', 'INPUT_3', 'input_3'])
	iniList.append(['INPUTS', 'INPUT_4', 'input_4'])
	iniList.append(['INPUTS', 'INPUT_5', 'input_5'])
	iniList.append(['INPUTS', 'INPUT_6', 'input_6'])
	iniList.append(['INPUTS', 'INPUT_7', 'input_7'])
	iniList.append(['INPUTS', 'INPUT_8', 'input_8'])
	iniList.append(['INPUTS', 'INPUT_9', 'input_9'])
	iniList.append(['INPUTS', 'INPUT_10', 'input_10'])

	iniList.append(['INPUTS', 'INPUT_JOINT_0', 'inputJoint_0'])
	iniList.append(['INPUTS', 'INPUT_JOINT_1', 'inputJoint_1'])
	iniList.append(['INPUTS', 'INPUT_JOINT_2', 'inputJoint_2'])
	iniList.append(['INPUTS', 'INPUT_JOINT_3', 'inputJoint_3'])
	iniList.append(['INPUTS', 'INPUT_JOINT_4', 'inputJoint_4'])
	iniList.append(['INPUTS', 'INPUT_JOINT_5', 'inputJoint_5'])
	iniList.append(['INPUTS', 'INPUT_JOINT_6', 'inputJoint_6'])
	iniList.append(['INPUTS', 'INPUT_JOINT_7', 'inputJoint_7'])
	iniList.append(['INPUTS', 'INPUT_JOINT_8', 'inputJoint_8'])
	iniList.append(['INPUTS', 'INPUT_JOINT_9', 'inputJoint_9'])
	iniList.append(['INPUTS', 'INPUT_JOINT_10', 'inputJoint_10'])

	iniList.append(['OUTPUTS', 'OUTPUT_0', 'output_0'])
	iniList.append(['OUTPUTS', 'OUTPUT_1', 'output_1'])
	iniList.append(['OUTPUTS', 'OUTPUT_2', 'output_2'])
	iniList.append(['OUTPUTS', 'OUTPUT_3', 'output_3'])
	iniList.append(['OUTPUTS', 'OUTPUT_4', 'output_4'])

	iniList.append(['OPTIONS', 'MANUAL_TOOL_CHANGE', 'manualToolChangeCB'])
	iniList.append(['OPTIONS', 'HALUI', 'haluiCB'])
	iniList.append(['OPTIONS', 'PYVCP', 'pyvcpCB'])
	iniList.append(['OPTIONS', 'GLADEVCP', 'gladevcpCB'])
	iniList.append(['OPTIONS', 'LADDER', 'ladderGB'])
	iniList.append(['OPTIONS', 'LADDER_RUNGS', 'ladderRungsSB'])

	return iniList

#iniList.append(['', '', ''])
