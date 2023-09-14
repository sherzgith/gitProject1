import yaml
# Please have your username and password in yaml file
config_file = "../../data/config.yaml"
with open(config_file, 'r') as file:
    credentials = yaml.safe_load(file)

print(credentials)
uname = credentials['testSIT']['username']
pword = credentials['testSIT']['password']
url = credentials['testSIT']['host']

print('***********Test Case started***********')
print(f" Open the website : {url}")
print(f" Enter the username : {uname}")
print(f" Enter the password : {pword}")
print('Click on login button')
print('...........')
print('Main page opened!!!!!!!!!!')



# print(credentials['username'])
# print(credentials['password'])
# print(credentials['host'])
