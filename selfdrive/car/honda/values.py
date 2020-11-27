from cereal import car
from selfdrive.car import dbc_dict

VisualAlert = car.CarControl.HUDControl.VisualAlert

# Car button codes
class CruiseButtons:
  RES_ACCEL   = 4
  DECEL_SET   = 3
  CANCEL      = 2
  MAIN        = 1

class AH:
  #[alert_idx, value]
  # See dbc files for info on values"
  NONE           = [0, 0]
  FCW            = [1, 1]
  STEER          = [2, 1]
  BRAKE_PRESSED  = [3, 10]
  GEAR_NOT_D     = [4, 6]
  SEATBELT       = [5, 5]
  SPEED_TOO_HIGH = [6, 8]

VISUAL_HUD = {
  VisualAlert.none: AH.NONE,
  VisualAlert.fcw: AH.FCW,
  VisualAlert.steerRequired: AH.STEER,
  VisualAlert.brakePressed: AH.BRAKE_PRESSED,
  VisualAlert.wrongGear: AH.GEAR_NOT_D,
  VisualAlert.seatbeltUnbuckled: AH.SEATBELT,
  VisualAlert.speedTooHigh: AH.SPEED_TOO_HIGH}

class ECU:
  CAM = 0

class CAR:
  ACCORD = "HONDA ACCORD 2018 SPORT 2T"
  CIVIC = "HONDA CIVIC 2016 TOURING"
  P_207 = "Peugeot 207"
  P_308_2018 = "Peugeot 308 SW 2018"
  Captur_2018 = "Renault Captur 2018"
  VROUM = "Renault"
  ESSAI = "HONDA ESSAI"

