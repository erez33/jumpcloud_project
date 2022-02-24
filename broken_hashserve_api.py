import requests as r
from requests import exceptions

import random

base_url = 'http://127.0.0.1:8088/'


class BrokenHashServeEndpoints:
    # todo improve error handling messages
    def post_hash_endpoint(self, password):
        try:
            response = r.post(base_url+'hash', data=password)
            return response.status_code, response.text
        except ConnectionError as ce:
            print('error with hash endpoint')

    def get_base64_password(self, job_identifier):
        #todo implement counter to test against 5 second wait
        try:
            response = r.get(base_url+'hash/'+str(job_identifier))
            return response.status_code, response.text
        except ConnectionError as ce:
            print('error with am i working')

    def get_stats(self):
        try:
            response = r.get(base_url+'stats')
            return response.status_code, response.json()
        except ConnectionError as ce:
            print('stats error out')

    def shutdown(self):
        try:
            response = r.post(base_url+'hash/', data='shutdown')
            return response.status_code
        except ConnectionError as ce:
            print('shutdown failed')




# Testing this class with code below
bhs = BrokenHashServeEndpoints()
# print(bhs.post_hash_endpoint('{"password":"\angrymonkey\"}'))
print(bhs.get_base64_password("ghjb"))
# print(bhs.get_stats())
# print(bhs.shutdown())

