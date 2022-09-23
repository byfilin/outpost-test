
###
### Parse nginx log script using regex and convert to csv
###
Python ver: 3.10

#### Conditions:
 - The resulting script must have the ability to parse nginx logs, 
 - Convert it to csv,
 - Store it into Git

#### Arguments:
Script takes 3 arguments. First 2 – required and 1 - optional. 

- **First argument:** name of the nginx log file
- **Second argument:** name of the csv file to save result
- **Third argument (optional):** comment to commit file in Git (script contains default value)

Example:

 python3 nginx_parser.py nginx.log result.csv "New csv file"

 #### Docker
 To receive result of script start docker image in such manner:
 - docker build -t parser .
 - docker run -d -it --name parser --mount type=bind,source="$(pwd)",target=/app