FINGERPRINTS = {
  CAR.ACCORD: [{
    148: 8, 228: 5, 304: 8, 330: 8, 344: 8, 380: 8, 399: 7, 419: 8, 420: 8, 427: 3, 432: 7, 441: 5, 446: 3, 450: 8, 464: 8, 477: 8, 479: 8, 495: 8, 545: 6, 662: 4, 773: 7, 777: 8, 780: 8, 804: 8, 806: 8, 808: 8, 829: 5, 862: 8, 884: 8, 891: 8, 927: 8, 929: 8, 1302: 8, 1600: 5, 1601: 8, 1652: 8
  }],
  CAR.CIVIC: [{
    57: 3, 148: 8, 228: 5, 304: 8, 330: 8, 344: 8, 380: 8, 399: 7, 401: 8, 420: 8, 427: 3, 428: 8, 432: 7, 450: 8, 464: 8, 470: 2, 476: 7, 487: 4, 490: 8, 493: 5, 506: 8, 512: 6, 513: 6, 545: 6, 597: 8, 662: 4, 773: 7, 777: 8, 780: 8, 795: 8, 800: 8, 804: 8, 806: 8, 808: 8, 829: 5, 862: 8, 884: 8, 891: 8, 892: 8, 927: 8, 929: 8, 985: 3, 1024: 5, 1027: 5, 1029: 8, 1036: 8, 1039: 8, 1108: 8, 1302: 8, 1322: 5, 1361: 5, 1365: 5, 1424: 5, 1633: 8,
  }],
  CAR.P_308_2018: [{
    114: 5, 168: 5, 228: 5, 264: 8, 269: 8, 274: 8, 277: 8, 488: 8, 512: 6, 513: 6, 520: 8, 552: 8, 649: 8, 743: 1, 749: 7, 757: 7, 773: 7, 781: 8, 813: 8, 840: 8, 845: 8, 909: 8, 968: 2, 973: 8, 1010: 8, 1037: 8, 1042: 8, 1069: 4, 1074: 8, 1080: 8, 1101: 8, 1106: 6, 1128: 8, 1134: 2, 1160: 8, 1166: 4, 1170: 6, 1173: 4, 1202: 8, 1230: 8, 1234: 3, 1266: 8, 1293: 8, 1294: 8, 1326: 8, 1330: 5, 1358: 8, 1362: 8, 1390: 6, 1394: 8, 1400: 4, 1416: 8, 1422: 8, 1426: 8, 1432: 4, 1448: 7, 1454: 5, 1458: 8, 1464: 8, 1486: 3, 1490: 3, 1496: 6, 1517: 3, 1518: 4, 1528: 5, 1554: 8, 1928: 8, 1933: 8, 1938: 8, 1941: 6, 1960: 4
  },
  {
    114: 5, 168: 5, 264: 8, 269: 8, 274: 8, 277: 8, 488: 8, 512: 6, 513: 6, 520: 8, 552: 8, 649: 8, 743: 1, 749: 7, 757: 7, 773: 7, 781: 8, 813: 8, 840: 8, 845: 8, 909: 8, 968: 2, 973: 8, 1010: 8, 1037: 8, 1042: 8, 1069: 4, 1074: 8, 1080: 8, 1101: 8, 1106: 6, 1128: 8, 1134: 2, 1160: 8, 1166: 4, 1170: 6, 1173: 4, 1202: 8, 1230: 8, 1234: 3, 1266: 8, 1293: 8, 1294: 8, 1326: 8, 1330: 5, 1358: 8, 1362: 8, 1390: 6, 1394: 8, 1400: 4, 1416: 8, 1422: 8, 1426: 8, 1432: 4, 1448: 7, 1454: 5, 1458: 8, 1464: 8, 1486: 3, 1490: 3, 1496: 6, 1517: 3, 1518: 4, 1528: 5, 1554: 8, 1928: 8, 1933: 8, 1938: 8, 1941: 6, 1960: 4
  },
  {
    114: 5, 168: 5, 264: 8, 269: 8, 274: 8, 277: 8, 488: 8, 513: 6, 520: 8, 552: 8, 649: 8, 743: 1, 749: 7, 757: 7, 773: 7, 781: 8, 813: 8, 840: 8, 845: 8, 909: 8, 968: 2, 973: 8, 1010: 8, 1037: 8, 1042: 8, 1069: 4, 1074: 8, 1080: 8, 1101: 8, 1106: 6, 1128: 8, 1134: 2, 1160: 8, 1166: 4, 1170: 6, 1173: 4, 1202: 8, 1230: 8, 1234: 3, 1266: 8, 1293: 8, 1294: 8, 1326: 8, 1330: 5, 1358: 8, 1362: 8, 1390: 6, 1394: 8, 1400: 4, 1416: 8, 1422: 8, 1426: 8, 1432: 4, 1448: 7, 1454: 5, 1458: 8, 1464: 8, 1486: 3, 1490: 3, 1496: 6, 1517: 3, 1518: 4, 1528: 5, 1554: 8, 1928: 8, 1933: 8, 1938: 8, 1941: 6, 1960: 4
  },
  {
    114: 5, 488: 8, 513: 6, 520: 8, 552: 8, 649: 8, 743: 1, 749: 7, 757: 7, 773: 7, 781: 8, 813: 8, 840: 8, 845: 8, 909: 8, 968: 2, 973: 8, 1010: 8, 1037: 8, 1042: 8, 1069: 4, 1074: 8, 1080: 8, 1101: 8, 1106: 6, 1128: 8, 1134: 2, 1160: 8, 1166: 4, 1170: 6, 1173: 4, 1202: 8, 1230: 8, 1234: 3, 1266: 8, 1293: 8, 1294: 8, 1326: 8, 1330: 5, 1358: 8, 1362: 8, 1390: 6, 1394: 8, 1400: 4, 1416: 8, 1422: 8, 1426: 8, 1432: 4, 1448: 7, 1454: 5, 1458: 8, 1464: 8, 1486: 3, 1490: 3, 1496: 6, 1517: 3, 1518: 4, 1528: 5, 1554: 8, 1928: 8, 1933: 8, 1938: 8, 1941: 6, 1960: 4
  },
  # Autre essai (69 ids) tel que mesure
  {
    114: 5, 168: 5, 264: 8, 269: 8, 274: 8, 277: 8, 488: 8, 513: 6, 520: 8, 552: 8, 649: 8, 743: 1, 749: 7, 757: 7, 773: 7, 781: 8, 813: 8, 840: 8, 845: 8, 909: 8, 968: 2, 973: 8, 1010: 8, 1037: 8, 1042: 8, 1069: 4, 1074: 8, 1080: 8, 1101: 8, 1106: 6, 1128: 8, 1134: 2, 1160: 8, 1166: 4, 1170: 6, 1173: 4, 1202: 8, 1230: 8, 1234: 3, 1266: 8, 1293: 8, 1294: 8, 1326: 8, 1330: 5, 1358: 8, 1362: 8, 1390: 6, 1394: 8, 1400: 4, 1416: 8, 1422: 8, 1426: 8, 1432: 4, 1448: 7, 1454: 5, 1458: 8, 1464: 8, 1486: 3, 1490: 3, 1496: 6, 1517: 3, 1518: 4, 1528: 5, 1554: 8, 1928: 8, 1933: 8, 1938: 8, 1941: 6, 1960: 4
  }],
  # Renault Clio IV
  CAR.VROUM: [{
    144: 5, 198: 8, 302: 8, 390: 7, 394: 6, 413: 8, 416: 1, 432: 4, 502: 8, 516: 3, 529: 8, 532: 2, 535: 8, 536: 1, 578: 8, 666: 8, 668: 8, 679: 8, 681: 1, 695: 5, 700: 8, 710: 6, 771: 7, 848: 8, 850: 4, 852: 8, 855: 5, 878: 4, 914: 5, 951: 8, 1018: 2, 1050: 4, 1053: 4, 1075: 8, 1076: 2, 1116: 6, 1188: 8, 1196: 5, 1246: 3, 1272: 8, 1274: 2, 1280: 5, 1285: 4, 1297: 7, 1362: 2, 1373: 8, 1379: 2, 1380: 2, 1397: 2, 1409: 4, 1486: 3, 1495: 7, 1498: 8, 1502: 8, 1503: 3, 1513: 8, 1580: 1, 1606: 8, 1608: 8, 1619: 4, 1623: 2, 1628: 3, 1637: 8, 1638: 4, 1640: 2, 1642: 8, 1649: 2, 1675: 6, 1689: 8, 1695: 4, 1787: 8
  },
  {
    144: 5, 198: 8, 228: 5, 302: 8, 390: 7, 394: 6, 413: 8, 416: 1, 432: 4, 502: 8, 512: 6, 513: 6, 516: 3, 529: 8, 532: 2, 535: 8, 536: 1, 578: 8, 649: 8, 666: 8, 668: 8, 679: 8, 681: 1, 695: 5, 700: 8, 710: 6, 771: 7, 848: 8, 850: 4, 852: 8, 855: 5, 878: 4, 914: 5, 951: 8, 1018: 2, 1050: 4, 1053: 4, 1075: 8, 1076: 2, 1116: 6, 1188: 8, 1196: 5, 1246: 3, 1272: 8, 1274: 2, 1280: 5, 1285: 4, 1297: 7, 1362: 2, 1373: 8, 1379: 2, 1380: 2, 1397: 2, 1409: 4, 1486: 3, 1495: 7, 1498: 8, 1502: 8, 1503: 3, 1513: 8, 1580: 1, 1606: 8, 1608: 8, 1619: 4, 1623: 2, 1628: 3, 1637: 8, 1638: 4, 1640: 2, 1642: 8, 1649: 2, 1675: 6, 1689: 8, 1695: 4, 1787: 8
  }],
  CAR.ESSAI: [{
    666: 8, 668: 8, 679: 8, 513: 6, 228: 5, 198: 8, 649: 8, 390: 7
  }],
}

