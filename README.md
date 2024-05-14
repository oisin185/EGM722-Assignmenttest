# EGM722-Assignmenttest
The main dependencies for this script are as follows: 
-	Python (Version 3.11.9)
-	OS
-	Geopandas
-	Matplotlib – pyplot, patches, lines
-	Cartopy – crs, ShapelyFeature


Overview of the Datasets:
Datasets are included in the repository.
- Dataset:		/ 				Data Type:			/		Source:
- Belfast_DEA	/ 				Shapefile Vector 	/		Ordnance Survey Northern Ireland (OSNI)
- BelfastBusstops_V2	/		Shapefile Vector	/		ArcGIS Hub (Private Member)
- Belfast_Roads			/		Shapefile Vector	/		Northern Ireland Statistics and Research Agency (NISRA)
- Belfast_RailPlatforms	/		Shapefile Vector	/		Data.gov.uk (Accurate as of 2017)


Setup: Anaconda.
This project was created utilising a GitHub Repository and an Anaconda environment.
Once the repository is cloned and forked and pulled to your computer, an Anaconda environment which will replicate the environment during the creation of the program can be created.
Navigate to where the ‘environment.yml’ file is stored to import the file, subsequently, name the new environment appropriately and click ‘Import’.


Setup: Pycharm.
During the creation, PyCharm Community (version 2022.3.2) was used and all coding revolves around its abilities as an IDE. 
Therefore, setting up the correct environment within PyCharm is necessary. 
Once PyCharm is loaded, click into ‘Edit Configurations’, then ‘Add New Configuration’, then ‘Python’. This will allow for the naming and identifying of the script and the path to the environment file.
Next click ‘Browse’ next to the ‘Script Path’ section and navigate to where the ‘EGM722-Assignmenttest’ cloned repository rests on your computer. 
Under ‘Environment’ in the ‘Configuration’ section click the dropdown menu under ‘Python Interpreter’ and locate the environment which was set up when it was created in Anaconda.
This tells PyCharm where which environment to use to run the program.Ensure that the interpreter being used is the one just created.
Ensure all dependencies are enabled when creating the environment.
Finally click ‘Okay’ and run the script by clicking the green play button named ‘Run’. This should produce a Matplotlib document which can be saved.
