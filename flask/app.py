from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('/home.html')

@app.route('/india')
def lda_india():
    return render_template('/lda-india.html')

@app.route('/australia')
def lda_australia():
    return render_template('/lda-australia.html')

@app.route('/uk')
def lda_uk():
    return render_template('/lda-uk.html')

@app.route('/usa')
def lda_usa():
    return render_template('/lda-usa.html')

if __name__ == '__main__':
    app.run()
