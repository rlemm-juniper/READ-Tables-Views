import yaml
from jnpr.junos.factory import loadyaml
from jnpr.junos import Device
from jnpr.junos.op.routes import RouteTable

dev = Device('192.168.0.1')
dev.open()

mytable = loadyaml('MyRouteTable.yaml')
route_table = mytable['MyRouteTable'](dev)
route_table.get()
formatter = "{0:<24}{1:<20}{2:<20}{3:<20}{4:<10}"

for r in route_table:
  if route_table.keys():
    if r.protocol == 'OSPF':
      routes = formatter.format(r.name, r.to, r.via, r.protocol, r.age)
      print routes

dev.close()
