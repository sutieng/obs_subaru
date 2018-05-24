from lsst.obs.superBIT.ingestsuperbit import SuperBITParseTask
config.parse.retarget(SuperBITParseTask)

config.parse.translation = {#'proposal': 'PROP-ID',
                            'dataType': 'DATA-TYPE',
                            'expTime': 'EXPTIME',
                            #'pa': 'INST-PA',
                            #'autoguider': 'T_AG',
                            #'ccdTemp': 'T_CCDTV',
                            #'config': 'T_CFGFIL',
                            'frameId': 'FRAMEID',
                            #'expId': 'EXP-ID',
                            'dateObs': 'DATE_OBS',
                            'taiObs': 'DATE_OBS',
                            }
config.parse.defaults = {'ccdTemp': "0", # Added in commissioning run 3
                         }
config.parse.translators = {'field': 'translate_field',
                            'visit': 'translate_visit',
                            'pointing': 'translate_pointing',
                            'filter': 'translate_filter',
                            'ccd': 'translate_ccd',
                            }

config.register.columns = {'field': 'text',
                           'visit': 'int',
                           'ccd': 'int',
                           'pointing': 'int',
                           'filter': 'text',
                           #'proposal': 'text',
                           'dateObs': 'text',
                           'taiObs': 'text',
                           'expTime': 'double',
                           #'pa': 'double',
                           #'autoguider': 'int',
                           #'ccdTemp': 'double',
                           #'config': 'text',
                           'frameId': 'text',
                           #'expId': 'text',
                           'dataType': 'text',
                           }
config.register.unique = ['visit', 'ccd', ]
config.register.visit = ['visit', 'field', 'filter', 'dateObs', 'taiObs']
