from flask import Flask, render_template, request, redirect, url_for
import pymysql
import json

app = Flask(__name__)

# Database connection configuration
DB_HOST = 'localhost'
DB_USER = 'root'
DB_PASSWORD = 'onepiece'
DB_NAME = 'perpus_nim'

# Create database connection
def get_db_connection():
    return pymysql.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        db=DB_NAME,
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )

# Route for index page
@app.route('/')
def index():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM buku_nim')
    books = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('index_nim.html', books=books)

# Route for displaying add book form
@app.route('/tambah')
def tambah():
    return render_template('tambah_nim.html')

# Route for handling book addition (POST)
@app.route('/add_book', methods=['POST'])
def add_book():
    if request.method == 'POST':
        kode_buku = request.form['kode_buku']
        nama_buku = request.form['nama_buku']
        penerbit = request.form['penerbit']
        pengarang = request.form['pengarang']
        jumlah_buku = request.form['jumlah_buku']
        
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO buku_nim (Kode_Buku, Nama_Buku, Penerbit, Pengarang, Jumlah_Buku)
            VALUES (%s, %s, %s, %s, %s)
        ''', (kode_buku, nama_buku, penerbit, pengarang, jumlah_buku))
        conn.commit()
        cursor.close()
        conn.close()
        return redirect(url_for('index'))

# Route for displaying edit form
@app.route('/edit/<kode_buku>')
def edit(kode_buku):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM buku_nim WHERE Kode_Buku = %s', (kode_buku,))
    book = cursor.fetchone()
    cursor.close()
    conn.close()
    return render_template('edit_nim.html', book=book)

# Route for handling book update (POST)
@app.route('/update_book', methods=['POST'])
def update_book():
    if request.method == 'POST':
        kode_buku = request.form['kode_buku']
        nama_buku = request.form['nama_buku']
        penerbit = request.form['penerbit']
        pengarang = request.form['pengarang']
        jumlah_buku = request.form['jumlah_buku']
        
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE buku_nim 
            SET Nama_Buku = %s, Penerbit = %s, Pengarang = %s, Jumlah_Buku = %s
            WHERE Kode_Buku = %s
        ''', (nama_buku, penerbit, pengarang, jumlah_buku, kode_buku))
        conn.commit()
        cursor.close()
        conn.close()
        return redirect(url_for('index'))

# New route for handling book deletion
@app.route('/delete/<kode_buku>')
def delete_book(kode_buku):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM buku_nim WHERE Kode_Buku = %s', (kode_buku,))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)