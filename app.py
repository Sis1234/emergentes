from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)
app.secret_key = 'tu_clave_secreta'  

users = {
    "evelyn": "contraseña",
}

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        # Validar usuario y contraseña
        if username in users and users[username] == password:
            session['username'] = username 
            return redirect(url_for('welcome')) 
            flash('Nombre de usuario o contraseña incorrectos.')  
            return redirect(url_for('login'))

    return render_template('login.html')


@app.route('/welcome')
def welcome():
    if 'username' in session:
        username = session['username'] 
        return render_template('welcome.html', username=username)
    else:
        return redirect(url_for('login'))  

@app.route('/logout')
def logout():
    session.pop('username', None) 
    flash('Has cerrado sesión correctamente.')
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)