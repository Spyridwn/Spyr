import urllib2
import json

stoixia_a=raw_input('dwse ta stoixia ths east: ')
stoixia_d=raw_input('desw ta stoixia ths west: ')
stoixia_v=raw_input('desw ta stoixia tou north: ')
stoixia_n=raw_input('dwse ta stoixia tou south: ')

response=urllib2.urlopen('http://api.geonames.org/citiesJSON?north='+stoixia_a+'&south='+stoixia_d+'&east='+stoixia_v+'&west='+stoixia_n+'&username=stephen007').read()
response=json.loads(response)

max_plith = response['geonames'][0]['population'] 
max_polis = response['geonames'][0]['name'] 
for polis in response['geonames']:
    if (max_polis < polis['population']): 
        max_polis = polis['population'] 
        max_polis = polis

print "to onoma ths polis me tous perisoterous katikous einai "+max_polis
