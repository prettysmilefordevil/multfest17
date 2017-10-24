Для обновления приложения:
git init
git add .
git commit -m ''
git push -u https://github.com/prettysmilefordevil/multfest17
git push heroku master
heroku ps:scale web=1 (=0 - shutdown app)
heroku open
heroku logs --tail

print('<a href="{0}">{0}</a>'.format(link))