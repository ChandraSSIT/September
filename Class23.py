# API
# Method => Get,Post,Put,Patch,Delete
# URL => Uniform resource locator ( location/address/endpoint of api)
# Response => data return from api

# CRUD =>
# Create => Post
# Read => Get
# Update => Put
# Delete => Delete

# Get => Reading existing data
# Header => token information, application type =>
# URL
# Response => It contains status code
# based on status code we will go for further steps to validate
# Status codes => 100 series to 500 series
# 200 series  => Success responses , 200,201,202,204
# 200 => ok
# 201 => Created
# 202 =>Accepted
# 204 => No content
# 400 series => Client error
# 400 => Bad Request
# 401 => Unauthorised
# 402 =>Payment required
# 403 => Forbidden
# 404 => Not found
# 405 => Method not allowed
# 500 series => Server error


import requests


response = requests.get("https://reqres.in/api/users?page=1")
print(response)
print(response.status_code)
print(response.json())
print(response.headers)

