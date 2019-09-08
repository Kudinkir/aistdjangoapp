1)mkdir somedir
2)cd somedir
3)git clone https://github.com/Kudinkir/aistdjangoapp.git
4)Create your own virtual env with the command python3 -m venv env
5)Enter command source env/bin/activate
6) cd aistdjangoapp
7) pip install -r requirements.txt
if you will have problems with Pillow(someone like "Cannot use ImageField because Pillow is not installed")
you must run pip install Pillow
8)python3 manage.py runserver
Our app is available on http://127.0.0.1:8000/ 
