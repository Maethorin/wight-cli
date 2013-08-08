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

blade-login:
	@wight target-set http://wight.plataformas.corp.globoi.com/
	@wight login

aws-login:
	@wight target-set http://wight.timeho.me/
	@wight login

team:
	@wight team-create local
	@wight project-create wight --team local --repo https://github.com/heynemann/wight.git

default:
	@wight default-set --team local --project wight

schedule:
	@wight schedule --url http://wight.timeho.me/
