# Singapore_Addresses
A database of Singapore Addresses queried from OneMap

## This project is created to help others gain access to all SG postal codes and addresses for personal use

**Instructions -> Go to New_output.xlsx and click the three dots to download**
**OneMap.py -> To query from the REST API**
**Postal_cleaning.py -> Adding sector, regions and district**
**Postal_load.py -> Combine multiple files if you need to batch run**

### This repository is maintained by @Zarilex09 and last updated on 22/8/23 
**Latest API docs -> https://www.onemap.gov.sg/apidocs/**
### The database contains 122,259 addresses with postal codes, sector, region and district based on general acceptance of boundaries.

Column names & Description include:
***SEARCHVAL***: The search parameter/name
***BLK_NO***: Block number
***ROAD_NAME***: Road name
***BUILDING***: Building
***ADDRESS***: Full address with postal code
***POSTAL***: 6 digit Postal code
***X***: X coordinates
***Y***: Y coordinates
***LATITUDE***: latitude
***LONGITUDE***: longitude
***LONGTITUDE***: longitude
***SECTOR***: 2 digit sector code
***REGION***: Region Name
***DISTRICT***: District number
