# CI_CD_Python
DevOps with Python

conda env create -f DevOps_env.yml
	DevOps_env.yml
		- name: DevOps
		- channels:
		- defaults
		- dependencies:
		-   - pip=18.1
		-   - numpy=1.15.4
		-   - pandas=0.23.4
		-   - jupyter=1.0.0
		
	prefix: C:\Users\Anaconda3\envs\DevOps
	

Pipeline: 

	Installation: 
		○ py -m pip install --upgrade pip
		○ pip install flake8 pytest pytest-cov
		○ pip install spyder-unittest
		○ pip install pip-chill
		○ pip install tox
	
		
	Commandes: 
		○ pytest -v --cov
		○ coverage run -m pytest
		○ flake8 --statistics  (Source --> run code analysis)
		○ pip-chill > requirements.txt
		○ tox -e dev (tox)
	
	Option:
		○ python setup.py sdist
		○ py -m pip install --upgrade build
		○ pip install mock
		○ pip install hypothesis

	tox -e DevOps 