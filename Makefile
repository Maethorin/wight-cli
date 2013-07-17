test:
	@sleep 3
	@rm -rf ~/.wighttest
	@rm -rf .coverage
	@coverage2 run --branch `which nosetests` -vv --with-yanc -s tests/unit/

focus: mongo_test redis
	@sleep 1
	@rm -rf ~/.wighttest
	@WIGHT_USERDATA_PATH=~/.wighttest nosetests -a 'focus' -vv --with-yanc -s tests/unit/

acceptance acc a: mongo_test redis kill_app
	@sleep 3
	@rm -rf ~/.wightacc
	@python wight/api/server.py --port 2368 --bind 0.0.0.0 --conf ./tests/acceptance/acceptance.conf &
	@WIGHT_USERDATA_PATH=~/.wightacc nosetests -vv --with-yanc -s tests/acceptance/ --stop

setup:
	@pip install -e .\[tests\]

local-login:
	@wight target-set http://0.0.0.0:2367
	@wight login

local-team:
	@wight team-create local
	@wight project-create --team local --project wight --repo https://github.com/heynemann/wight.git

local-schedule:
	@wight schedule --team local --project wight --url http://wight.timeho.me/