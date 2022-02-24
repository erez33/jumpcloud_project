# import hashlib
# import base64
#
# password = 'angrymonkey'
# # print(str.encode(password))
# h = hashlib.sha512(b'angrymonkey')
# # h = hashlib.sha512(password.encode('utf-8'))
# print(h.hexdigest())
#
# if h.hexdigest() == '34dd0f00ab6279aca24d8f3f41de7701e3331e46ef6437706188839f0b4376ffc5216bdccb5b0a09beea8bb36ef10f0277f32a8d07b2088d2958a0c6a7be00d6':
#     print(type(h.hexdigest()))
#     print(True)
# else:
#     print(False)
#
#
# b = bytes(h.hexdigest(), 'utf-8')
# e = base64.b64encode(b)
# print(e)
#
# print(base64.decodebytes(e))
# print(len('MzRkZDBmMDBhYjYyNzlhY2EyNGQ4ZjNmNDFkZTc3MDFlMzMzMWU0NmVmNjQzNzcwNjE4ODgzOWYwYjQzNzZmZmM1MjE2YmRjY2I1YjBhMDliZWVhOGJiMzZlZjEwZjAyNzdmMzJhOGQwN2IyMDg4ZDI5NThhMGM2YTdiZTAwZDY='))
# print(len('NN0PAKtieayiTY8/Qd53AeMzHkbvZDdwYYiDnwtDdv/FIWvcy1sKCb7qi7Nu8Q8Cd/MqjQeyCI0pWKDGp74A1g=='))
#
# # a = base64.decodebytes(b'NN0PAKtieayiTY8/Qd53AeMzHkbvZDdwYYiDnwtDdv/FIWvcy1sKCb7qi7Nu8Q8Cd/MqjQeyCI0pWKDGp74A1g==')
#
# print(b)
# print(type(b))
#
# c = h.hexdigest()
#
# encode = base64.b64encode(bytes(c, 'utf-8'))
# # print(base64.decodebytes(encode))
#
# # import requests
# # # this file only contains scratch code
# #
# # # base_endpoint = 'http://127.0.0.1:8088/'
# # #
# # # r = requests.get(base_endpoint+'stats')
# # # print(r.headers)
# # # print(r.json())
# # # print(r.text)
# # # print(r.status_code)
# #
# # shutdown_endpoint = 'http://127.0.0.1:8088/hash'
# # r = requests.post(shutdown_endpoint, data='shutdown')
# # # print(r.headers)
# # # print(r.json())
# # # print(r.text)
# # print(r.status_code)
