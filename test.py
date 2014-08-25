from labac import Configuration, LBAC


def complext_test():
	
	conf = Configuration()
	conf.object_label_hierarchy = [\
						("o1",["o2","o3"]),\
						("o2",["o4"]),\
						("o5",["o4","o6"])\
		
				      ]
	
	conf.user_label_hierarchy = [\
						("u1",["u2"]),\
						("u3",["u1"])\
				    ]

	#conf.policy = [ ("o5","u1") ]
	conf.add_policy("write", [ ("o5","u1") ] )
	conf.add_policy("read",[ ("o1","u3"), ("o5","u3")] )
	
	lbac = LBAC(conf)
	print lbac.acl
	print lbac.request(user="u1",object="o6",action="read")	


def simple_test_case():
	conf = Configuration()

	user_hierarchy = [ ("manager",["employee"]), ("employee",["stuff"]) ]

	object_hierarchy = [ ("secret", ["public"]), ("confidential",["public"]) ]

	conf.object_label_hierarchy = object_hierarchy

	conf.user_label_hierarchy = user_hierarchy

	conf.add_policy("read",[ ("confidential","employee" ) ] )
	# create LaBAC class with this configuration
	lbac = LBAC(conf)
	# now check if 'employee' can read 'confidential'
	print lbac.request(user='employee', object='confidential', action='read')
	

if __name__ == "__main__":
	#complext_test()
	simple_test_case()
