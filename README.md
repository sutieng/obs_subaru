# obs_superBIT

superBIT-specific configuration and tasks (based on obs_subaru as the backbone) for the LSST Data Management Stack

Version of LSST Science Pipelines: 15.0

how to use this package?
1. In lsst_stack/
	
	source loadLSST.bash

2. Clone a package

	git clone https://github.com/sutieng/obs_superBIT.git
  
	cd obs_superBIT

3. Set up the package

 	setup lsst_obs
  
 	setup -j -r obs_superbit

4. Create a DATA directory

 	mkdir superbit_repo
  
 	echo "lsst.obs.superBIT.SuperBITMapper" >  superbit_repo/_mapper

5. Ingest the raw images into the data repository

 	superbitIngestImages.py superbit_repo/  tests/data/image_ifc_1526928542_72732.fits

6. Ingest Dark/Bias/Flat image into data repository
	
	ingestCalibs.py superbit_repo/ --calib superbit_repo/CALIB 'tests/data/BIAS-2018-05-21.fits' --validity 99
	ingestCalibs.py superbit_repo/ --calib superbit_repo/CALIB 'tests/data/DARK-2018-05-21.fits' --validity 99
	ingestCalibs.py superbit_repo/ --calib superbit_repo/CALIB 'tests/data/FLAT*.fits' --validity 99

7. invoke the analysis program that processes CCD.

	processCcd.py superbit_repo/  --id visit=72737 ccd=1 --output outputrepo --calib superbit_repo/CALIB --clobber-config  --no-versions

