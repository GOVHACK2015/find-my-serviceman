#!/usr/bin/env python

import sys
import requests
import json

class Person(object):
	"""Basic info on a service person

	name, service_num, rank, rel_units"""
	name = ''
	service_num = ''
	# These next 2 might have to be lists?
	ranks = []
	related_units = []

	def __init__(self, name):
		"""Constructor"""
		self.name = name

	def __str__(self):
		"""Printing"""
		return self.name

def get_all_results(url):
	"""Get all the results from awm api"""
	# This used to find out how many results there were ... Not necessary now
	# r = requests.get(url)
	# temp = r.json()
	# print requests.get(url).json()

	# This can get all the result with temp['found'] ... But that's too slow
	# Just going to run with 20k results for now
	num_results = 100000
	cur_result 	= 0
	# This number could be set better so as to not get too many results always
	# Also, this and num_results needs to be changed to make requests for more?
	amt_results = 1000

	url += '&count=%d&start=%d'

	results = []

	while (cur_result <= num_results):
		# Do request
		r = requests.get(url % (amt_results, cur_result))
		temp = r.json()

		# Append all results to the results list
		for result in temp['results']:
			results.append(result)

			cur_result += amt_results
			print cur_result
	
	return results

def get_all_people(url):
	"""Returns a list of Person objects

	At the moment this only creates a new person with a name and nothing else"""
	results = get_all_results(url)

	people = []
	names = []

	for result in results:
		if result['preferred_name'] not in names:
			names.append(result['preferred_name'])

	# This isn't correct, this will probably insert too many people into the people list
	for name in names:
		#print name
		#person = get_all_person_info(name)
		#print person.ranks
		#print "\n\n"

		#people.append(person)

		fp = open("test.txt",'w')

		for a in results:
			#print type(a)
			#exit(1)
			#fp.write(str(a))

			print json.dumps(a, sort_keys=True,indent=4, separators=(',', ': '))
			exit(1)

def search_by_year():
	"""You know"""

def get_all_person_info(name):
	"""Find all people records for a person (name + service no.)

	This needs to happen because there can be multiple People records for each person"""
	person = Person(name)

	url = 'https://www.awm.gov.au/direct/data.php?key=ww1hack2015&q=%s AND record_type:"people"' % name
	results = get_all_results(url)

	units = []
	ranks = []

	for result in results:
		temp_units = get_person_related_units(result)

		if temp_units != None:
			for unit in temp_units:
				if unit not in units:
					units.append(unit)

		temp_ranks = get_person_ranks(result)

		if temp_ranks != None:
			for rank in temp_ranks:
				if rank not in ranks:
					ranks.append(rank)

	person.related_units = units
	person.ranks = ranks

	return person

def get_person_related_units(result):
	"""This will return a list of related units for a single People record"""

	if 'related_units_id' in result.keys():
		return result['related_units_id']
	else:
		return []

def get_preson_ranks(result):
	"""Returns a list? of ranks for a single People record"""

	if 'rank' in result.keys():
		return result['rank']
	else:
		return []


def get_people_by_unit(unit_code):
        """Returns a list of people records who servered in <unit_code>"""

	url = 'https://www.awm.gov.au/direct/data.php?key=ww1hack2015&q:related_units_id=%s' % unit_code
	r = requests.get(url)
	temp_json = r.json()
	
	return temp_json['results']

def get_roles_in_unit(unit_code):
        """Returns a list of all ranks reprsented in that unit"""

	people_set=get_people_by_unit(unit_code)
	role_set = set()

	for person in people_set:
		try:
			role_set.add(person['base_rank'])
		except KeyError:
			print "missing key"
	
	return list(role_set)

def get_people_by_unit_role(unit_code, role):
	"""Returns a list of people of rank <role> and in unit <unit_code>"""

	people_set=get_people_by_unit(unit_code)
		
	results = []
	for person in people_set:
		try:
			if person['base_rank'] in role:
				results.append(person)
		except KeyError:
			print "Missing key"
	return results

def pretty_print(obj):
        """helper function to cleanly print json to screen."""
	print json.dumps(obj, sort_keys=True, indent=4, separators=(',', ': '))


def search(name, rank = None, year =None):
        #TODO allow for more open search
        url='https://www.awm.gov.au/direct/data.php?key=ww1hack2015&q={0} AND record_type:people'.format(name)
        
        if rank is not None:
            url=url+' AND base_rank:{}'.format(rank)


        print url
	r = requests.get(url)
	temp_json = r.json()
	
	return temp_json['results']


def prepare_json_stack():
    
    #TODO fix root
    evil_hardcoded_name="William Edward James Smith"
    evil_hardcode_unitcode="U20795"



    role_list = []
    for role in get_roles_in_unit(evil_hardcode_unitcode):
        people_list=[]
        for person in get_people_by_unit_role(evil_hardcode_unitcode, role):
            people_list.append(dict(name=get_persons_name(person)))

        role_list.append(dict(name=role, children = people_list))
    
    list_of_units=[] 
    list_of_units.append(dict(name=evil_hardcode_unitcode, children=role_list))
    root = dict(name=evil_hardcoded_name, children=list_of_units)

    return root
    
    
def get_persons_name(obj):
    try:
        return obj['preferred_name']
    except KeyError:
        return "NA"


#a =  get_roles_in_unit("U51462")
#for b in a:	
#	print b

#a =  get_people_by_unit_role("U51462", "Donkeyman")
#for b in a:	
#	print b


    
a =  search("William Cockshutt")
for b in a:	
	print b



#a = prepare_json_stack()

#pretty_print(a)
