#!/bin/bash
if [ "$1" == "run" ]; then
    echo "Starting app"
    python manage.py runserver
elif [ "$1" == "run_worker" ]; then
    # start redis server in background
	redis-server & 
	python worker.py
elif [ "$1" == "test" ]; then
	python manage.py test videopath/apps/**/tests/**/*.py
elif [ "$1" == "deploy" ]; then
	#capture db state
	heroku pgbackups:capture --expire --app videopath-api
	# deploy
	git push heroku master
	# run migrations
	heroku run python manage.py migrate --app videopath-api
elif [ "$1" == "import_heroku_db" ]; then
	# capture remote db and import to local postgres instance
	 heroku pgbackups:capture --expire --app videopath-api
	 backup_url=$(heroku pgbackups:url --app videopath-api)
	 curl -o latest.dump $backup_url
	 pg_restore --verbose --clean --no-acl --no-owner -h localhost -U David -d videopath_import latest.dump
	 rm latest.dump
elif [ "$1" == "heroku_login" ]; then
	#capture db state
	spawn heroku login 
	expect "*?mail:*"
	send -- "dscharf@gmx.net\r"
	expect "*?assword:*"
	send -- "password"
elif [ "$1" == "reset_local_db" ]; then
    rm test.db
	python manage.py syncdb --noinput
	python manage.py migrate
	python manage.py createsuperuser
	python manage.py check_permissions
else 
	echo "Command not found"
fi
