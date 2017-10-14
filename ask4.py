import urllib2
import json

prwth_polh =raw_input('Grapse prwth polh: ')
deuterh_polh =raw_input('Grapse deuterh polh: ')

prwth_polh_dedomena =urllib2.urlopen('https://api.teleport.org/api/urban_areas/slug:' + prwth_polh + '/scores/').read()
deuterh_polh_dedomena =urllib2.urlopen('https://api.teleport.org/api/urban_areas/slug:' + deuterh_polh  + '/scores/').read()


prwth_polh_dedomena =json.loads(prwth_polh_dedomena)
deuterh_polh_dedomena =json.loads(deuterh_polh_dedomena)

if (prwth_polh_dedomena['teleport_city_score'] == deuterh_polh_dedomena['teleport_city_score']):
	print "Kai oi 2 poleis exoun to idio score"

if (prwth_polh_dedomena['teleport_city_score'] > deuterh_polh_dedomena['teleport_city_score']):
	print "H polh " + prwth_polh + " exei megalitero score"

if (prwth_polh_dedomena['teleport_city_score'] < deuterh_polh_dedomena['teleport_city_score']):
	print "H polh " + deuterh_polh  + " exei megalitero score"
