from app import app, db

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Crea la base de datos y las tablas si no existen
    app.run(debug=True, use_reloader=False)
