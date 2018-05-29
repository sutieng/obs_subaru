import re
import datetime
from lsst.pipe.tasks.ingest import IngestTask, ParseTask, IngestArgumentParser
from lsst.pipe.tasks.ingestCalibs import CalibsParseTask

class SuperBITIngestArgumentParser(IngestArgumentParser):
    
    def _parseDirectories(self, namespace):
        namespace.input = namespace.rawInput ###the path of input data
        namespace.output = namespace.rawOutput
        namespace.calib = None
        del namespace.rawInput
        del namespace.rawCalib
        del namespace.rawOutput
        del namespace.rawRerun


class SuperBITIngestTask(IngestTask):
    ArgumentParser = SuperBITIngestArgumentParser

def datetime2mjd(date_time):
    
    YY = date_time.year
    MO = date_time.month
    DD = date_time.day
    HH = date_time.hour
    MI = date_time.minute
    SS = date_time.second
    
    if MO == 1 or MO == 2:
        mm = MO + 12
        yy = YY - 1
    else:
        mm = MO
        yy = YY
    
    dd = DD + (HH/24.0 + MI/24.0/60.0 + SS/24.0/3600.0)

    A = int(365.25*yy)
    B = int(yy/400.0)
    C = int(yy/100.0)
    D = int(30.59*(mm-2))
    
    mjd = A + B - C + D + dd - 678912
    
    return mjd

class SuperBITParseTask(ParseTask):
    DAY0 =0  # Zero point for  the date

    def translate_field(self, md):
        field = md.get("OBJECT").strip()
        if field == "#":
            field = "UNKNOWN"
        # replacing inappropriate characters for file path and upper()
        field = re.sub(r'\W', '_', field).upper()
#return field
        field="TEST"
        return field

    def translate_visit(self, md):
        expId = md.get("FRAMEID")
        #m = re.search("(\d{6})", expId)  ###EXP-ID: 6numbers, can be changed, depend on how they set
        return expId

    def getTjd(self, md):
        """Return truncated (modified) Julian Date"""
        return int(md.get('MJD')) - self.DAY0


    def translate_pointing(self, md):
        """This value was originally called 'pointing', and intended to be used
        to identify a logical group of exposures.  It has evolved to simply be
        a form of truncated Modified Julian Date, and is called 'visitID' in
        some versions of the code.  However, we retain the name 'pointing' for
        backward compatibility.  ##images have the same visitID are observed on the same date
        """
        try:
            return self.getTjd(md)
        except:
            pass
    
        try:
            dateobs = md.get("DATE_OBS")
            m = re.search(r'(\d{4})-(\d{2})-(\d{2})', dateobs)
            year, month, day = m.groups()
            obsday = datetime.datetime(int(year), int(month), int(day), 0, 0, 0)
            mjd = datetime2mjd(obsday)
            return int(mjd) - self.DAY0
        except:
            pass

        self.log.warn("Unable to determine suitable 'pointing' value; using 0")
        return 0

    def translate_ccd(self,md):
        ccd=1 ##superbit only have one ccd
        return ccd

    def translate_filter(self, md):
        """Want upper-case filter names"""
        try:
            #return "WHEELPOS"+str(md.get('WHEELPOS'))
            return md.get('FILTER').strip().upper()
        except:
            return "Unrecognized"


class SuperBITCalibsParseTask(CalibsParseTask):

    def _translateFromCalibId(self, field, md):
        '''reading Calib information from md.CALIB_ID, so in the header of CALIB:
CALIB_ID= 'filter=NONE calibDate=2013-11-03 ccd=0'''
        data = md.get("CALIB_ID")
        match = re.search(".*%s=(\S+)" % field, data)
        return match.groups()[0]
            
    def translate_ccd(self, md):
        #return int(self._translateFromCalibId("ccd", md))
        ccd=1
        #print("!!!using lsst/obs/subperbit/ingestsuperbit")
        return ccd
    
    def translate_filter(self, md):
    #return self._translateFromCalibId("filter", md)
        #return "WHEELPOS"+str(md.get('WHEELPOS'))
        return md.get('FILTER').strip().upper()

    def translate_calibDate(self, md):
        return md.get("DATE_OBS")
    

###data structure: "OBJECT"->"DATE-OBS"->translate_pointing("DATE-OBS")->"FILTER01"->HSC-"FRAMEID"-"ccd".fits


