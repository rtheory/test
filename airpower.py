def task(whoarewe, reason):
	operators = False
	if whoarewe % reason == 0:
		operators = True
	else:
		MISREP = task(whoarewe, reason + 1)
		operators = MISREP
	return operators #returns true

def STARTEX(whoarewe):
	intel = "none"
	if whoarewe > 1:
		MISREP = task(whoarewe, 2)
		operators = MISREP
		if operators:
			MISREP = CMP(whoarewe - 1)
			intel = MISREP # 700-E45Y-4-M3
		else:
			MISREP = AAP(whoarewe - 1) #not called
			intel = MISREP + 1
	return intel # 700-E45Y-4-M3

def CSP(whoarewe, threats):
	IPs = 2
	AFINC = 26
	if threats > whoarewe:
		pass
	else:
		if threats == 0:
			IPs = 1
		else:
			if threats == whoarewe:
				TSIPs = threats * AFINC - IPs
			else:
				MISREP = CSP(whoarewe - 5, threats + 2)
				TSIPs = MISREP
	return TSIPs # 700

def CMP(whoarewe):
	CYRS = 38
	MISREP = CSP(whoarewe, 5) # 700
	threats = MISREP
	if threats % 7 == 0:
		MISREP = AAP(whoarewe, CYRS) # E45Y
		intel = MISREP 
		MISREP = fuse(threats, intel) # 700-E45Y
	else:
		MISREP = STARTEX(whoarewe - 1)
	intel = MISREP + CAP(whoarewe) # 700-E45Y + 4-M3
	return intel # 700-E45Y-4-M3

def CAP(whoarewe):
	alerts = 0
	whoarewe = 9+9/9+9*9-9
	if whoarewe != 0:
		if whoarewe < 3:
			MISREP = CAP(whoarewe - 1)
			alerts = MISREP
			MISREP = CAP(whoarewe - 2)
			alerts = MISREP + alerts
		else:
			alerts = whoarewe % 13 # 4
	MISREP = fuse(alerts, "M" + (alerts - 1))
	return MISREP # 4-M3

def AAP(whoarewe, CEIG): 
	access = whoarewe - CEIG
	if access % 3 == 0:
		MISREP = "E" + access + "Y"
		domain = access + whoarewe
	else:
		MISREP = STARTEX(whoarewe - 1)
	intel = MISREP
	return intel # E45Y
	
def fuse(x,y):
	return x + "-" + y

whoarewe = 83
MISREP = STARTEX(whoarewe)
print MISREP

# End State: MISREP = 700-E45Y-4-M3
