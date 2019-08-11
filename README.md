Role Name
=========

Simple role to demonstrate unit testing for 2 scenarios using molecule. This roles creates linux users and then create virtual hosts directories and assigns the ownership to the created directories.
1. Allowed users can read/write in their directory
2. Users cannot write in others directories

This also contains Jenkins pipeline which can be used to create the job. The pipeline is available under `ci/pipeline.gdsl`

The test case python code is available under `molecule/default/tests`

Requirements
------------

Python

molecule

ansible 

docker

Role Variables
--------------

```---
   # vars file for test-suit
   v_hosts:
     - dev1:
         website: mango.com
         port: 8081
     - dev2:
         website: apple.com
         port: 8082
     - dev3:
         website: papaya.com
         port: 8083
     - dev4:
         website: grapes.com
         port: 8084
   
   main_document_root: /var/www/
   html_directory: public_html
   ```

Dependencies
------------

N/A 

Example Playbook
----------------

```bash
molecule destroy
molecule converge
molecule verify

```

License
-------

BSD

Author Information
------------------

Aspiring fisherman