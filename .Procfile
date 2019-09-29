web: gunicorn QA_CommunityForum.wsgi --log-file -

worker: bundle exec rake jobs:work
web: node QA_CommunityForum\admins\frontend\admin_homepage\src\index.js