DBC = {
  CAR.ACCORD: dbc_dict('honda_accord_s2t_2018_can_generated', None),
  CAR.CIVIC: dbc_dict('honda_civic_touring_2016_can_generated', 'acura_ilx_2016_nidec'),
  CAR.P_308_2018: dbc_dict('honda_P308_2018_can_generated', None),
  CAR.VROUM: dbc_dict('VROUM_can_generated', None),
  CAR.ESSAI: dbc_dict('honda_Clio_IV_2018_can_generated', None),
}

STEER_THRESHOLD = {
  CAR.ACCORD: 1200,
  CAR.CIVIC: 1200,
  CAR.P_308_2018: 1200,  # potentiellement a modifier pour essayer d'aller au dessus
  CAR.VROUM: 1200,
  CAR.ESSAI: 1200,
}

SPEED_FACTOR = {
  CAR.ACCORD: 1.,
  CAR.CIVIC: 1.,
  CAR.P_308_2018: 1.,  # potentiellement a modifier pour essayer d'aller au dessus
  CAR.VROUM: 1.,
  CAR.ESSAI: 1.,
}

# msgs sent for steering controller by camera module on can 0.
# those messages are mutually exclusive on CRV and non-CRV cars
ECU_FINGERPRINT = {
  ECU.CAM: [0xE4, 0x194],   # steer torque cmd
}

HONDA_BOSCH = [CAR.ACCORD]
