 
def test_LaBAC():
	
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
	
	lbac = LaBAC(conf)
	print lbac.acl
	print lbac.request(user="u1",object="o6",action="read")
	


def test_setup():
	setup = Setup()
	setup.object_hierarchy = Configuration._dummy_object_label()
	setup.user_hierarchy = Configuration._dummy_user_label()
	setup.policy = Configuration._dummy_policy()
	print setup.acl

def test_setup2():
	
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
		

	setup = Setup(conf)

	print setup.acl
	
	

def test_configuration():
	print "{} \n {} \n {} \n".format ( \
			Configuration._dummy_policy(), \
			Configuration._dummy_user_label(),\
			Configuration._dummy_object_label()     )



#status = working			
def test_user_label_hierarchy():
	ulh = LabelHierarchy(user=True)
	ulh.add_x_dominates_y(x="u1",y="u2")
	ulh.add_x_dominates_y(x="u2",y="u3")
	ulh.get_hierarchy()

#status= working
def test_object_hierarchy():
	olh = LabelHierarchy()
	olh.add_x_dominates_y(x="o1",y="o2")
	olh.add_x_dominates_y(x="o2",y="o3")
	olh.get_hierarchy()

#status = working
def test_object_label():
	ol = ObjectLabel("o3")
	ol.is_senior_to = "o2"
	ol.is_senior_to = "o1"
	print ol.is_senior_to
	ol.cleared_user_label="u1"
	print ol.cleared_user_label
	print ol.acl

def test_label():
	l = Label('o1')
	l.is_senior_to = 'u1'
	l.is_senior_to = 'u2'
	print l.is_senior_to

def test():
	test_object_label()


if __name__ == "__main__":
	test_LaBAC()
