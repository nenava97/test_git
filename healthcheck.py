import json

#storing dictionary of systems health status into variable
var = """ { "Status": "Healthy", "Checks": [ { "Name": "Connections", "Status": "Healthy" }, { "Name": "ConnectionRead", "Status": "unHealthy" }, { "Name": "redis", "Status": "Healthy" }, { "Name": "ProcessCheck", "Status": "Healthy" }, { "Name": "UserProfile", "Status": "unHealthy" }, { "Name": "features", "Status": "uHealthy", "Description": "sample sample sample" }, { "Name": "shutdown", "Status": "Healthy" }, { "Name": "lifespan", "Status": "unHealthy" } ] }

"""

#create class that will parse through json and do a health check of systems in var
class JsonParser:
  def __init__(self, data):
    self.data = data
    self.dict_data = json.loads(self.data)

  def check_health(self):
    checks = self.dict_data["Checks"]
    print(checks)

    healthy = 0
    unhealthy = 0

    for i in checks:
      if i["Status"] == "Healthy":
        healthy += 1
      else:
        unhealthy += 1
    print(f"Healthy: {healthy}, Unhealthy: {unhealthy}")

  def print_names(self):
    checks = self.dict_data["Checks"]

    healthy_names = []
    unhealthy_names = []

    for i in checks:
      if i["Status"] == "Healthy":
        healthy_names.append(i["Name"])
      else:
        unhealthy_names.append(i["Name"])
    print(f"Healthy Names: {healthy_names}, Unhealthy Names: {unhealthy_names}")

#will print appended list of healthy and unhealthy system names 
object1 = JsonParser(var)
object1.check_health()
object1.print_names()