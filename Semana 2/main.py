from sassutils.wsgi import SassMiddleware
import requests
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for
import forms


app = Flask(__name__)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')


@app.route('/', methods=['GET', 'POST'])
def index():
    form = forms.SearchProfileForm(request.form)
    if request.method == 'POST' and form.validate():
        username = form.username.data
        return redirect(url_for('profile', name=username))
    return render_template('base.html', form=form)


@app.route('/user/<name>')
def profile(name):
    form = forms.SearchProfileForm(request.form)
    req = requests.get(f'https://api.github.com/users/{name}')
    profile = req.json()
    if ('message' in profile):
        return redirect(url_for('error404'))
    else:
        date = datetime.strptime(
            profile['created_at'], "%Y-%m-%dT%H:%M:%SZ").date().strftime("%d/%m/%y")
        return render_template('profile.html', profile=profile, date=date, form=form)


@app.route('/error')
def error404():
    form = forms.SearchProfileForm(request.form)
    return render_template('404.html', form=form)


if __name__ == '__main__':
    app.run()
