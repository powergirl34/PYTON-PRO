# İçeri Aktarma
from flask import Flask, render_template,request, redirect
# Veritabanı kütüphanesini içe aktarma
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime 

app = Flask(__name__)
# SQLite ile bağlantı kurma 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///diary.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# DB oluşturma
db = SQLAlchemy(app )

#Görev #1. DB tablosu oluşturma
class Entry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    subtitle = db.Column(db.String(300), nullable=False)
    text = db.Column(db.Text, nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<Entry {self.id}>'

# İçerik sayfasını çalıştırma
@app.route('/')
def index():
    # DB nesnelerini görüntüleme
    # Görev #2. DB'deki nesneleri index.html'de görüntüleme
    entries = Entry.query.order_by(Entry.date_created.desc()).all()
    return render_template('index.html',
                           entries=entries
         )
    
