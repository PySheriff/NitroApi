import requests
import json
import os

credentials = json.dumps({
    "login":
        {
            "username": "nsroot",
            "password": "nsroot"
        }
})
''' DO NOT USE WRITE YOUR CREDENTIALS IN CODE in production. Credentials variable holds your login credentials
 to login and obtain a session id aka token from the adc upon successful authentication. I only used this 
 method since it's my lab environment. You will need to write a script that receives a token and write that into an environment
 variable to be used as part of the request headers for subsequent connections'''


class nitro:
    def __init__(self, host):
        self.host = host  # instance variable

    def login(self, cred):
        """Login function"""
        try:
            baseurl = "http://{}/nitro/v1/config/login".format(self.host)
            '''creating the URL to the API endpoint'''
            headers = {'Content-Type': 'application/json'}
            '''headers to append to the request'''
            response = requests.post(baseurl, data=cred, headers=headers)
            '''HTTP POST request'''
            return response.json()
        except Exception as inst:
            print(inst)

    def getvs(self):
        '''function to retrieve all Virtual Servers on the ADC'''
        try:
            baseurl = "http://{}/nitro/v1/stat/lbvserver".format(self.host)
            '''creating the URL to the API endpoint'''
            headers = {'Cookie': 'NITRO_AUTH_TOKEN='}
            '''headers to append to the request'''
            response = requests.get(baseurl, headers=headers)
            '''HTTP GET request'''
            print(response.status_code)
            data = response.json()
            virtual_servers = data['lbvserver']
            print(virtual_servers)
        except Exception as inst:
            print(inst)


ns_session = nitro('192.168.1.30')
print(ns_session.login(credentials))
# ns_session.getvs()
