web: gunicorn QA_CommunityForum.wsgi --log-file -
web: java $JAVA_OPTS -jar target/dependency/jetty-runner.jar --port $PORT target/*.war

worker: bundle exec rake jobs:work