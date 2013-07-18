test:
	@rm -rf ~/.wighttest
	@rm -rf .coverage
	@coverage2 run --branch `which nosetests` -vv --with-yanc -s tests/unit/

focus:
	@rm -rf ~/.wighttest
	@WIGHT_USERDATA_PATH=~/.wighttest nosetests -a 'focus' -vv --with-yanc -s tests/unit/

acc:
	@rm -rf ~/.wightacc
	@WIGHT_USERDATA_PATH=~/.wightacc nosetests -vv --with-yanc -s tests/acceptance/ --stop

setup:
	@pip install -e .\[tests\]

pip:
	@python setup.py -q sdist upload

local-login:
	@wight target-set http://0.0.0.0:2367
	@wight login

local-team:
	@wight team-create local
	@wight project-create --team local --project wight --repo https://github.com/heynemann/wight.git

local-schedule:
	@wight schedule --team local --project wight --url http://wight.timeho.me/
