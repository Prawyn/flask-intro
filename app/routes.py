from flask import Flask, render_template, request, flash
from formes import ContactForm

app = Flask(__name__)
app.secret_key = 'MY OWN KEY'

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if request.method == 'POST':
        if not form.validate():
            flash('All fields are required!')
            return render_template('contact.html', form=form)
        else:
            return 'the form posted...'
            
    elif request.method == 'GET':
        return render_template('contact.html', form=form)    

if __name__ == "__main__":
    app.run(debug=True)
