Label Based Access Control (LaBAC)
=====

**What is LaBAC?**

LaBAC is a simplified type of Attribute Based Access Control (ABAC). Where in ABAC there can be many attributes, in LaBAC there is only one attribute associated with object (named object-label) and one attribute associated with User (called user-label). As this access Control is based on label, I call it Label Based Access Control or LaBAC.

**Label Hierarchy**:

*User-Label Hierarchy*: As mention, we attach label on user and object. Label value can have hierarchy. For example, lets assume for a user, user-label is his position (you can say role as used RBAC) in the organization. So, possible uesr-label values are : {manager, employee, stuff}. As you can guess, a user labeled with 'employee' has all the acccess of a user labeled with 'stuff' and a user labeled with 'manager' has all the access for a user labeled with 'employee'. This explains user hierarchy. In this context label 'manager' dominates label 'employee' and 'employee' dominates 'stuff'

*Object-label Hierarchy*: Similarly to the user-label, objects can have label (otherwise said attribute) attached to it. For example, object label can be 'secret', 'confidential' and 'public'. Lets assume both 'secret' & 'condifential' dominate 'public'. What it means anyone who can access object labeled with 'secret' can also access object labeled with 'public'. Also, anyone who can access object labeled with 'confidential' can also access object labeled with 'public'

*Policy*: 
A policy say user with which label can access object with which label. One example, 
('employee', read, 'confidential') means that users with label  employee can read object with label confidential.

**How to use this package?**
In order to use labac, we need a configuration object, that capture user-label hierarchy, object-label hierarchy and policy. This configuration object is then Feed into the 'LBAC' object. 



using previous example, 

our user_labels are = ['manager', 'employee', 'stuff'] , manager dominate employee, employee dominate stuff. this user label hierarchy is captured as following list :

user_hierarchy = [ ("manager",["employee"], ("employee",["stuff"]) ]



