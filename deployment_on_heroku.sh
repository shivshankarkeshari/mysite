cd ..
cd venv
source bin/activate
cd ..
cd mysite

procfile=Procfile
if test -f "$procfile";
then
  rm Procfile
  touch Procfile
  echo 'web: gunicorn zo007.wsgi --log-file -' > Procfile

else
  touch Procfile
  echo 'web: gunicorn zo007.wsgi --log-file -' > Procfile
fi


req_file=requirements.txt

#exclude = 'pylint', 'pep8'
# pip freeze |
#             Where-Object { $exclude -notcontains $_ } |
#             ForEach-Object { pip install --upgrade $_ }

if test -f "$req_file";
then
  rm requirements.txt
  pip freeze > requirements.txt
else
    pip freeze > requirements.txt
fi


runtime_file=runtime.txt
if test -f "$runtime_file";
then
  rm runtime.txt
  touch runtime.txt
  echo "python-3.7.5" > runtime.txt
else
  touch runtime.txt
  echo "python-3.7.5" > runtime.txt
fi



#git add .
#echo "Commit message"
#read commit_message
#git commit -m commit_message
#git push heroku master

