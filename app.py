# # # # # from flask import Flask, request, jsonify, render_template
# # # # # from model import load_model, predict_image

# # # # # app = Flask(__name__)

# # # # # # Load model at startup
# # # # # model = load_model()

# # # # # @app.route('/')
# # # # # def home():
# # # # #     return "Crowd Estimation Flask Backend is Running!"

# # # # # @app.route('/predict', methods=['POST'])
# # # # # def predict():
# # # # #     if 'file' not in request.files:
# # # # #         return jsonify({"error": "No file uploaded"}), 400
# # # # #     file = request.files['file']
# # # # #     prediction = predict_image(model, file)
# # # # #     return jsonify({"count": int(prediction)})

# # # # # @app.route('/ui')
# # # # # def ui():
# # # # #     return render_template('index.html')

# # # # # if __name__ == '__main__':
# # # # #     app.run(debug=True)

# # # # # from flask import Flask, request, jsonify, render_template
# # # # # from model import load_model, predict_image
# # # # # import sqlite3, os, uuid

# # # # # app = Flask(__name__)
# # # # # DB_PATH = "database.db"

# # # # # # Load model
# # # # # model = load_model()

# # # # # # Create database if not exists
# # # # # def init_db():
# # # # #     conn = sqlite3.connect(DB_PATH)
# # # # #     c = conn.cursor()
# # # # #     c.execute("""CREATE TABLE IF NOT EXISTS predictions (
# # # # #                     id TEXT PRIMARY KEY,
# # # # #                     filename TEXT,
# # # # #                     count REAL
# # # # #                 )""")
# # # # #     conn.commit()
# # # # #     conn.close()

# # # # # init_db()

# # # # # @app.route('/')
# # # # # def home():
# # # # #     return "Crowd Estimation Flask Backend is Running!"

# # # # # @app.route('/predict', methods=['POST'])
# # # # # def predict():
# # # # #     if 'file' not in request.files:
# # # # #         return jsonify({"error": "No file uploaded"}), 400
    
# # # # #     file = request.files['file']
# # # # #     filename = str(uuid.uuid4()) + "_" + file.filename
# # # # #     filepath = os.path.join("static", filename)
# # # # #     file.save(filepath)

# # # # #     count, density_path = predict_image(model, file)

# # # # #     # Store in DB
# # # # #     conn = sqlite3.connect(DB_PATH)
# # # # #     c = conn.cursor()
# # # # #     c.execute("INSERT INTO predictions VALUES (?, ?, ?)", (filename, filename, count))
# # # # #     conn.commit()
# # # # #     conn.close()

# # # # #     return render_template("index.html",
# # # # #                            crowd_count=int(count),
# # # # #                            input_image=filepath,
# # # # #                            density_image=density_path)

# # # # # @app.route('/ui')
# # # # # def ui():
# # # # #     return render_template('index.html')

# # # # # @app.route('/history')
# # # # # def history():
# # # # #     conn = sqlite3.connect(DB_PATH)
# # # # #     c = conn.cursor()
# # # # #     c.execute("SELECT * FROM predictions")
# # # # #     rows = c.fetchall()
# # # # #     conn.close()
# # # # #     return jsonify(rows)

# # # # # if __name__ == '__main__':
# # # # #     app.run(debug=True)
# # # # import os
# # # # import uuid
# # # # from flask import Flask, request, render_template, url_for
# # # # from werkzeug.utils import secure_filename
# # # # from model_utils import load_model, predict_image

# # # # app = Flask(__name__)

# # # # # Ensure static exists (absolute path)
# # # # STATIC_DIR = os.path.join(app.root_path, "static")
# # # # os.makedirs(STATIC_DIR, exist_ok=True)

# # # # # Load model once
# # # # model = load_model()

# # # # @app.route('/predict', methods=['POST'])
# # # # def predict():
# # # #     if 'file' not in request.files:
# # # #         return "No file uploaded", 400

# # # #     file = request.files['file']
# # # #     if file.filename == '':
# # # #         return "No file selected", 400

# # # #     # sanitize and create unique filename
# # # #     safe_name = secure_filename(file.filename)
# # # #     unique_name = f"{uuid.uuid4().hex}_{safe_name}"
# # # #     abs_path = os.path.join(STATIC_DIR, unique_name)

# # # #     # Save uploaded file to absolute static path
# # # #     try:
# # # #         file.save(abs_path)
# # # #     except Exception as e:
# # # #         return f"Failed to save file: {e}", 500

# # # #     # Predict - predict_image expects a file path string and returns (count, density_filename)
# # # #     count, density_fname = predict_image(model, abs_path)

# # # #     # Build URLs for template
# # # #     input_url = url_for('static', filename=unique_name)
# # # #     density_url = url_for('static', filename=density_fname)

# # # #     return render_template('index.html',
# # # #                            crowd_count=int(count),
# # # #                            input_image=input_url,
# # # #                            density_image=density_url)

# # # # from flask import Flask, request, jsonify, render_template
# # # # from model_utils import load_model, predict_image
# # # # import sqlite3, os, uuid

# # # # app = Flask(__name__)
# # # # DB_PATH = "database.db"

# # # # # Load model at startup
# # # # model = load_model()

# # # # # Create database if not exists
# # # # def init_db():
# # # #     conn = sqlite3.connect(DB_PATH)
# # # #     c = conn.cursor()
# # # #     c.execute("""CREATE TABLE IF NOT EXISTS predictions (
# # # #                     id TEXT PRIMARY KEY,
# # # #                     filename TEXT,
# # # #                     count REAL
# # # #                 )""")
# # # #     conn.commit()
# # # #     conn.close()

# # # # init_db()

# # # # @app.route('/')
# # # # def home():
# # # #     return "Crowd Estimation Flask Backend is Running!"

# # # # @app.route('/predict', methods=['POST'])
# # # # def predict():
# # # #     if 'file' not in request.files:
# # # #         return jsonify({"error": "No file uploaded"}), 400
    
# # # #     file = request.files['file']
# # # #     unique_id = str(uuid.uuid4())
# # # #     filename = unique_id + "_" + file.filename
# # # #     filepath = os.path.join("static", filename)
# # # #     file.save(filepath)

# # # #     # Run prediction
# # # #     count, density_path = predict_image(model, filepath)

# # # #     # Store result in DB
# # # #     conn = sqlite3.connect(DB_PATH)
# # # #     c = conn.cursor()
# # # #     c.execute("INSERT INTO predictions VALUES (?, ?, ?)", (unique_id, filename, count))
# # # #     conn.commit()
# # # #     conn.close()

# # # #     return render_template("index.html",
# # # #                            crowd_count=int(count),
# # # #                            input_image=filepath,
# # # #                            density_image=density_path)

# # # # @app.route('/ui')
# # # # def ui():
# # # #     return render_template('index.html')

# # # # @app.route('/history')
# # # # def history():
# # # #     conn = sqlite3.connect(DB_PATH)
# # # #     c = conn.cursor()
# # # #     c.execute("SELECT * FROM predictions")
# # # #     rows = c.fetchall()
# # # #     conn.close()
# # # #     return jsonify(rows)

# # # # if __name__ == '__main__':
# # # #     app.run(debug=True)


# # # # @app.route('/history')
# # # # def history():
# # # #     conn = sqlite3.connect(DB_PATH)
# # # #     c = conn.cursor()
# # # #     c.execute("SELECT * FROM predictions")
# # # #     rows = c.fetchall()
# # # #     conn.close()
# # # #     return render_template("history.html", rows=rows)


# # # # import os
# # # # os.makedirs("static", exist_ok=True)   # makes sure static/ exists

# # # # # Ensure static folder exists
# # # # os.makedirs("static", exist_ok=True)

# # # # app = Flask(__name__)

# # # # @app.route('/predict', methods=['POST'])
# # # # def predict():
# # # #     if 'file' not in request.files:
# # # #         return jsonify({"error": "No file uploaded"}), 400

# # # #     file = request.files['file']
# # # #     filename = str(uuid.uuid4()) + "_" + file.filename

# # # #     # 🔹 Ensure correct static path
# # # #     static_dir = os.path.join(app.root_path, "static")
# # # #     os.makedirs(static_dir, exist_ok=True)

# # # #     filepath = os.path.join(static_dir, filename)
# # # #     file.save(filepath)   # ✅ Now Flask saves correctly

# # # #     count, density_path = predict_image(model, filepath)

# # # #     return render_template(
# # # #         "index.html",
# # # #         crowd_count=int(count),
# # # #         input_image="static/" + filename,   # for frontend display
# # # #         density_image=density_path
# # # #     )

# # # # import os

# # # # # Ensure 'static' folder exists
# # # # if not os.path.exists("static"):
# # # #     os.makedirs("static")
# # # # @app.route('/predict', methods=['POST'])
# # # # def predict():
# # # #     if 'file' not in request.files:
# # # #         return "No file uploaded", 400

# # # #     file = request.files['file']
# # # #     if file.filename == '':
# # # #         return "No selected file", 400

# # # #     # Save file into static/
# # # #     filename = str(uuid.uuid4()) + "_" + file.filename
# # # #     filepath = os.path.join("static", filename)
# # # #     file.save(filepath)

# # # #     # Run model prediction
# # # #     count, density_map_path = predict_image(filepath)

# # # #     return render_template("result.html", count=count, 
# # # #                            image_path=filepath, density_path=density_map_path)


# # # # density_url = url_for('static', filename=density_fname)
# # # # import sqlite3
# # # # from datetime import datetime

# # # # # Example when saving prediction
# # # # conn = sqlite3.connect('history.db')
# # # # c = conn.cursor()

# # # # # Ensure table has timestamp column
# # # # c.execute('''
# # # #     CREATE TABLE IF NOT EXISTS history (
# # # #         id INTEGER PRIMARY KEY AUTOINCREMENT,
# # # #         image_path TEXT,
# # # #         crowd_count INTEGER,
# # # #         predicted_at TEXT
# # # #     )
# # # # ''')

# # # # # Insert record with readable timestamp
# # # # c.execute('INSERT INTO history (image_path, crowd_count, predicted_at) VALUES (?, ?, ?)',
# # # #           (saved_path, int(predicted_count), datetime.now().strftime("%d-%m-%Y %H:%M:%S")))

# # # # conn.commit()
# # # # conn.close()

# # # # import os
# # # # import uuid
# # # # import sqlite3
# # # # from datetime import datetime
# # # # from flask import Flask, request, render_template, jsonify, url_for
# # # # from werkzeug.utils import secure_filename
# # # # from model_utils import load_model, predict_image  # adjust if your file is named differently

# # # # app = Flask(__name__)

# # # # # Paths
# # # # DB_PATH = "history.db"
# # # # STATIC_DIR = os.path.join(app.root_path, "static")
# # # # os.makedirs(STATIC_DIR, exist_ok=True)

# # # # # Load model once
# # # # model = load_model()

# # # # # -------------------------------
# # # # # Initialize DB
# # # # # -------------------------------
# # # # def init_db():
# # # #     conn = sqlite3.connect(DB_PATH)
# # # #     c = conn.cursor()
# # # #     c.execute('''
# # # #         CREATE TABLE IF NOT EXISTS history (
# # # #             id INTEGER PRIMARY KEY AUTOINCREMENT,
# # # #             image_path TEXT,
# # # #             crowd_count INTEGER,
# # # #             predicted_at TEXT
# # # #         )
# # # #     ''')
# # # #     conn.commit()
# # # #     conn.close()

# # # # init_db()

# # # # # -------------------------------
# # # # # Routes
# # # # # -------------------------------
# # # # @app.route('/')
# # # # def home():
# # # #     return "Crowd Estimation Flask Backend is Running!"

# # # # @app.route('/ui')
# # # # def ui():
# # # #     return render_template('index.html')

# # # # @app.route('/predict', methods=['POST'])
# # # # def predict():
# # # #     if 'file' not in request.files:
# # # #         return "No file uploaded", 400

# # # #     file = request.files['file']
# # # #     if file.filename == '':
# # # #         return "No file selected", 400

# # # #     # Unique safe filename
# # # #     safe_name = secure_filename(file.filename)
# # # #     unique_name = f"{uuid.uuid4().hex}_{safe_name}"
# # # #     abs_path = os.path.join(STATIC_DIR, unique_name)
# # # #     file.save(abs_path)

# # # #     # Run prediction
# # # #     count, density_fname = predict_image(model, abs_path)

# # # #     # Save to DB with readable timestamp
# # # #     conn = sqlite3.connect(DB_PATH)
# # # #     c = conn.cursor()
# # # #     c.execute(
# # # #         "INSERT INTO history (image_path, crowd_count, predicted_at) VALUES (?, ?, ?)",
# # # #         (unique_name, int(count), datetime.now().strftime("%d-%m-%Y %H:%M:%S"))
# # # #     )
# # # #     conn.commit()
# # # #     conn.close()

# # # #     # URLs for frontend
# # # #     input_url = url_for('static', filename=unique_name)
# # # #     density_url = url_for('static', filename=density_fname)

# # # #     return render_template(
# # # #         "index.html",
# # # #         crowd_count=int(count),
# # # #         input_image=input_url,
# # # #         density_image=density_url
# # # #     )

# # # # @app.route('/history')
# # # # def history():
# # # #     conn = sqlite3.connect(DB_PATH)
# # # #     c = conn.cursor()
# # # #     c.execute("SELECT * FROM history ORDER BY id DESC")
# # # #     rows = c.fetchall()
# # # #     conn.close()
# # # #     return render_template("history.html", rows=rows)

# # # # # -------------------------------
# # # # # Run
# # # # # -------------------------------
# # # # if __name__ == '__main__':
# # # #     app.run(debug=True)

# # # # from flask import Flask, send_from_directory

# # # # app = Flask(__name__)

# # # # @app.route('/favicon.ico')
# # # # def favicon():
# # # #     return send_from_directory(
# # # #         app.static_folder, 'favicon.ico', mimetype='image/vnd.microsoft.icon'
# # # #     )

# # # # from flask import Flask, render_template, request, redirect, url_for, session

# # # # app = Flask(__name__)
# # # # app.secret_key = "my_secret_key"  # Required for session handling

# # # # # Temporary user storage
# # # # users = {}

# # # # @app.route('/')
# # # # def home():
# # # #     if "user" in session:
# # # #         return render_template("index.html")   # Your existing website
# # # #     return redirect(url_for("login"))

# # # # @app.route('/login', methods=["GET", "POST"])
# # # # def login():
# # # #     if request.method == "POST":
# # # #         email = request.form["email"]
# # # #         password = request.form["password"]

# # # #         if email in users and users[email] == password:
# # # #             session["user"] = email
# # # #             return redirect(url_for("home"))
# # # #         return "Invalid credentials! Try again."
# # # #     return render_template("login.html")

# # # # @app.route('/signup', methods=["GET", "POST"])
# # # # def signup():
# # # #     if request.method == "POST":
# # # #         email = request.form["email"]
# # # #         password = request.form["password"]

# # # #         users[email] = password
# # # #         return redirect(url_for("login"))
# # # #     return render_template("signup.html")

# # # # @app.route('/logout')
# # # # def logout():
# # # #     session.pop("user", None)
# # # #     return redirect(url_for("login"))

# # # # if __name__ == "__main__":
# # # #     app.run(debug=True)

# # # # import os
# # # # import uuid
# # # # import sqlite3
# # # # from datetime import datetime
# # # # from flask import Flask, request, render_template, jsonify, url_for, redirect, session, send_from_directory
# # # # from werkzeug.utils import secure_filename
# # # # from model_utils import load_model, predict_image  # adjust if your file is named differently

# # # # # -------------------------------
# # # # # App setup
# # # # # -------------------------------
# # # # app = Flask(__name__)
# # # # app.secret_key = "my_secret_key"  # Required for session handling

# # # # DB_PATH = "history.db"
# # # # STATIC_DIR = os.path.join(app.root_path, "static")
# # # # os.makedirs(STATIC_DIR, exist_ok=True)

# # # # # Temporary user storage (replace later with DB if needed)
# # # # users = {}

# # # # # Load model once
# # # # model = load_model()

# # # # # -------------------------------
# # # # # Initialize DB
# # # # # -------------------------------
# # # # def init_db():
# # # #     conn = sqlite3.connect(DB_PATH)
# # # #     c = conn.cursor()
# # # #     c.execute('''
# # # #         CREATE TABLE IF NOT EXISTS history (
# # # #             id INTEGER PRIMARY KEY AUTOINCREMENT,
# # # #             image_path TEXT,
# # # #             crowd_count INTEGER,
# # # #             predicted_at TEXT
# # # #         )
# # # #     ''')
# # # #     conn.commit()
# # # #     conn.close()

# # # # init_db()

# # # # # -------------------------------
# # # # # Auth routes
# # # # # -------------------------------
# # # # @app.route('/')
# # # # def home():
# # # #     if "user" in session:
# # # #         return render_template("index.html")   # show your website
# # # #     return redirect(url_for("login"))

# # # # @app.route('/login', methods=["GET", "POST"])
# # # # def login():
# # # #     if request.method == "POST":
# # # #         email = request.form["email"]
# # # #         password = request.form["password"]

# # # #         if email in users and users[email] == password:
# # # #             session["user"] = email
# # # #             return redirect(url_for("home"))
# # # #         return "Invalid credentials! Try again."
# # # #     return render_template("login.html")

# # # # @app.route('/signup', methods=["GET", "POST"])
# # # # def signup():
# # # #     if request.method == "POST":
# # # #         email = request.form["email"]
# # # #         password = request.form["password"]

# # # #         users[email] = password
# # # #         return redirect(url_for("login"))
# # # #     return render_template("signup.html")

# # # # @app.route('/logout')
# # # # def logout():
# # # #     session.pop("user", None)
# # # #     return redirect(url_for("login"))

# # # # # -------------------------------
# # # # # Prediction routes
# # # # # -------------------------------
# # # # @app.route('/predict', methods=['POST'])
# # # # def predict():
# # # #     if "user" not in session:
# # # #         return redirect(url_for("login"))

# # # #     if 'file' not in request.files:
# # # #         return "No file uploaded", 400

# # # #     file = request.files['file']
# # # #     if file.filename == '':
# # # #         return "No file selected", 400

# # # #     # Unique safe filename
# # # #     safe_name = secure_filename(file.filename)
# # # #     unique_name = f"{uuid.uuid4().hex}_{safe_name}"
# # # #     abs_path = os.path.join(STATIC_DIR, unique_name)
# # # #     file.save(abs_path)

# # # #     # Run prediction
# # # #     count, density_fname = predict_image(model, abs_path)

# # # #     # Save to DB with readable timestamp
# # # #     conn = sqlite3.connect(DB_PATH)
# # # #     c = conn.cursor()
# # # #     c.execute(
# # # #         "INSERT INTO history (image_path, crowd_count, predicted_at) VALUES (?, ?, ?)",
# # # #         (unique_name, int(count), datetime.now().strftime("%d-%m-%Y %H:%M:%S"))
# # # #     )
# # # #     conn.commit()
# # # #     conn.close()

# # # #     # URLs for frontend
# # # #     input_url = url_for('static', filename=unique_name)
# # # #     density_url = url_for('static', filename=density_fname)

# # # #     return render_template(
# # # #         "index.html",
# # # #         crowd_count=int(count),
# # # #         input_image=input_url,
# # # #         density_image=density_url
# # # #     )

# # # # @app.route('/history')
# # # # def history():
# # # #     if "user" not in session:
# # # #         return redirect(url_for("login"))

# # # #     conn = sqlite3.connect(DB_PATH)
# # # #     c = conn.cursor()
# # # #     c.execute("SELECT * FROM history ORDER BY id DESC")
# # # #     rows = c.fetchall()
# # # #     conn.close()
# # # #     return render_template("history.html", rows=rows)

# # # # # -------------------------------
# # # # # Favicon
# # # # # -------------------------------
# # # # @app.route('/favicon.ico')
# # # # def favicon():
# # # #     return send_from_directory(
# # # #         app.static_folder, 'favicon.ico', mimetype='image/vnd.microsoft.icon'
# # # #     )

# # # # # -------------------------------
# # # # # Run
# # # # # -------------------------------
# # # # if __name__ == '__main__':
# # # #     app.run(debug=True)
















# # # # import os
# # # # import uuid
# # # # import sqlite3
# # # # from datetime import datetime
# # # # from flask import Flask, request, render_template, url_for, redirect, session, send_from_directory
# # # # from werkzeug.utils import secure_filename
# # # # from model_utils import load_model, predict_image  # adjust if your file is named differently

# # # # # -------------------------------
# # # # # App setup
# # # # # -------------------------------
# # # # app = Flask(__name__)
# # # # app.secret_key = "my_secret_key"  # Required for session handling

# # # # DB_PATH = "history.db"
# # # # STATIC_DIR = os.path.join(app.root_path, "static")
# # # # os.makedirs(STATIC_DIR, exist_ok=True)

# # # # # Load model once
# # # # model = load_model()

# # # # # -------------------------------
# # # # # Initialize DB
# # # # # -------------------------------
# # # # def init_db():
# # # #     conn = sqlite3.connect(DB_PATH)
# # # #     c = conn.cursor()

# # # #     # History table
# # # #     c.execute('''
# # # #         CREATE TABLE IF NOT EXISTS history (
# # # #             id INTEGER PRIMARY KEY AUTOINCREMENT,
# # # #             image_path TEXT,
# # # #             crowd_count INTEGER,
# # # #             predicted_at TEXT
# # # #         )
# # # #     ''')

# # # #     # Users table
# # # #     c.execute('''
# # # #         CREATE TABLE IF NOT EXISTS users (
# # # #             id INTEGER PRIMARY KEY AUTOINCREMENT,
# # # #             email TEXT UNIQUE,
# # # #             password TEXT
# # # #         )
# # # #     ''')

# # # #     conn.commit()
# # # #     conn.close()

# # # # init_db()

# # # # # -------------------------------
# # # # # Auth routes
# # # # # -------------------------------
# # # # @app.route('/')
# # # # def home():
# # # #     if "user" in session:
# # # #         return render_template("index.html")   # main website
# # # #     return redirect(url_for("login"))

# # # # @app.route('/login', methods=["GET", "POST"])
# # # # def login():
# # # #     if request.method == "POST":
# # # #         email = request.form["email"]
# # # #         password = request.form["password"]

# # # #         conn = sqlite3.connect(DB_PATH)
# # # #         c = conn.cursor()
# # # #         c.execute("SELECT * FROM users WHERE email=? AND password=?", (email, password))
# # # #         user = c.fetchone()
# # # #         conn.close()

# # # #         if user:
# # # #             session["user"] = email
# # # #             return redirect(url_for("home"))
# # # #         return render_template("login.html", error="Invalid email or password!")
    
# # # #     return render_template("login.html")

# # # # @app.route('/signup', methods=["GET", "POST"])
# # # # def signup():
# # # #     if request.method == "POST":
# # # #         email = request.form["email"]
# # # #         password = request.form["password"]

# # # #         try:
# # # #             conn = sqlite3.connect(DB_PATH)
# # # #             c = conn.cursor()
# # # #             c.execute("INSERT INTO users (email, password) VALUES (?, ?)", (email, password))
# # # #             conn.commit()
# # # #             conn.close()
# # # #             return redirect(url_for("login"))
# # # #         except sqlite3.IntegrityError:
# # # #             return render_template("signup.html", error="Email already exists!")

# # # #     return render_template("signup.html")

# # # # @app.route('/logout')
# # # # def logout():
# # # #     session.pop("user", None)
# # # #     return redirect(url_for("login"))

# # # # # -------------------------------
# # # # # Prediction routes
# # # # # -------------------------------
# # # # @app.route('/predict', methods=['POST'])
# # # # def predict():
# # # #     if "user" not in session:
# # # #         return redirect(url_for("login"))

# # # #     if 'file' not in request.files:
# # # #         return "No file uploaded", 400

# # # #     file = request.files['file']
# # # #     if file.filename == '':
# # # #         return "No file selected", 400

# # # #     # Unique safe filename
# # # #     safe_name = secure_filename(file.filename)
# # # #     unique_name = f"{uuid.uuid4().hex}_{safe_name}"
# # # #     abs_path = os.path.join(STATIC_DIR, unique_name)
# # # #     file.save(abs_path)

# # # #     # Run prediction
# # # #     count, density_fname = predict_image(model, abs_path)

# # # #     # Save to DB with readable timestamp
# # # #     conn = sqlite3.connect(DB_PATH)
# # # #     c = conn.cursor()
# # # #     c.execute(
# # # #         "INSERT INTO history (image_path, crowd_count, predicted_at) VALUES (?, ?, ?)",
# # # #         (unique_name, int(count), datetime.now().strftime("%d-%m-%Y %H:%M:%S"))
# # # #     )
# # # #     conn.commit()
# # # #     conn.close()

# # # #     # URLs for frontend
# # # #     input_url = url_for('static', filename=unique_name)
# # # #     density_url = url_for('static', filename=density_fname)

# # # #     return render_template(
# # # #         "index.html",
# # # #         crowd_count=int(count),
# # # #         input_image=input_url,
# # # #         density_image=density_url
# # # #     )

# # # # @app.route('/history')
# # # # def history():
# # # #     if "user" not in session:
# # # #         return redirect(url_for("login"))

# # # #     conn = sqlite3.connect(DB_PATH)
# # # #     c = conn.cursor()
# # # #     c.execute("SELECT * FROM history ORDER BY id DESC")
# # # #     rows = c.fetchall()
# # # #     conn.close()
# # # #     return render_template("history.html", rows=rows)

# # # # # -------------------------------
# # # # # Favicon
# # # # # -------------------------------
# # # # @app.route('/favicon.ico')
# # # # def favicon():
# # # #     return send_from_directory(
# # # #         app.static_folder, 'favicon.ico', mimetype='image/vnd.microsoft.icon'
# # # #     )

# # # # # -------------------------------
# # # # # Run
# # # # # -------------------------------
# # # # if __name__ == '__main__':
# # # #     app.run(debug=True)




# # # # new code

# # # # import os
# # # # import uuid
# # # # import sqlite3
# # # # from datetime import datetime
# # # # from flask import Flask, request, render_template, url_for, redirect, session, send_from_directory
# # # # from werkzeug.utils import secure_filename
# # # # from model_utils import load_model, predict_image  # Import your updated model_utils

# # # # # -------------------------------
# # # # # App setup
# # # # # -------------------------------
# # # # app = Flask(__name__)
# # # # app.secret_key = "my_secret_key"  # Required for session handling

# # # # DB_PATH = "history.db"
# # # # STATIC_DIR = os.path.join(app.root_path, "static")
# # # # os.makedirs(STATIC_DIR, exist_ok=True)

# # # # # Load the model once
# # # # model = load_model()

# # # # # -------------------------------
# # # # # Initialize DB
# # # # # -------------------------------
# # # # def init_db():
# # # #     conn = sqlite3.connect(DB_PATH)
# # # #     c = conn.cursor()

# # # #     # History table
# # # #     c.execute('''
# # # #         CREATE TABLE IF NOT EXISTS history (
# # # #             id INTEGER PRIMARY KEY AUTOINCREMENT,
# # # #             image_path TEXT,
# # # #             crowd_count INTEGER,
# # # #             predicted_at TEXT
# # # #         )
# # # #     ''')

# # # #     # Users table
# # # #     c.execute('''
# # # #         CREATE TABLE IF NOT EXISTS users (
# # # #             id INTEGER PRIMARY KEY AUTOINCREMENT,
# # # #             email TEXT UNIQUE,
# # # #             password TEXT
# # # #         )
# # # #     ''')

# # # #     conn.commit()
# # # #     conn.close()

# # # # init_db()

# # # # # -------------------------------
# # # # # Auth routes
# # # # # -------------------------------
# # # # @app.route('/')
# # # # def home():
# # # #     if "user" in session:
# # # #         return render_template("index.html")  # main website
# # # #     return redirect(url_for("login"))

# # # # @app.route('/login', methods=["GET", "POST"])
# # # # def login():
# # # #     if request.method == "POST":
# # # #         email = request.form["email"]
# # # #         password = request.form["password"]

# # # #         conn = sqlite3.connect(DB_PATH)
# # # #         c = conn.cursor()
# # # #         c.execute("SELECT * FROM users WHERE email=? AND password=?", (email, password))
# # # #         user = c.fetchone()
# # # #         conn.close()

# # # #         if user:
# # # #             session["user"] = email
# # # #             return redirect(url_for("home"))
# # # #         return render_template("login.html", error="Invalid email or password!")
    
# # # #     return render_template("login.html")

# # # # @app.route('/signup', methods=["GET", "POST"])
# # # # def signup():
# # # #     if request.method == "POST":
# # # #         email = request.form["email"]
# # # #         password = request.form["password"]

# # # #         try:
# # # #             conn = sqlite3.connect(DB_PATH)
# # # #             c = conn.cursor()
# # # #             c.execute("INSERT INTO users (email, password) VALUES (?, ?)", (email, password))
# # # #             conn.commit()
# # # #             conn.close()
# # # #             return redirect(url_for("login"))
# # # #         except sqlite3.IntegrityError:
# # # #             return render_template("signup.html", error="Email already exists!")

# # # #     return render_template("signup.html")

# # # # @app.route('/logout')
# # # # def logout():
# # # #     session.pop("user", None)
# # # #     return redirect(url_for("login"))

# # # # # -------------------------------
# # # # # Prediction routes
# # # # # -------------------------------
# # # # @app.route('/predict', methods=['POST'])
# # # # def predict():
# # # #     if "user" not in session:
# # # #         return redirect(url_for("login"))

# # # #     if 'file' not in request.files:
# # # #         return "No file uploaded", 400

# # # #     file = request.files['file']
# # # #     if file.filename == '':
# # # #         return "No file selected", 400

# # # #     # Unique safe filename
# # # #     safe_name = secure_filename(file.filename)
# # # #     unique_name = f"{uuid.uuid4().hex}_{safe_name}"
# # # #     abs_path = os.path.join(STATIC_DIR, unique_name)
# # # #     file.save(abs_path)

# # # #     # Run prediction
# # # #     count, density_fname = predict_image(model, abs_path)

# # # #     # Save to DB with readable timestamp
# # # #     conn = sqlite3.connect(DB_PATH)
# # # #     c = conn.cursor()
# # # #     c.execute(
# # # #         "INSERT INTO history (image_path, crowd_count, predicted_at) VALUES (?, ?, ?)",
# # # #         (unique_name, count, datetime.now().strftime("%d-%m-%Y %H:%M:%S"))
# # # #     )
# # # #     conn.commit()
# # # #     conn.close()

# # # #     # URLs for frontend
# # # #     input_url = url_for('static', filename=unique_name)
# # # #     density_url = url_for('static', filename=density_fname)

# # # #     return render_template(
# # # #         "index.html",
# # # #         crowd_count=count,
# # # #         input_image=input_url,
# # # #         density_image=density_url
# # # #     )

# # # # @app.route('/history')
# # # # def history():
# # # #     if "user" not in session:
# # # #         return redirect(url_for("login"))

# # # #     conn = sqlite3.connect(DB_PATH)
# # # #     c = conn.cursor()
# # # #     c.execute("SELECT * FROM history ORDER BY id DESC")
# # # #     rows = c.fetchall()
# # # #     conn.close()
# # # #     return render_template("history.html", rows=rows)

# # # # # -------------------------------
# # # # # Favicon
# # # # # -------------------------------
# # # # @app.route('/favicon.ico')
# # # # def favicon():
# # # #     return send_from_directory(
# # # #         app.static_folder, 'favicon.ico', mimetype='image/vnd.microsoft.icon'
# # # #     )

# # # # # -------------------------------
# # # # # Run the Flask app
# # # # # -------------------------------
# # # # if __name__ == '__main__':
# # # #     app.run(debug=True)


# # # import os
# # # import uuid
# # # import sqlite3
# # # from datetime import datetime
# # # from flask import Flask, request, render_template, url_for, redirect, session, send_from_directory
# # # from werkzeug.utils import secure_filename
# # # from model_utils import load_model, predict_image  # Import updated model_utils

# # # # -------------------------------
# # # # App setup
# # # # -------------------------------
# # # app = Flask(__name__)
# # # app.secret_key = "my_secret_key"  # Required for session handling

# # # DB_PATH = "history.db"
# # # STATIC_DIR = os.path.join(app.root_path, "static")
# # # os.makedirs(STATIC_DIR, exist_ok=True)

# # # # Load the model once at app startup
# # # model = load_model()

# # # # -------------------------------
# # # # Initialize DB
# # # # -------------------------------
# # # def init_db():
# # #     conn = sqlite3.connect(DB_PATH)
# # #     c = conn.cursor()

# # #     # History table
# # #     c.execute('''
# # #         CREATE TABLE IF NOT EXISTS history (
# # #             id INTEGER PRIMARY KEY AUTOINCREMENT,
# # #             image_path TEXT,
# # #             crowd_count INTEGER,
# # #             predicted_at TEXT
# # #         )
# # #     ''')

# # #     # Users table
# # #     c.execute('''
# # #         CREATE TABLE IF NOT EXISTS users (
# # #             id INTEGER PRIMARY KEY AUTOINCREMENT,
# # #             email TEXT UNIQUE,
# # #             password TEXT
# # #         )
# # #     ''')

# # #     conn.commit()
# # #     conn.close()

# # # init_db()

# # # # -------------------------------
# # # # Auth routes
# # # # -------------------------------
# # # @app.route('/')
# # # def home():
# # #     if "user" in session:
# # #         return render_template("index.html")  # Main page
# # #     return redirect(url_for("login"))

# # # @app.route('/login', methods=["GET", "POST"])
# # # def login():
# # #     if request.method == "POST":
# # #         email = request.form["email"]
# # #         password = request.form["password"]

# # #         conn = sqlite3.connect(DB_PATH)
# # #         c = conn.cursor()
# # #         c.execute("SELECT * FROM users WHERE email=? AND password=?", (email, password))
# # #         user = c.fetchone()
# # #         conn.close()

# # #         if user:
# # #             session["user"] = email
# # #             return redirect(url_for("home"))
# # #         return render_template("login.html", error="Invalid email or password!")
    
# # #     return render_template("login.html")

# # # @app.route('/signup', methods=["GET", "POST"])
# # # def signup():
# # #     if request.method == "POST":
# # #         email = request.form["email"]
# # #         password = request.form["password"]

# # #         try:
# # #             conn = sqlite3.connect(DB_PATH)
# # #             c = conn.cursor()
# # #             c.execute("INSERT INTO users (email, password) VALUES (?, ?)", (email, password))
# # #             conn.commit()
# # #             conn.close()
# # #             return redirect(url_for("login"))
# # #         except sqlite3.IntegrityError:
# # #             return render_template("signup.html", error="Email already exists!")

# # #     return render_template("signup.html")

# # # @app.route('/logout')
# # # def logout():
# # #     session.pop("user", None)
# # #     return redirect(url_for("login"))


# # from flask import Flask, request, render_template, url_for, redirect, session, send_from_directory
# # import os
# # import uuid
# # import sqlite3
# # from datetime import datetime
# # from werkzeug.utils import secure_filename
# # from model_utils import load_model, predict_image  # Assuming model_utils.py is correct

# # # -------------------------------
# # # App setup
# # # -------------------------------
# # app = Flask(__name__)
# # app.secret_key = "my_secret_key"  # Required for session handling

# # DB_PATH = "history.db"
# # STATIC_DIR = os.path.join(app.root_path, "static")
# # os.makedirs(STATIC_DIR, exist_ok=True)

# # # Load model once when the Flask app starts
# # model = load_model()  # This will load the model globally, so it doesn't reload for each request

# # # -------------------------------
# # # Initialize DB
# # # -------------------------------
# # def init_db():
# #     conn = sqlite3.connect(DB_PATH)
# #     c = conn.cursor()

# #     # History table
# #     c.execute('''
# #         CREATE TABLE IF NOT EXISTS history (
# #             id INTEGER PRIMARY KEY AUTOINCREMENT,
# #             image_path TEXT,
# #             crowd_count INTEGER,
# #             predicted_at TEXT
# #         )
# #     ''')

# #     # Users table
# #     c.execute('''
# #         CREATE TABLE IF NOT EXISTS users (
# #             id INTEGER PRIMARY KEY AUTOINCREMENT,
# #             email TEXT UNIQUE,
# #             password TEXT
# #         )
# #     ''')

# #     conn.commit()
# #     conn.close()

# # init_db()

# # # -------------------------------
# # # Auth routes
# # # -------------------------------
# # @app.route('/')
# # def home():
# #     if "user" in session:
# #         return render_template("index.html")  # Main page
# #     return redirect(url_for("login"))

# # @app.route('/login', methods=["GET", "POST"])
# # def login():
# #     if request.method == "POST":
# #         email = request.form["email"]
# #         password = request.form["password"]

# #         conn = sqlite3.connect(DB_PATH)
# #         c = conn.cursor()
# #         c.execute("SELECT * FROM users WHERE email=? AND password=?", (email, password))
# #         user = c.fetchone()
# #         conn.close()

# #         if user:
# #             session["user"] = email
# #             return redirect(url_for("home"))
# #         return render_template("login.html", error="Invalid email or password!")
    
# #     return render_template("login.html")

# # @app.route('/signup', methods=["GET", "POST"])
# # def signup():
# #     if request.method == "POST":
# #         email = request.form["email"]
# #         password = request.form["password"]

# #         try:
# #             conn = sqlite3.connect(DB_PATH)
# #             c = conn.cursor()
# #             c.execute("INSERT INTO users (email, password) VALUES (?, ?)", (email, password))
# #             conn.commit()
# #             conn.close()
# #             return redirect(url_for("login"))
# #         except sqlite3.IntegrityError:
# #             return render_template("signup.html", error="Email already exists!")

# #     return render_template("signup.html")

# # @app.route('/logout')
# # def logout():
# #     session.pop("user", None)  # Remove the user from the session
# #     return redirect(url_for("login"))  # Redirect to the login page

# # # -------------------------------
# # # Prediction routes
# # # -------------------------------
# # @app.route('/predict', methods=['POST'])
# # def predict():
# #     if "user" not in session:
# #         return redirect(url_for("login"))

# #     if 'file' not in request.files:
# #         return "No file uploaded", 400

# #     file = request.files['file']
# #     if file.filename == '':
# #         return "No file selected", 400

# #     # Unique safe filename
# #     safe_name = secure_filename(file.filename)
# #     unique_name = f"{uuid.uuid4().hex}_{safe_name}"
# #     abs_path = os.path.join(STATIC_DIR, unique_name)
# #     file.save(abs_path)

# #     # Log the image path
# #     print(f"Image saved at: {abs_path}")

# #     # Run prediction
# #     count, density_fname = predict_image(model, abs_path)

# #     # Log the prediction result
# #     print(f"Predicted count: {count}")

# #     # Save to DB with readable timestamp
# #     conn = sqlite3.connect(DB_PATH)
# #     c = conn.cursor()
# #     c.execute(
# #         "INSERT INTO history (image_path, crowd_count, predicted_at) VALUES (?, ?, ?)",
# #         (unique_name, int(count), datetime.now().strftime("%d-%m-%Y %H:%M:%S"))
# #     )
# #     conn.commit()
# #     conn.close()

# #     # URLs for frontend
# #     input_url = url_for('static', filename=unique_name)
# #     density_url = url_for('static', filename=density_fname)

# #     # Log the URLs for debugging
# #     print(f"Input image URL: {input_url}")
# #     print(f"Density map URL: {density_url}")

# #     return render_template(
# #         "index.html",
# #         crowd_count=int(count),
# #         input_image=input_url,
# #         density_image=density_url
# #     )

# # @app.route('/history')
# # def history():
# #     if "user" not in session:
# #         return redirect(url_for("login"))

# #     conn = sqlite3.connect(DB_PATH)
# #     c = conn.cursor()
# #     c.execute("SELECT * FROM history ORDER BY id DESC")
# #     rows = c.fetchall()
# #     conn.close()
# #     return render_template("history.html", rows=rows)

# # # -------------------------------
# # # Favicon
# # # -------------------------------
# # @app.route('/favicon.ico')
# # def favicon():
# #     return send_from_directory(
# #         app.static_folder, 'favicon.ico', mimetype='image/vnd.microsoft.icon'
# #     )

# # # -------------------------------
# # # Run the Flask app
# # # -------------------------------
# # if __name__ == '__main__':
# #     app.run(debug=True)


# @app.route('/predict', methods=['POST'])
# def predict():
#     if "user" not in session:
#         return redirect(url_for("login"))

#     if 'file' not in request.files:
#         return "No file uploaded", 400

#     file = request.files['file']
#     if file.filename == '':
#         return "No file selected", 400

#     # Unique safe filename
#     safe_name = secure_filename(file.filename)
#     unique_name = f"{uuid.uuid4().hex}_{safe_name}"
#     abs_path = os.path.join(STATIC_DIR, unique_name)
#     file.save(abs_path)

#     # Log the image path
#     print(f"Image saved at: {abs_path}")

#     # Run prediction
#     count, density_fname = predict_image(model, abs_path)

#     # Log the prediction result before passing it to the frontend
#     print(f"Predicted crowd count: {count}")

#     # If the model is returning an inaccurate count, you can apply post-processing here
#     # Example: Adjusting the crowd count (debugging step):
#     if count < 5:
#         print(f"Prediction too low, adjusting count to 5")
#         count = 5  # Adjusting count for low predictions as an example

#     # Save to DB with readable timestamp
#     conn = sqlite3.connect(DB_PATH)
#     c = conn.cursor()
#     c.execute(
#         "INSERT INTO history (image_path, crowd_count, predicted_at) VALUES (?, ?, ?)",
#         (unique_name, int(count), datetime.now().strftime("%d-%m-%Y %H:%M:%S"))
#     )
#     conn.commit()
#     conn.close()

#     # URLs for frontend
#     input_url = url_for('static', filename=unique_name)
#     density_url = url_for('static', filename=density_fname)

#     # Log the URLs for debugging
#     print(f"Input image URL: {input_url}")
#     print(f"Density map URL: {density_url}")

#     # Return the updated crowd count
#     return render_template(
#         "index.html",
#         crowd_count=int(count),  # Final count
#         input_image=input_url,
#         density_image=density_url
#     )


# Import necessary libraries
# from flask import Flask, request, render_template, url_for, redirect, session, send_from_directory
# import os
# import uuid
# import sqlite3
# from datetime import datetime
# from werkzeug.utils import secure_filename
# from model_utils import load_model, predict_image  # Import model utility functions

# # Initialize Flask app
# app = Flask(__name__)
# app.secret_key = "my_secret_key"  # Secret key for session management

# DB_PATH = "history.db"  # Path to the database
# STATIC_DIR = os.path.join(app.root_path, "static")  # Directory to store uploaded images and generated maps
# os.makedirs(STATIC_DIR, exist_ok=True)

# # Load the model once when the app starts
# model = load_model()  # Load the model at the start

# # -------------------------------
# # Initialize database
# # -------------------------------
# def init_db():
#     conn = sqlite3.connect(DB_PATH)
#     c = conn.cursor()

#     # History table: stores the image path, crowd count, and timestamp
#     c.execute('''
#         CREATE TABLE IF NOT EXISTS history (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             image_path TEXT,
#             crowd_count INTEGER,
#             predicted_at TEXT
#         )
#     ''')

#     # Users table: stores the user emails and hashed passwords
#     c.execute('''
#         CREATE TABLE IF NOT EXISTS users (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             email TEXT UNIQUE,
#             password TEXT
#         )
#     ''')

#     conn.commit()
#     conn.close()

# init_db()

# # -------------------------------
# # Auth routes (login, signup, logout)
# # -------------------------------
# @app.route('/')
# def home():
#     if "user" in session:
#         return render_template("index.html")  # Main page after login
#     return redirect(url_for("login"))

# @app.route('/login', methods=["GET", "POST"])
# def login():
#     if request.method == "POST":
#         email = request.form["email"]
#         password = request.form["password"]

#         conn = sqlite3.connect(DB_PATH)
#         c = conn.cursor()
#         c.execute("SELECT * FROM users WHERE email=? AND password=?", (email, password))
#         user = c.fetchone()
#         conn.close()

#         if user:
#             session["user"] = email  # Store email in session
#             return redirect(url_for("home"))
#         return render_template("login.html", error="Invalid email or password!")
    
#     return render_template("login.html")

# @app.route('/signup', methods=["GET", "POST"])
# def signup():
#     if request.method == "POST":
#         email = request.form["email"]
#         password = request.form["password"]

#         try:
#             conn = sqlite3.connect(DB_PATH)
#             c = conn.cursor()
#             c.execute("INSERT INTO users (email, password) VALUES (?, ?)", (email, password))
#             conn.commit()
#             conn.close()
#             return redirect(url_for("login"))
#         except sqlite3.IntegrityError:
#             return render_template("signup.html", error="Email already exists!")

#     return render_template("signup.html")

# @app.route('/logout')
# def logout():
#     session.pop("user", None)  # Remove user from session
#     return redirect(url_for("login"))  # Redirect to the login page

# # -------------------------------
# # Prediction route: handles image upload and crowd counting prediction
# # -------------------------------
# @app.route('/predict', methods=['POST'])
# def predict():
#     if "user" not in session:
#         return redirect(url_for("login"))

#     if 'file' not in request.files:
#         return "No file uploaded", 400

#     file = request.files['file']
#     if file.filename == '':
#         return "No file selected", 400

#     # Save the uploaded image with a unique name
#     safe_name = secure_filename(file.filename)
#     unique_name = f"{uuid.uuid4().hex}_{safe_name}"
#     abs_path = os.path.join(STATIC_DIR, unique_name)
#     file.save(abs_path)

#     # Log the image path for debugging
#     print(f"Image saved at: {abs_path}")

#     # Run prediction using the pre-loaded model
#     count, density_fname = predict_image(model, abs_path)

#     # Log the prediction result for debugging
#     print(f"Predicted crowd count: {count}")

#     # Save the prediction result in the database
#     conn = sqlite3.connect(DB_PATH)
#     c = conn.cursor()
#     c.execute(
#         "INSERT INTO history (image_path, crowd_count, predicted_at) VALUES (?, ?, ?)",
#         (unique_name, int(count), datetime.now().strftime("%d-%m-%Y %H:%M:%S"))
#     )
#     conn.commit()
#     conn.close()

#     # Generate URLs for the input image and density map for the frontend
#     input_url = url_for('static', filename=unique_name)
#     density_url = url_for('static', filename=density_fname)

#     # Log the URLs for debugging
#     print(f"Input image URL: {input_url}")
#     print(f"Density map URL: {density_url}")

#     # Return the result to the frontend
#     return render_template(
#         "index.html",
#         crowd_count=int(count),
#         input_image=input_url,
#         density_image=density_url
#     )

# # -------------------------------
# # History route: displays past predictions
# # -------------------------------
# @app.route('/history')
# def history():
#     if "user" not in session:
#         return redirect(url_for("login"))

#     conn = sqlite3.connect(DB_PATH)
#     c = conn.cursor()
#     c.execute("SELECT * FROM history ORDER BY id DESC")
#     rows = c.fetchall()
#     conn.close()
#     return render_template("history.html", rows=rows)

# # -------------------------------
# # Favicon route (optional)
# # -------------------------------
# @app.route('/favicon.ico')
# def favicon():
#     return send_from_directory(
#         app.static_folder, 'favicon.ico', mimetype='image/vnd.microsoft.icon'
#     )

# # -------------------------------
# # Run the Flask app
# # -------------------------------
# if __name__ == '__main__':
#     app.run(debug=True)

# from yolo_count import count_people
# from fake_heatmap import generate_fake_density_map

# from flask import Flask, request, render_template, url_for, redirect, session
# import os, uuid, sqlite3
# from datetime import datetime
# from werkzeug.utils import secure_filename
# from model_utils import load_model, predict_image

# app = Flask(__name__)
# app.secret_key = "my_secret_key"

# DB_PATH = "history.db"
# STATIC_DIR = os.path.join(app.root_path, "static")
# os.makedirs(STATIC_DIR, exist_ok=True)

# model = load_model()

# def init_db():
#     con = sqlite3.connect(DB_PATH)
#     c = con.cursor()
#     c.execute("CREATE TABLE IF NOT EXISTS history(id INTEGER PRIMARY KEY AUTOINCREMENT, image_path TEXT, crowd_count INTEGER, predicted_at TEXT)")
#     c.execute("CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY AUTOINCREMENT, email TEXT UNIQUE, password TEXT)")
#     con.commit(); con.close()

# init_db()

# @app.route("/")
# def home():
#     return render_template("index.html")

# @app.route("/predict", methods=["POST"])
# def predict():
#     if "file" not in request.files:
#         return "❌ No file uploaded"

#     file = request.files["file"]
#     fname = secure_filename(file.filename)
#     unique_name = f"{uuid.uuid4().hex}_{fname}"

#     abs_path = os.path.join(STATIC_DIR, unique_name)
#     file.save(abs_path)

#     crowd_count = count_people(abs_path)    # ✅ YOLO counting
#     density_img = None                     # ❗ because YOLO has no density output

#     con = sqlite3.connect(DB_PATH)
#     c = con.cursor()
#     c.execute("INSERT INTO history(image_path,crowd_count,predicted_at) VALUES(?,?,?)",
#             (unique_name, int(crowd_count), datetime.now().strftime("%d-%m-%Y %H:%M:%S")))
#     con.commit(); con.close()

#     return render_template("index.html",
#                            crowd_count=crowd_count,
#                            input_image=url_for("static", filename=unique_name),
#                            density_image=density_img
#                            )


# @app.route("/history")
# def history():
#     con = sqlite3.connect(DB_PATH)
#     c = con.cursor()
#     c.execute("SELECT * FROM history ORDER BY id DESC")
#     rows = c.fetchall()
#     con.close()
#     return render_template("history.html", rows=rows)

# if __name__ == "__main__":
#     app.run(debug=True)


# from yolo_count import count_people
# from fake_heatmap import generate_fake_density_map

# from flask import Flask, request, render_template, url_for, redirect, session
# import os, uuid, sqlite3
# from datetime import datetime
# from werkzeug.utils import secure_filename
# from model_utils import load_model

# app = Flask(__name__)
# app.secret_key = "my_secret_key"

# DB_PATH = "history.db"
# STATIC_DIR = os.path.join(app.root_path, "static")
# OUTPUT_DIR = os.path.join(STATIC_DIR, "outputs")
# os.makedirs(STATIC_DIR, exist_ok=True)
# os.makedirs(OUTPUT_DIR, exist_ok=True)

# model = load_model()

# def init_db():
#     con = sqlite3.connect(DB_PATH)
#     c = con.cursor()
#     c.execute("""
#     CREATE TABLE IF NOT EXISTS history(
#         id INTEGER PRIMARY KEY AUTOINCREMENT, 
#         image_path TEXT, 
#         heatmap_path TEXT,
#         crowd_count INTEGER, 
#         predicted_at TEXT
#     )
#     """)
#     con.commit()
#     con.close()

# init_db()

# @app.route("/")
# def home():
#     return render_template("index.html")

# @app.route("/predict", methods=["POST"])
# def predict():
#     if "file" not in request.files:
#         return "❌ No file uploaded"

#     file = request.files["file"]
#     fname = secure_filename(file.filename)
#     unique_name = f"{uuid.uuid4().hex}_{fname}"
#     abs_path = os.path.join(STATIC_DIR, unique_name)
#     file.save(abs_path)

#     # 🧠 YOLO Person Detection
#     detections = []
#     crowd_count, detections = count_people(abs_path, return_boxes=True)

#     # 🔥 Generate Fake Density Heatmap
#     heatmap_name = generate_fake_density_map(abs_path, detections)
#     heatmap_path = f"outputs/{heatmap_name}"

#     # 💾 Save Results to DB
#     con = sqlite3.connect(DB_PATH)
#     c = con.cursor()
#     c.execute("INSERT INTO history(image_path,heatmap_path,crowd_count,predicted_at) VALUES(?,?,?,?)",
#             (unique_name, heatmap_path, int(crowd_count), datetime.now().strftime("%d-%m-%Y %H:%M:%S")))
#     con.commit()
#     con.close()

#     return render_template(
#         "index.html",
#         crowd_count=crowd_count,
#         input_image=url_for("static", filename=unique_name),
#         density_image=url_for("static", filename=heatmap_path)
#     )

# @app.route("/history")
# def history():
#     con = sqlite3.connect(DB_PATH)
#     c = con.cursor()
#     c.execute("SELECT * FROM history ORDER BY id DESC")
#     rows = c.fetchall()
#     con.close()
#     return render_template("history.html", rows=rows)

# if __name__ == "__main__":
#     app.run(debug=True)



# from flask import Flask, request, render_template, url_for
# import os, uuid, sqlite3
# from datetime import datetime
# from werkzeug.utils import secure_filename

# from yolo_count import count_people   # ✅ Your YOLO file
# from fake_heatmap import generate_fake_density_map  # ✅ Your heatmap file

# app = Flask(__name__)
# app.secret_key = "my_secret_key"

# DB_PATH = "history.db"
# STATIC_DIR = os.path.join(app.root_path, "static")
# os.makedirs(STATIC_DIR, exist_ok=True)


# # ----------------------------------------
# # 🔹 DATABASE INITIALIZATION
# # ----------------------------------------
# def init_db():
#     con = sqlite3.connect(DB_PATH)
#     c = con.cursor()
#     c.execute("""
#         CREATE TABLE IF NOT EXISTS history(
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             image_path TEXT,
#             heatmap_path TEXT,
#             crowd_count INTEGER,
#             predicted_at TEXT
#         )
#     """)
#     con.commit()
#     con.close()

# init_db()


# # ----------------------------------------
# # 🔹 HOME PAGE
# # ----------------------------------------
# @app.route("/")
# def home():
#     return render_template("index.html")


# # ----------------------------------------
# # 🔹 PREDICTION ROUTE
# # ----------------------------------------
# @app.route("/predict", methods=["POST"])
# def predict():
#     if "file" not in request.files:
#         return "❌ No file uploaded"

#     file = request.files["file"]
#     fname = secure_filename(file.filename)
#     unique_name = f"{uuid.uuid4().hex}_{fname}"

#     abs_path = os.path.join(STATIC_DIR, unique_name)
#     file.save(abs_path)

#     # 🟡 YOLO CROWD COUNT
#     count, boxes = count_people(abs_path, return_boxes=True)

#     # 🟠 Generate FAKE heatmap based on bounding boxes
#     heatmap_filename = generate_fake_density_map(abs_path, boxes)

#     # SAVE to Database
#     con = sqlite3.connect(DB_PATH)
#     c = con.cursor()
#     c.execute(
#         "INSERT INTO history(image_path, heatmap_path, crowd_count, predicted_at) VALUES(?,?,?,?)",
#         (unique_name, heatmap_filename, int(count),
#          datetime.now().strftime("%d-%m-%Y %H:%M:%S"))
#     )
#     con.commit()
#     con.close()

#     return render_template("index.html",
#                            crowd_count=count,
#                            input_image=url_for("static", filename=unique_name),
#                            density_image=url_for("static", filename=heatmap_filename)
#                            )


# # ----------------------------------------
# # 🔹 HISTORY PAGE
# # ----------------------------------------
# @app.route("/history")
# def history():
#     con = sqlite3.connect(DB_PATH)
#     c = con.cursor()
#     c.execute("SELECT * FROM history ORDER BY id DESC")
#     rows = c.fetchall()
#     con.close()
#     return render_template("history.html", rows=rows)


# # ----------------------------------------
# # 🔹 MAIN
# # ----------------------------------------
# if __name__ == "__main__":
#     app.run(debug=True)



# working code

# from flask import Flask, request, render_template, url_for
# import os, uuid, sqlite3
# from datetime import datetime
# from werkzeug.utils import secure_filename
# from yolo_count import count_people   # YOLO COUNTER

# app = Flask(__name__)
# app.secret_key = "my_secret_key"

# DB_PATH = "history.db"
# STATIC_DIR = os.path.join(app.root_path, "static")
# os.makedirs(STATIC_DIR, exist_ok=True)


# # -------------------- DB CREATE ----------------------
# def init_db():
#     con = sqlite3.connect(DB_PATH)
#     c = con.cursor()
#     c.execute("""
#         CREATE TABLE IF NOT EXISTS history(
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             image_path TEXT,
#             crowd_count INTEGER,
#             predicted_at TEXT
#         )
#     """)
#     con.commit()
#     con.close()

# init_db()



# # -------------------- HOME PAGE ----------------------
# @app.route("/")
# def home():
#     return render_template("index.html")



# # -------------------- CROWD COUNT ----------------------
# @app.route("/predict", methods=["POST"])
# def predict():
#     if "file" not in request.files:
#         return "❌ No file uploaded"

#     file = request.files["file"]
#     filename = secure_filename(file.filename)
#     unique_name = f"{uuid.uuid4().hex}_{filename}"

#     save_path = os.path.join(STATIC_DIR, unique_name)
#     file.save(save_path)

#     # COUNT PEOPLE
#     crowd_count = count_people(save_path)

#     # SAVE TO DATABASE
#     con = sqlite3.connect(DB_PATH)
#     c = con.cursor()
#     c.execute("INSERT INTO history(image_path, crowd_count, predicted_at) VALUES(?,?,?)",
#               (unique_name, crowd_count, datetime.now().strftime("%d-%m-%Y %H:%M:%S")))
#     con.commit()
#     con.close()

#     return render_template("index.html",
#                            crowd_count=crowd_count,
#                            input_image=url_for("static", filename=unique_name)
#                            )



# # -------------------- HISTORY PAGE ----------------------
# @app.route("/history")
# def history():
#     con = sqlite3.connect(DB_PATH)
#     c = con.cursor()
#     c.execute("SELECT * FROM history ORDER BY id DESC")
#     rows = c.fetchall()
#     con.close()
#     return render_template("history.html", rows=rows)



# # -------------------- MAIN ----------------------
# if __name__ == "__main__":
#     app.run(debug=True)


# from flask import Flask, request, render_template, url_for
# import os, uuid, sqlite3
# from datetime import datetime
# from werkzeug.utils import secure_filename
# from yolo_count import count_people  # Import updated function

# app = Flask(__name__)
# app.secret_key = "my_secret_key"

# DB_PATH = "history.db"
# STATIC_DIR = os.path.join(app.root_path, "static")
# os.makedirs(STATIC_DIR, exist_ok=True)

# # -------------------- DB INIT ----------------------
# def init_db():
#     con = sqlite3.connect(DB_PATH)
#     c = con.cursor()
#     c.execute("""
#         CREATE TABLE IF NOT EXISTS history(
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             image_path TEXT,
#             crowd_count INTEGER,
#             avg_conf REAL,
#             predicted_at TEXT
#         )
#     """)
#     con.commit()
#     con.close()

# init_db()

# # -------------------- HOME PAGE ----------------------
# @app.route("/")
# def home():
#     return render_template("index.html")

# # -------------------- PREDICT ----------------------
# @app.route("/predict", methods=["POST"])
# def predict():
#     if "file" not in request.files:
#         return "❌ No file uploaded"

#     file = request.files["file"]
#     filename = secure_filename(file.filename)
#     unique_name = f"{uuid.uuid4().hex}_{filename}"

#     save_path = os.path.join(STATIC_DIR, unique_name)
#     file.save(save_path)

#     # GET CROWD COUNT + AVERAGE CONFIDENCE
#     crowd_count, avg_conf = count_people(save_path)

#     # SAVE TO DATABASE
#     con = sqlite3.connect(DB_PATH)
#     c = con.cursor()
#     c.execute("INSERT INTO history(image_path, crowd_count, avg_conf, predicted_at) VALUES(?,?,?,?)",
#               (unique_name, crowd_count, avg_conf, datetime.now().strftime("%d-%m-%Y %H:%M:%S")))
#     con.commit()
#     con.close()

#     return render_template("index.html",
#                            crowd_count=crowd_count,
#                            avg_conf=avg_conf,
#                            model_name="YOLOv8n",
#                            input_image=url_for("static", filename=unique_name)
#                            )

# # -------------------- HISTORY ----------------------
# @app.route("/history")
# def history():
#     con = sqlite3.connect(DB_PATH)
#     c = con.cursor()
#     c.execute("SELECT * FROM history ORDER BY id DESC")
#     rows = c.fetchall()
#     con.close()
#     return render_template("history.html", rows=rows)

# # -------------------- MAIN ----------------------
# if __name__ == "__main__":
#     app.run(debug=True)

# from flask import Flask, request, render_template, url_for
# import os, uuid, sqlite3
# from datetime import datetime
# from werkzeug.utils import secure_filename
# from yolo_count import count_people  # Import updated YOLO function

# app = Flask(__name__)
# app.secret_key = "my_secret_key"

# DB_PATH = "history.db"
# STATIC_DIR = os.path.join(app.root_path, "static")
# os.makedirs(STATIC_DIR, exist_ok=True)

# # -------------------- DB INIT ----------------------
# def init_db():
#     con = sqlite3.connect(DB_PATH)
#     c = con.cursor()
#     c.execute("""
#         CREATE TABLE IF NOT EXISTS history(
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             image_path TEXT,
#             crowd_count INTEGER,
#             avg_conf REAL,
#             predicted_at TEXT
#         )
#     """)
    
#     # Ensure avg_conf exists
#     c.execute("PRAGMA table_info(history)")
#     cols = [col[1] for col in c.fetchall()]
#     if "avg_conf" not in cols:
#         c.execute("ALTER TABLE history ADD COLUMN avg_conf REAL")

#     con.commit()
#     con.close()

# init_db()

# # -------------------- HOME PAGE ----------------------
# @app.route("/")
# def home():
#     return render_template("index.html")

# # -------------------- CROWD COUNT ----------------------
# @app.route("/predict", methods=["POST"])
# def predict():
#     if "file" not in request.files:
#         return "❌ No file uploaded"

#     file = request.files["file"]
#     filename = secure_filename(file.filename)
#     unique_name = f"{uuid.uuid4().hex}_{filename}"

#     save_path = os.path.join(STATIC_DIR, unique_name)
#     file.save(save_path)

#     crowd_count, avg_conf = count_people(save_path)

#     # SAVE TO DB
#     con = sqlite3.connect(DB_PATH)
#     c = con.cursor()
#     c.execute("INSERT INTO history(image_path, crowd_count, avg_conf, predicted_at) VALUES(?,?,?,?)",
#               (unique_name, crowd_count, avg_conf, datetime.now().strftime("%d-%m-%Y %H:%M:%S")))
#     con.commit()
#     con.close()

#     return render_template("index.html",
#                            crowd_count=crowd_count,
#                            avg_conf=avg_conf,
#                            model_name="YOLOv8n",
#                            input_image=url_for("static", filename=unique_name)
#                            )

# # -------------------- HISTORY PAGE ----------------------
# @app.route("/history")
# def history():
#     con = sqlite3.connect(DB_PATH)
#     c = con.cursor()
#     c.execute("SELECT * FROM history ORDER BY id DESC")
#     rows = c.fetchall()
#     con.close()
#     return render_template("history.html", rows=rows)

# # -------------------- MAIN RUN ----------------------
# if __name__ == "__main__":
#     app.run(debug=True)

# new code 25/11

# from flask import Flask, request, render_template, url_for
# import os, uuid, sqlite3
# from datetime import datetime
# from werkzeug.utils import secure_filename

# from model_utils import load_model, predict_image

# app = Flask(__name__)
# app.secret_key = "my_secret_key"

# DB_PATH = "history.db"
# STATIC_DIR = os.path.join(app.root_path, "static")
# os.makedirs(STATIC_DIR, exist_ok=True)

# # -------------------- LOAD CSRNet MODEL ----------------------
# model = load_model(device="cpu")


# # -------------------- DB INIT ----------------------
# def init_db():
#     con = sqlite3.connect(DB_PATH)
#     c = con.cursor()
#     c.execute("""
#         CREATE TABLE IF NOT EXISTS history(
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             image_path TEXT,
#             density_path TEXT,
#             crowd_count INTEGER,
#             predicted_at TEXT
#         )
#     """)
#     con.commit()
#     con.close()

# init_db()


# # -------------------- HOME PAGE ----------------------
# @app.route("/")
# def home():
#     return render_template("index.html")


# # -------------------- PREDICT ROUTE ----------------------
# @app.route("/predict", methods=["POST"])
# def predict():
#     if "file" not in request.files:
#         return "❌ No file uploaded"

#     file = request.files["file"]
#     filename = secure_filename(file.filename)

#     unique_name = f"{uuid.uuid4().hex}_{filename}"
#     save_path = os.path.join(STATIC_DIR, unique_name)
#     file.save(save_path)

#     # ---- PREDICT WITH CSRNet ----
#     count, density_file = predict_image(model, save_path)

#     density_url = url_for("static", filename=density_file)

#     # ---- SAVE TO HISTORY ----
#     con = sqlite3.connect(DB_PATH)
#     c = con.cursor()
#     c.execute("""
#         INSERT INTO history(image_path, density_path, crowd_count, predicted_at)
#         VALUES (?, ?, ?, ?)
#     """, (unique_name, density_file, count, datetime.now().strftime("%d-%m-%Y %H:%M:%S")))
#     con.commit()
#     con.close()

#     return render_template(
#         "index.html",
#         crowd_count=count,
#         input_image=url_for("static", filename=unique_name),
#         density_image=density_url
#     )


# # -------------------- HISTORY PAGE ----------------------
# @app.route("/history")
# def history():
#     con = sqlite3.connect(DB_PATH)
#     c = con.cursor()
#     c.execute("SELECT * FROM history ORDER BY id DESC")
#     rows = c.fetchall()
#     con.close()
#     return render_template("history.html", rows=rows)


# # -------------------- MAIN ----------------------
# if __name__ == "__main__":
#     app.run(debug=True)











# app.py (replace your existing app.py with this)
# from flask import Flask, request, render_template, url_for, redirect, session, flash
# import os, uuid, sqlite3
# from datetime import datetime
# from werkzeug.utils import secure_filename
# from werkzeug.security import generate_password_hash, check_password_hash

# from model_utils import load_model, predict_image  # keep your CSRNet utilities

# app = Flask(__name__)
# app.secret_key = "my_secret_key"  # change this for production!

# # -------------------- PATHS ----------------------
# DB_PATH = "history.db"
# STATIC_DIR = os.path.join(app.root_path, "static")
# UPLOAD_FOLDER = os.path.join(STATIC_DIR, "uploads")
# DENSITY_FOLDER = os.path.join(STATIC_DIR, "density")

# os.makedirs(UPLOAD_FOLDER, exist_ok=True)
# os.makedirs(DENSITY_FOLDER, exist_ok=True)

# # -------------------- LOAD CSRNet MODEL ----------------------
# # This will load the model once on startup
# try:
#     model = load_model(device="cpu")
# except Exception as e:
#     print("Warning: could not load model on startup:", e)
#     model = None

# # -------------------- DB INIT ----------------------
# def init_db():
#     con = sqlite3.connect(DB_PATH)
#     c = con.cursor()

#     # history table (image and density)
#     c.execute("""
#         CREATE TABLE IF NOT EXISTS history(
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             image_path TEXT,
#             density_path TEXT,
#             crowd_count INTEGER,
#             predicted_at TEXT
#         )
#     """)

#     # users table for login/signup
#     c.execute("""
#         CREATE TABLE IF NOT EXISTS users(
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             username TEXT UNIQUE,
#             password_hash TEXT,
#             created_at TEXT
#         )
#     """)

#     con.commit()
#     con.close()

# init_db()

# # -------------------- HELPERS ----------------------
# def get_db_connection():
#     return sqlite3.connect(DB_PATH)

# def current_user():
#     """Return username if logged in, else None"""
#     return session.get("username")

# def login_required(fn):
#     """Simple decorator to require login for routes (lightweight)"""
#     from functools import wraps
#     @wraps(fn)
#     def wrapper(*args, **kwargs):
#         if not current_user():
#             return redirect(url_for("login"))
#         return fn(*args, **kwargs)
#     return wrapper

# # -------------------- AUTH ROUTES ----------------------
# @app.route("/signup", methods=["GET", "POST"])
# def signup():
#     if request.method == "POST":
#         username = request.form.get("username", "").strip()
#         password = request.form.get("password", "")

#         if not username or not password:
#             flash("Please provide username and password.", "error")
#             return render_template("signup.html")

#         pw_hash = generate_password_hash(password)

#         try:
#             con = get_db_connection()
#             c = con.cursor()
#             c.execute("INSERT INTO users(username, password_hash, created_at) VALUES(?,?,?)",
#                       (username, pw_hash, datetime.now().strftime("%d-%m-%Y %H:%M:%S")))
#             con.commit()
#             con.close()
#         except sqlite3.IntegrityError:
#             flash("Username already exists. Choose another.", "error")
#             return render_template("signup.html")

#         flash("Account created. Please log in.", "success")
#         return redirect(url_for("login"))

#     return render_template("signup.html")


# @app.route("/login", methods=["GET", "POST"])
# def login():
#     if request.method == "POST":
#         username = request.form.get("username", "").strip()
#         password = request.form.get("password", "")

#         if not username or not password:
#             flash("Please fill both fields.", "error")
#             return render_template("login.html")

#         con = get_db_connection()
#         c = con.cursor()
#         c.execute("SELECT password_hash FROM users WHERE username = ?", (username,))
#         row = c.fetchone()
#         con.close()

#         if not row:
#             flash("Invalid username or password.", "error")
#             return render_template("login.html")

#         pw_hash = row[0]
#         if not check_password_hash(pw_hash, password):
#             flash("Invalid username or password.", "error")
#             return render_template("login.html")

#         # login success
#         session["username"] = username
#         flash(f"Welcome, {username}!", "success")
#         return redirect(url_for("home"))

#     return render_template("login.html")


# @app.route("/logout")
# def logout():
#     session.pop("username", None)
#     flash("Logged out.", "info")
#     return redirect(url_for("login"))

# # -------------------- HOME PAGE (requires login) ----------------------
# @app.route("/")
# @login_required
# def home():
#     # Render the main index page (upload + results)
#     return render_template("index.html", crowd_count=None)

# # -------------------- PREDICT ROUTE (requires login) ----------------------
# @app.route("/predict", methods=["POST"])
# @login_required
# def predict():
#     if "file" not in request.files:
#         flash("No file uploaded.", "error")
#         return redirect(url_for("home"))

#     file = request.files["file"]
#     if file.filename == "":
#         flash("No file selected.", "error")
#         return redirect(url_for("home"))

#     filename = secure_filename(file.filename)
#     unique_name = f"{uuid.uuid4().hex}_{filename}"
#     save_path = os.path.join(UPLOAD_FOLDER, unique_name)

#     try:
#         # Save uploaded file into static/uploads
#         file.save(save_path)
#     except Exception as e:
#         flash(f"Failed to save uploaded file: {e}", "error")
#         return redirect(url_for("home"))

#     # ---- ensure model loaded ----
#     global model
#     if model is None:
#         try:
#             model = load_model(device="cpu")
#         except Exception as e:
#             flash("Model could not be loaded. See server logs.", "error")
#             return redirect(url_for("home"))

#     # ---- PREDICT WITH CSRNet ----
#     try:
#         count, density_filename = predict_image(model, save_path)
#     except Exception as e:
#         flash(f"Prediction failed: {e}", "error")
#         return redirect(url_for("home"))

#     # density_filename returned as filename relative to static/ (model_utils should return that)
#     # If model_utils saved into static/ then density_filename is the filename; otherwise adapt.
#     # We save density into DENSITY_FOLDER to be consistent:
#     # If predict_image returned a full path, normalize it:
#     # (here we assume it returns a filename like "density_<origname>.png")
#     density_src_rel = density_filename
#     density_url = url_for("static", filename=os.path.join("density", os.path.basename(density_src_rel)))

#     # move density file to static/density if predict_image saved elsewhere
#     # (safe-guard: if file exists in project/static root, move to density folder)
#     # NOTE: adapt this section if your predict_image already saves to static/density
#     possible_path_in_static = os.path.join(STATIC_DIR, density_src_rel)
#     if os.path.exists(possible_path_in_static):
#         # move into density folder
#         dest = os.path.join(DENSITY_FOLDER, os.path.basename(density_src_rel))
#         try:
#             os.replace(possible_path_in_static, dest)
#         except Exception:
#             pass
#         density_url = url_for("static", filename=os.path.join("density", os.path.basename(density_src_rel)))
#     else:
#         # maybe predict_image already saved to DENSITY_FOLDER
#         dest = os.path.join(DENSITY_FOLDER, os.path.basename(density_src_rel))
#         if not os.path.exists(dest) and os.path.exists(os.path.join(STATIC_DIR, "density", os.path.basename(density_src_rel))):
#             dest = os.path.join(STATIC_DIR, "density", os.path.basename(density_src_rel))

#     # ---- SAVE TO HISTORY ----
#     con = get_db_connection()
#     c = con.cursor()
#     c.execute("""
#         INSERT INTO history(image_path, density_path, crowd_count, predicted_at)
#         VALUES (?, ?, ?, ?)
#     """, (os.path.join("uploads", unique_name), os.path.join("density", os.path.basename(density_src_rel)), int(count), datetime.now().strftime("%d-%m-%Y %H:%M:%S")))
#     con.commit()
#     con.close()

#     # Render index with results
#     return render_template(
#         "index.html",
#         crowd_count=count,
#         input_image=url_for("static", filename=os.path.join("uploads", unique_name)),
#         density_image=density_url
#     )

# # -------------------- HISTORY PAGE ----------------------
# @app.route("/history")
# @login_required
# def history():
#     con = get_db_connection()
#     c = con.cursor()
#     c.execute("SELECT id, image_path, density_path, crowd_count, predicted_at FROM history ORDER BY id DESC")
#     rows = c.fetchall()
#     con.close()
#     return render_template("history.html", rows=rows)

# # -------------------- RUN ----------------------
# if __name__ == "__main__":
#     app.run(debug=True)






# import os
# import sqlite3
# import uuid
# from flask import Flask, render_template, request, redirect, url_for, session
# from werkzeug.utils import secure_filename
# from model_utils import load_model, predict_density_map

# app = Flask(__name__)
# app.secret_key = "your_secret_key"

# UPLOAD_FOLDER = "static/uploads"
# DENSITY_FOLDER = "static/density_maps"

# os.makedirs(UPLOAD_FOLDER, exist_ok=True)
# os.makedirs(DENSITY_FOLDER, exist_ok=True)

# # -----------------------------------------------------------
# # DATABASE SETUP
# # -----------------------------------------------------------
# def init_db():
#     conn = sqlite3.connect("users.db")
#     c = conn.cursor()

#     # user table
#     c.execute("""
#         CREATE TABLE IF NOT EXISTS users (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             username TEXT UNIQUE,
#             password TEXT
#         )
#     """)

#     # history table
#     c.execute("""
#         CREATE TABLE IF NOT EXISTS history (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             user_id INTEGER,
#             image_path TEXT,
#             density_path TEXT,
#             count REAL
#         )
#     """)

#     conn.commit()
#     conn.close()

# init_db()

# # -----------------------------------------------------------
# # LOGIN CHECK DECORATOR
# # -----------------------------------------------------------
# from functools import wraps
# def login_required(f):
#     @wraps(f)
#     def secure(*args, **kwargs):
#         if "user_id" not in session:
#             return redirect(url_for("login"))
#         return f(*args, **kwargs)
#     return secure

# # -----------------------------------------------------------
# # ROUTES
# # -----------------------------------------------------------

# @app.route("/")
# def root():
#     return redirect(url_for("login"))

# @app.route("/home")
# @login_required
# def home():
#     return render_template("index.html", crowd_count=None)

# # ---------------- LOGIN ----------------
# @app.route("/login", methods=["GET", "POST"])
# def login():
#     if request.method == "POST":
#         username = request.form["username"]
#         password = request.form["password"]

#         conn = sqlite3.connect("users.db")
#         c = conn.cursor()
#         c.execute("SELECT id FROM users WHERE username=? AND password=?", (username, password))
#         user = c.fetchone()
#         conn.close()

#         if user:
#             session["user_id"] = user[0]
#             return redirect(url_for("home"))
#         else:
#             return render_template("login.html", error="Invalid username or password")

#     return render_template("login.html")

# # ---------------- SIGNUP ----------------
# @app.route("/signup", methods=["GET", "POST"])
# def signup():
#     if request.method == "POST":
#         username = request.form["username"]
#         password = request.form["password"]

#         conn = sqlite3.connect("users.db")
#         c = conn.cursor()

#         try:
#             c.execute("INSERT INTO users(username, password) VALUES(?,?)", (username, password))
#             conn.commit()
#             conn.close()
#             return redirect(url_for("login"))
#         except:
#             conn.close()
#             return render_template("signup.html", error="Username already exists")

#     return render_template("signup.html")

# # ---------------- LOGOUT ----------------
# @app.route("/logout")
# def logout():
#     session.clear()
#     return redirect(url_for("login"))

# # -----------------------------------------------------------
# # PREDICT ROUTE
# # -----------------------------------------------------------

# model = load_model()

# @app.route("/predict", methods=["POST"])
# @login_required
# def predict():
#     file = request.files["file"]

#     if file.filename == "":
#         return redirect(url_for("home"))

#     filename = secure_filename(file.filename)
#     unique_name = f"{uuid.uuid4()}_{filename}"
#     save_path = os.path.join(UPLOAD_FOLDER, unique_name)
#     file.save(save_path)

#     # Run CSRNet prediction
#     count, density_map_path = predict_density_map(model, save_path)

#     # Store into database
#     conn = sqlite3.connect("users.db")
#     c = conn.cursor()
#     c.execute("INSERT INTO history(user_id, image_path, density_path, count) VALUES (?,?,?,?)",
#               (session["user_id"], save_path, density_map_path, count))
#     conn.commit()
#     conn.close()

#     return render_template("index.html",
#                            crowd_count=int(count),
#                            input_image="/" + save_path,
#                            density_image="/" + density_map_path)

# # -----------------------------------------------------------
# # HISTORY PAGE
# # -----------------------------------------------------------
# @app.route("/history")
# @login_required
# def history():
#     conn = sqlite3.connect("users.db")
#     c = conn.cursor()
#     c.execute("SELECT image_path, density_path, count FROM history WHERE user_id=?",
#               (session["user_id"],))
#     data = c.fetchall()
#     conn.close()
#     return render_template("history.html", records=data)

# # -----------------------------------------------------------
# # RUN
# # -----------------------------------------------------------

# if __name__ == "__main__":
#     app.run(debug=True)


















# import os
# import sqlite3
# import uuid
# from flask import Flask, render_template, request, redirect, url_for, session
# from werkzeug.utils import secure_filename
# from model_utils import load_model, predict_density_map


# app = Flask(__name__)
# app.secret_key = "your_secret_key"

# UPLOAD_FOLDER = "static/uploads"
# DENSITY_FOLDER = "static/density_maps"

# os.makedirs(UPLOAD_FOLDER, exist_ok=True)
# os.makedirs(DENSITY_FOLDER, exist_ok=True)

# # -----------------------------------------------------------
# # DATABASE SETUP
# # -----------------------------------------------------------
# def init_db():
#     conn = sqlite3.connect("users.db")
#     c = conn.cursor()

#     # user table
#     c.execute("""
#         CREATE TABLE IF NOT EXISTS users (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             username TEXT UNIQUE,
#             password TEXT
#         )
#     """)

#     # history table
#     c.execute("""
#         CREATE TABLE IF NOT EXISTS history (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             user_id INTEGER,
#             image_path TEXT,
#             density_path TEXT,
#             count REAL
#         )
#     """)

#     conn.commit()
#     conn.close()

# init_db()

# # -----------------------------------------------------------
# # LOGIN CHECK DECORATOR
# # -----------------------------------------------------------
# from functools import wraps
# def login_required(f):
#     @wraps(f)
#     def secure(*args, **kwargs):
#         if "user_id" not in session:
#             return redirect(url_for("login"))
#         return f(*args, **kwargs)
#     return secure

# # -----------------------------------------------------------
# # ROUTES
# # -----------------------------------------------------------

# @app.route("/")
# def root():
#     return redirect(url_for("login"))

# @app.route("/home")
# @login_required
# def home():
#     return render_template("index.html", crowd_count=None)

# # ---------------- LOGIN ----------------
# @app.route("/login", methods=["GET", "POST"])
# def login():
#     if request.method == "POST":
#         username = request.form["username"]
#         password = request.form["password"]

#         conn = sqlite3.connect("users.db")
#         c = conn.cursor()
#         c.execute("SELECT id FROM users WHERE username=? AND password=?", (username, password))
#         user = c.fetchone()
#         conn.close()

#         if user:
#             session["user_id"] = user[0]
#             return redirect(url_for("home"))
#         else:
#             return render_template("login.html", error="Invalid username or password")

#     return render_template("login.html")

# # ---------------- SIGNUP ----------------
# @app.route("/signup", methods=["GET", "POST"])
# def signup():
#     if request.method == "POST":
#         username = request.form["username"]
#         password = request.form["password"]

#         conn = sqlite3.connect("users.db")
#         c = conn.cursor()

#         try:
#             c.execute("INSERT INTO users(username, password) VALUES(?,?)", (username, password))
#             conn.commit()
#             conn.close()
#             return redirect(url_for("login"))
#         except:
#             conn.close()
#             return render_template("signup.html", error="Username already exists")

#     return render_template("signup.html")

# # ---------------- LOGOUT ----------------
# @app.route("/logout")
# def logout():
#     session.clear()
#     return redirect(url_for("login"))

# # -----------------------------------------------------------
# # PREDICT ROUTE
# # -----------------------------------------------------------

# model = load_model()

# @app.route("/predict", methods=["POST"])
# @login_required
# def predict():
#     file = request.files["file"]

#     if file.filename == "":
#         return redirect(url_for("home"))

#     filename = secure_filename(file.filename)
#     unique_name = f"{uuid.uuid4()}_{filename}"
#     save_path = os.path.join(UPLOAD_FOLDER, unique_name)
#     file.save(save_path)

#     # Run CSRNet prediction
#     count, density_map_path = predict_density_map(model, save_path)

#     # Store into database
#     conn = sqlite3.connect("users.db")
#     c = conn.cursor()
#     c.execute("INSERT INTO history(user_id, image_path, density_path, count) VALUES (?,?,?,?)",
#               (session["user_id"], save_path, density_map_path, count))
#     conn.commit()
#     conn.close()

#     return render_template("index.html",
#                            crowd_count=int(count),
#                            input_image="/" + save_path,
#                            density_image="/" + density_map_path)

# # -----------------------------------------------------------
# # HISTORY PAGE
# # -----------------------------------------------------------
# @app.route("/history")
# @login_required
# def history():
#     conn = sqlite3.connect("users.db")
#     c = conn.cursor()
#     c.execute("SELECT image_path, density_path, count FROM history WHERE user_id=?",
#               (session["user_id"],))
#     data = c.fetchall()
#     conn.close()
#     return render_template("history.html", records=data)

# # -----------------------------------------------------------
# # RUN
# # -----------------------------------------------------------

# if __name__ == "__main__":
#     app.run(debug=True)













# import os
# import sqlite3
# import uuid
# from flask import Flask, render_template, request, redirect, url_for, session
# from werkzeug.utils import secure_filename
# from model_utils import load_model, predict_density_map
# from functools import wraps

# app = Flask(__name__)
# app.secret_key = "your_secret_key"

# UPLOAD_FOLDER = "static/uploads"
# DENSITY_FOLDER = "static/density_maps"

# os.makedirs(UPLOAD_FOLDER, exist_ok=True)
# os.makedirs(DENSITY_FOLDER, exist_ok=True)

# # -----------------------------------------------------------
# # DATABASE SETUP
# # -----------------------------------------------------------
# def init_db():
#     conn = sqlite3.connect("users.db")
#     c = conn.cursor()

#     # user table
#     c.execute("""
#         CREATE TABLE IF NOT EXISTS users (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             email TEXT UNIQUE,
#             password TEXT
#         )
#     """)

#     # history table
#     c.execute("""
#         CREATE TABLE IF NOT EXISTS history (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             user_id INTEGER,
#             image_path TEXT,
#             density_path TEXT,
#             count REAL
#         )
#     """)

#     conn.commit()
#     conn.close()

# init_db()

# # -----------------------------------------------------------
# # LOGIN CHECK DECORATOR
# # -----------------------------------------------------------
# def login_required(f):
#     @wraps(f)
#     def secure(*args, **kwargs):
#         if "user_id" not in session:
#             return redirect(url_for("login"))
#         return f(*args, **kwargs)
#     return secure


# # -----------------------------------------------------------
# # ROUTES
# # -----------------------------------------------------------

# @app.route("/")
# def root():
#     return redirect(url_for("login"))


# @app.route("/home")
# @login_required
# def home():
#     return render_template("index.html", crowd_count=None)


# # ---------------- LOGIN ----------------
# @app.route("/login", methods=["GET", "POST"])
# def login():
#     if request.method == "POST":

#         email = request.form.get("email")
#         password = request.form.get("password")

#         conn = sqlite3.connect("users.db")
#         c = conn.cursor()
#         c.execute("SELECT id FROM users WHERE email=? AND password=?", (email, password))
#         user = c.fetchone()
#         conn.close()

#         if user:
#             session["user_id"] = user[0]
#             return redirect(url_for("home"))
#         else:
#             return render_template("login.html", error="Invalid email or password")

#     return render_template("login.html")


# # ---------------- SIGNUP ----------------
# @app.route("/signup", methods=["GET", "POST"])
# def signup():
#     if request.method == "POST":

#         email = request.form.get("email")
#         password = request.form.get("password")

#         conn = sqlite3.connect("users.db")
#         c = conn.cursor()

#         try:
#             c.execute("INSERT INTO users(email, password) VALUES(?,?)", (email, password))
#             conn.commit()
#             conn.close()
#             return redirect(url_for("login"))

#         except:
#             conn.close()
#             return render_template("signup.html", error="Email already exists")

#     return render_template("signup.html")


# # ---------------- LOGOUT ----------------
# @app.route("/logout")
# def logout():
#     session.clear()
#     return redirect(url_for("login"))


# # -----------------------------------------------------------
# # PREDICT ROUTE
# # -----------------------------------------------------------

# model = load_model()

# @app.route("/predict", methods=["POST"])
# @login_required
# def predict():
#     file = request.files.get("file")

#     if not file or file.filename == "":
#         return redirect(url_for("home"))

#     filename = secure_filename(file.filename)
#     unique_name = f"{uuid.uuid4()}_{filename}"
#     save_path = os.path.join(UPLOAD_FOLDER, unique_name)
#     file.save(save_path)

#     # Run CSRNet prediction
#     count, density_map_path = predict_density_map(model, save_path)

#     # Store into database
#     conn = sqlite3.connect("users.db")
#     c = conn.cursor()
#     c.execute("""
#         INSERT INTO history(user_id, image_path, density_path, count)
#         VALUES (?,?,?,?)
#     """,
#         (session["user_id"], save_path, density_map_path, count))

#     conn.commit()
#     conn.close()

#     return render_template("index.html",
#                            crowd_count=int(count),
#                            input_image="/" + save_path,
#                            density_image="/" + density_map_path)


# # -----------------------------------------------------------
# # HISTORY PAGE
# # -----------------------------------------------------------
# @app.route("/history")
# @login_required
# def history():
#     conn = sqlite3.connect("users.db")
#     c = conn.cursor()
#     c.execute("""
#         SELECT image_path, density_path, count
#         FROM history WHERE user_id=?
#     """, (session["user_id"],))
#     data = c.fetchall()
#     conn.close()

#     return render_template("history.html", records=data)


# # -----------------------------------------------------------
# # RUN
# # -----------------------------------------------------------
# if __name__ == "__main__":
#     app.run(debug=True)








# import os
# import sqlite3
# import uuid
# from flask import Flask, render_template, request, redirect, url_for, session, flash
# from werkzeug.utils import secure_filename
# from model_utils import load_model, predict_density_map
# from functools import wraps

# app = Flask(__name__)
# app.secret_key = "your_secret_key"

# # folders inside project root
# STATIC_DIR = os.path.join(app.root_path, "static")
# UPLOAD_FOLDER = os.path.join(STATIC_DIR, "uploads")
# DENSITY_FOLDER = os.path.join(STATIC_DIR, "density_maps")

# os.makedirs(UPLOAD_FOLDER, exist_ok=True)
# os.makedirs(DENSITY_FOLDER, exist_ok=True)

# DB_PATH = os.path.join(app.root_path, "users.db")

# # -----------------------------------------------------------
# # DATABASE SETUP
# # -----------------------------------------------------------
# def init_db():
#     conn = sqlite3.connect(DB_PATH)
#     c = conn.cursor()

#     # user table (email + password)
#     c.execute("""
#         CREATE TABLE IF NOT EXISTS users (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             email TEXT UNIQUE,
#             password TEXT
#         )
#     """)

#     # history table
#     c.execute("""
#         CREATE TABLE IF NOT EXISTS history (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             user_id INTEGER,
#             image_path TEXT,
#             density_path TEXT,
#             count REAL
#         )
#     """)

#     conn.commit()
#     conn.close()

# init_db()

# # -----------------------------------------------------------
# # LOGIN CHECK DECORATOR
# # -----------------------------------------------------------
# def login_required(f):
#     @wraps(f)
#     def secure(*args, **kwargs):
#         if "user_id" not in session:
#             return redirect(url_for("login"))
#         return f(*args, **kwargs)
#     return secure


# # -----------------------------------------------------------
# # ROUTES
# # -----------------------------------------------------------

# @app.route("/")
# def root():
#     # show login page by default
#     return redirect(url_for("login"))


# @app.route("/home")
# @login_required
# def home():
#     return render_template("index.html", crowd_count=None)


# # ---------------- LOGIN ----------------
# @app.route("/login", methods=["GET", "POST"])
# def login():
#     if request.method == "POST":
#         email = request.form.get("email")
#         password = request.form.get("password")

#         if not email or not password:
#             return render_template("login.html", error="Please enter email and password.")

#         conn = sqlite3.connect(DB_PATH)
#         c = conn.cursor()
#         c.execute("SELECT id FROM users WHERE email=? AND password=?", (email, password))
#         user = c.fetchone()
#         conn.close()

#         if user:
#             session["user_id"] = user[0]
#             return redirect(url_for("home"))
#         else:
#             return render_template("login.html", error="Invalid email or password.")

#     return render_template("login.html")


# # ---------------- SIGNUP ----------------
# @app.route("/signup", methods=["GET", "POST"])
# def signup():
#     if request.method == "POST":
#         email = request.form.get("email")
#         password = request.form.get("password")

#         if not email or not password:
#             return render_template("signup.html", error="All fields are required.")

#         conn = sqlite3.connect(DB_PATH)
#         c = conn.cursor()
#         try:
#             c.execute("INSERT INTO users(email, password) VALUES(?,?)", (email, password))
#             conn.commit()
#             conn.close()
#             return redirect(url_for("login"))
#         except sqlite3.IntegrityError:
#             conn.close()
#             return render_template("signup.html", error="Email already exists.")
#         except Exception as e:
#             conn.close()
#             return render_template("signup.html", error="Failed to create account.")

#     return render_template("signup.html")


# # ---------------- LOGOUT ----------------
# @app.route("/logout")
# def logout():
#     session.clear()
#     return redirect(url_for("login"))


# # -----------------------------------------------------------
# # PREDICT ROUTE
# # -----------------------------------------------------------

# # Load model once at startup (load_model in model_utils)
# model = None
# try:
#     model = load_model()
# except Exception as e:
#     # we'll attempt to reload at prediction time if model failed here
#     print("Warning: load_model failed at startup:", e)

# @app.route("/predict", methods=["POST"])
# @login_required
# def predict():
#     file = request.files.get("file")
#     if not file or file.filename == "":
#         flash("No file selected.")
#         return redirect(url_for("home"))

#     filename = secure_filename(file.filename)
#     unique_name = f"{uuid.uuid4().hex}_{filename}"
#     save_path = os.path.join(UPLOAD_FOLDER, unique_name)

#     try:
#         file.save(save_path)
#     except Exception as e:
#         flash(f"Failed to save uploaded file: {e}")
#         return redirect(url_for("home"))

#     # ensure model is loaded
#     global model
#     if model is None:
#         try:
#             model = load_model()
#         except Exception as e:
#             flash("Model load failed. Check server logs.")
#             return redirect(url_for("home"))

#     # predict
#     try:
#         count, density_rel_path = predict_density_map(model, save_path)
#     except Exception as e:
#         flash(f"Prediction failed: {e}")
#         return redirect(url_for("home"))

#     # density_rel_path should be relative path under static/, e.g. "density_maps/dens_abc.png"
#     # Save record to DB (store relative paths)
#     conn = sqlite3.connect(DB_PATH)
#     c = conn.cursor()
#     c.execute("INSERT INTO history(user_id, image_path, density_path, count) VALUES (?,?,?,?)",
#               (session["user_id"], os.path.join("uploads", unique_name), density_rel_path, float(count)))
#     conn.commit()
#     conn.close()

#     input_url = url_for("static", filename=os.path.join("uploads", unique_name))
#     density_url = url_for("static", filename=density_rel_path)

#     return render_template("index.html",
#                            crowd_count=int(round(count)),
#                            input_image=input_url,
#                            density_image=density_url)


# # -----------------------------------------------------------
# # HISTORY PAGE
# # -----------------------------------------------------------
# @app.route("/history")
# @login_required
# def history():
#     conn = sqlite3.connect(DB_PATH)
#     c = conn.cursor()
#     c.execute("SELECT image_path, density_path, count FROM history WHERE user_id=?", (session["user_id"],))
#     data = c.fetchall()
#     conn.close()
#     # convert rows to list, render template expects list of tuples
#     return render_template("history.html", records=data)


# # -----------------------------------------------------------
# # RUN
# # -----------------------------------------------------------
# if __name__ == "__main__":
#     app.run(debug=True)

















# import os
# import sqlite3
# import uuid
# from flask import Flask, render_template, request, redirect, url_for, session, flash
# from werkzeug.utils import secure_filename
# from model_utils import load_model, predict_density_map
# from functools import wraps

# app = Flask(__name__)
# app.secret_key = "your_secret_key"

# # folders inside project root
# STATIC_DIR = os.path.join(app.root_path, "static")
# UPLOAD_FOLDER = os.path.join(STATIC_DIR, "uploads")
# DENSITY_FOLDER = os.path.join(STATIC_DIR, "density_maps")

# os.makedirs(UPLOAD_FOLDER, exist_ok=True)
# os.makedirs(DENSITY_FOLDER, exist_ok=True)

# DB_PATH = os.path.join(app.root_path, "users.db")

# # -----------------------------------------------------------
# # DATABASE SETUP
# # -----------------------------------------------------------
# def init_db():
#     conn = sqlite3.connect(DB_PATH)
#     c = conn.cursor()

#     # user table (email + password)
#     c.execute("""
#         CREATE TABLE IF NOT EXISTS users (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             email TEXT UNIQUE,
#             password TEXT
#         )
#     """)

#     # history table
#     c.execute("""
#         CREATE TABLE IF NOT EXISTS history (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             user_id INTEGER,
#             image_path TEXT,
#             density_path TEXT,
#             count REAL
#         )
#     """)

#     conn.commit()
#     conn.close()

# init_db()

# # -----------------------------------------------------------
# # LOGIN CHECK DECORATOR
# # -----------------------------------------------------------
# def login_required(f):
#     @wraps(f)
#     def secure(*args, **kwargs):
#         if "user_id" not in session:
#             return redirect(url_for("login"))
#         return f(*args, **kwargs)
#     return secure


# # -----------------------------------------------------------
# # ROUTES
# # -----------------------------------------------------------

# @app.route("/")
# def root():
#     # show login page by default
#     return redirect(url_for("login"))


# @app.route("/home")
# @login_required
# def home():
#     # show the index page; crowd_count=None so results area hidden initially
#     return render_template("index.html", crowd_count=None)


# # ---------------- LOGIN ----------------
# @app.route("/login", methods=["GET", "POST"])
# def login():
#     if request.method == "POST":
#         email = request.form.get("email")
#         password = request.form.get("password")

#         if not email or not password:
#             return render_template("login.html", error="Please enter email and password.")

#         conn = sqlite3.connect(DB_PATH)
#         c = conn.cursor()
#         c.execute("SELECT id FROM users WHERE email=? AND password=?", (email, password))
#         user = c.fetchone()
#         conn.close()

#         if user:
#             session["user_id"] = user[0]
#             return redirect(url_for("home"))
#         else:
#             return render_template("login.html", error="Invalid email or password.")

#     return render_template("login.html")


# # ---------------- SIGNUP ----------------
# @app.route("/signup", methods=["GET", "POST"])
# def signup():
#     if request.method == "POST":
#         email = request.form.get("email")
#         password = request.form.get("password")

#         if not email or not password:
#             return render_template("signup.html", error="All fields are required.")

#         conn = sqlite3.connect(DB_PATH)
#         c = conn.cursor()
#         try:
#             c.execute("INSERT INTO users(email, password) VALUES(?,?)", (email, password))
#             conn.commit()
#             conn.close()
#             return redirect(url_for("login"))
#         except sqlite3.IntegrityError:
#             conn.close()
#             return render_template("signup.html", error="Email already exists.")
#         except Exception:
#             conn.close()
#             return render_template("signup.html", error="Failed to create account.")

#     return render_template("signup.html")


# # ---------------- LOGOUT ----------------
# @app.route("/logout")
# def logout():
#     session.clear()
#     return redirect(url_for("login"))


# # -----------------------------------------------------------
# # PREDICT ROUTE
# # -----------------------------------------------------------

# # Load model once at startup (load_model in model_utils)
# model = None
# try:
#     model = load_model()
# except Exception as e:
#     # we'll attempt to reload at prediction time if model failed here
#     print("Warning: load_model failed at startup:", e)


# @app.route("/predict", methods=["POST"])
# @login_required
# def predict():
#     file = request.files.get("file")
#     if not file or file.filename == "":
#         flash("No file selected.")
#         return redirect(url_for("home"))

#     filename = secure_filename(file.filename)
#     unique_name = f"{uuid.uuid4().hex}_{filename}"
#     save_path = os.path.join(UPLOAD_FOLDER, unique_name)

#     try:
#         file.save(save_path)
#     except Exception as e:
#         flash(f"Failed to save uploaded file: {e}")
#         return redirect(url_for("home"))

#     # ensure model is loaded
#     global model
#     if model is None:
#         try:
#             model = load_model()
#         except Exception as e:
#             flash("Model load failed. Check server logs.")
#             return redirect(url_for("home"))

#     # predict
#     try:
#         # predict_density_map must return (count as float, relative_density_path like "density_maps/dens_xxx.png")
#         count, density_rel_path = predict_density_map(model, save_path)
#     except Exception as e:
#         flash(f"Prediction failed: {e}")
#         return redirect(url_for("home"))

#     # Save record to DB (store relative paths)
#     conn = sqlite3.connect(DB_PATH)
#     c = conn.cursor()
#     try:
#         c.execute(
#             "INSERT INTO history(user_id, image_path, density_path, count) VALUES (?,?,?,?)",
#             (session["user_id"], os.path.join("uploads", unique_name), density_rel_path, float(count))
#         )
#         conn.commit()
#     finally:
#         conn.close()

#     input_url = url_for("static", filename=os.path.join("uploads", unique_name))
#     density_url = url_for("static", filename=density_rel_path)

#     return render_template("index.html",
#                            crowd_count=int(round(max(0, float(count)))),
#                            input_image=input_url,
#                            density_image=density_url)


# # -----------------------------------------------------------
# # HISTORY PAGE
# # -----------------------------------------------------------
# @app.route("/history")
# @login_required
# def history():
#     conn = sqlite3.connect(DB_PATH)
#     c = conn.cursor()
#     c.execute("SELECT image_path, density_path, count FROM history WHERE user_id=?", (session["user_id"],))
#     data = c.fetchall()
#     conn.close()
#     # convert rows to list, render template expects list of tuples
#     return render_template("history.html", records=data)


# # -----------------------------------------------------------
# # RUN
# # -----------------------------------------------------------
# if __name__ == "__main__":
#     app.run(debug=True)




# from flask import Flask, render_template, request, redirect, url_for
# import os
# from werkzeug.utils import secure_filename
# from model_utils import load_model, predict_density_map
# import sqlite3

# app = Flask(__name__)
# app.config['UPLOAD_FOLDER'] = 'static/uploads'

# # Load CSRNet model
# model = load_model("E:\CrowdEstimation-master\CrowdEstimation-master\CSRNet\CSRnet-pytorch\weights\CSRNet_pretrained.pth", device="cpu")



# # ----------------------------
# #   CREATE HISTORY DATABASE
# # ----------------------------
# def init_db():
#     conn = sqlite3.connect("history.db")
#     cur = conn.cursor()
#     cur.execute("""
#         CREATE TABLE IF NOT EXISTS predictions (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             image_path TEXT,
#             density_path TEXT,
#             count REAL
#         )
#     """)
#     conn.commit()
#     conn.close()

# init_db()

# # --------------------------------
# #          HOME PAGE
# # --------------------------------
# @app.route("/")
# def home():
#     return render_template("index.html", crowd_count=None)

# # --------------------------------
# #            PREDICT
# # --------------------------------
# @app.route("/predict", methods=["POST"])
# def predict():
#     if "file" not in request.files:
#         return redirect(url_for('home'))

#     file = request.files["file"]
#     if file.filename == "":
#         return redirect(url_for('home'))

#     filename = secure_filename(file.filename)
#     save_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
#     file.save(save_path)

#     # RUN MODEL PREDICTION
#     count, density_rel_path = predict_density_map(model, save_path, device="cpu")

#     # Save history
#     conn = sqlite3.connect("history.db")
#     cur = conn.cursor()
#     cur.execute("INSERT INTO predictions (image_path, density_path, count) VALUES (?, ?, ?)",
#                 (save_path, "static/" + density_rel_path, count))
#     conn.commit()
#     conn.close()

#     return render_template(
#         "index.html",
#         crowd_count=int(count),
#         input_image="/" + save_path,
#         density_image="/static/" + density_rel_path
#     )

# # --------------------------------
# #            HISTORY
# # --------------------------------
# @app.route("/history")
# def history():
#     conn = sqlite3.connect("history.db")
#     cur = conn.cursor()
#     cur.execute("SELECT * FROM predictions ORDER BY id DESC")
#     rows = cur.fetchall()
#     conn.close()
#     return render_template("history.html", rows=rows)

# # --------------------------------
# #          RUN SERVER
# # --------------------------------
# if __name__ == "__main__":
#     os.makedirs("static/uploads", exist_ok=True)
#     os.makedirs("static/density_maps", exist_ok=True)
#     app.run(debug=True)




# # app.py
# from flask import Flask, render_template, request, redirect, url_for
# import os
# from werkzeug.utils import secure_filename
# from model_utils import load_model, predict_density_map

# import sqlite3

# app = Flask(__name__)
# app.config['UPLOAD_FOLDER'] = 'static/uploads'
# app.config['DENSITY_FOLDER'] = 'static/density_maps'

# # ensure folders exist
# os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
# os.makedirs(app.config['DENSITY_FOLDER'], exist_ok=True)

# # Load CSRNet model (tries default fallback locations)
# # If you want to specify an explicit path, pass it here:
# model = load_model(None, device="cpu")

# # ----------------------------
# #   CREATE HISTORY DATABASE
# # ----------------------------
# def init_db():
#     conn = sqlite3.connect("history.db")
#     cur = conn.cursor()
#     cur.execute("""
#         CREATE TABLE IF NOT EXISTS predictions (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             image_path TEXT,
#             density_path TEXT,
#             count REAL
#         )
#     """)
#     conn.commit()
#     conn.close()

# init_db()

# # --------------------------------
# #          HOME PAGE
# # --------------------------------
# @app.route("/")
# def home():
#     return render_template("index.html", crowd_count=None)

# # --------------------------------
# #            PREDICT
# # --------------------------------
# @app.route("/predict", methods=["POST"])
# def predict():
#     if "file" not in request.files:
#         return redirect(url_for('home'))

#     file = request.files["file"]
#     if file.filename == "":
#         return redirect(url_for('home'))

#     filename = secure_filename(file.filename)
#     save_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
#     file.save(save_path)

#     # RUN MODEL PREDICTION
#     count, density_rel_path = predict_density_map(model, save_path, device="cpu")

#     # Save history
#     conn = sqlite3.connect("history.db")
#     cur = conn.cursor()
#     cur.execute("INSERT INTO predictions (image_path, density_path, count) VALUES (?, ?, ?)",
#                 (save_path, os.path.join("static", density_rel_path), count))
#     conn.commit()
#     conn.close()

#     return render_template(
#         "index.html",
#         crowd_count=int(round(count)),
#         input_image="/" + save_path,
#         density_image="/" + os.path.join("static", density_rel_path)
#     )

# # --------------------------------
# #            HISTORY
# # --------------------------------
# @app.route("/history")
# def history():
#     conn = sqlite3.connect("history.db")
#     cur = conn.cursor()
#     cur.execute("SELECT * FROM predictions ORDER BY id DESC")
#     rows = cur.fetchall()
#     conn.close()
#     return render_template("history.html", rows=rows)

# # --------------------------------
# #          RUN SERVER
# # --------------------------------
# if __name__ == "__main__":
#     app.run(debug=True)





# app.py    working code 

# from flask import Flask, render_template, request, redirect, url_for
# import os
# from werkzeug.utils import secure_filename
# from model_utils import load_model, predict_density_map
# import sqlite3

# app = Flask(__name__)
# app.config['UPLOAD_FOLDER'] = 'static/uploads'
# app.config['DENSITY_FOLDER'] = 'static/density_maps'

# # ensure folders exist
# os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
# os.makedirs(app.config['DENSITY_FOLDER'], exist_ok=True)

# # Load model
# model = load_model(None, device="cpu")

# # ----------------------------
# #   CREATE HISTORY DATABASE
# # ----------------------------
# def init_db():
#     conn = sqlite3.connect("history.db")
#     cur = conn.cursor()
#     cur.execute("""
#         CREATE TABLE IF NOT EXISTS predictions (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             image_path TEXT,
#             density_path TEXT,
#             count REAL
#         )
#     """)
#     conn.commit()
#     conn.close()

# init_db()

# # --------------------------------
# #          HOME PAGE
# # --------------------------------
# @app.route("/")
# def home():
#     return render_template("index.html", crowd_count=None)

# # --------------------------------
# #            PREDICT
# # --------------------------------
# @app.route("/predict", methods=["POST"])
# def predict():
#     if "file" not in request.files:
#         return redirect(url_for('home'))

#     file = request.files["file"]
#     if file.filename == "":
#         return redirect(url_for('home'))

#     filename = secure_filename(file.filename)
#     input_image_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
#     file.save(input_image_path)

#     # density map filename
#     density_filename = "dens_" + filename.replace(".jpg", "").replace(".png", "") + ".png"
#     density_map_path = os.path.join(app.config["DENSITY_FOLDER"], density_filename)

#     # -------- CALL MODEL CORRECTLY ----------
#     count, density_rel_path = predict_density_map(
#         model,
#         input_image_path,     # input image
#         density_map_path,     # density map output file
#         device="cpu"
#     )
#     # -----------------------------------------

#     # Save history
#     conn = sqlite3.connect("history.db")
#     cur = conn.cursor()
#     cur.execute(
#         "INSERT INTO predictions (image_path, density_path, count) VALUES (?, ?, ?)",
#         (input_image_path, density_rel_path, count)
#     )
#     conn.commit()
#     conn.close()

#     return render_template(
#         "index.html",
#         crowd_count=int(round(count)),
#         input_image="/" + input_image_path,
#         density_image="/" + density_rel_path
#     )


# # --------------------------------
# #            HISTORY
# # --------------------------------
# @app.route("/history")
# def history():
#     conn = sqlite3.connect("history.db")
#     cur = conn.cursor()
#     cur.execute("SELECT * FROM predictions ORDER BY id DESC")
#     rows = cur.fetchall()
#     conn.close()
#     return render_template("history.html", rows=rows)


# # --------------------------------
# #          RUN SERVER
# # --------------------------------
# if __name__ == "__main__":
#     app.run(debug=True)




# working code finish here







# new code

# from flask import Flask, render_template, request, redirect, url_for, session
# import os
# import sqlite3
# from werkzeug.utils import secure_filename
# from model_utils import load_model, predict_density_map

# app = Flask(__name__)
# app.secret_key = "supersecret"

# app.config['UPLOAD_FOLDER'] = 'static/uploads'
# app.config['DENSITY_FOLDER'] = 'static/density_maps'

# os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
# os.makedirs(app.config['DENSITY_FOLDER'], exist_ok=True)

# model = load_model(None, device="cpu")


# # --------------------- USERS DB --------------------
# def init_user_db():
#     conn = sqlite3.connect("users.db")
#     cur = conn.cursor()
#     cur.execute("""
#         CREATE TABLE IF NOT EXISTS users(
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             username TEXT UNIQUE,
#             password TEXT
#         )
#     """)
#     conn.commit()
#     conn.close()

# init_user_db()


# # --------------------- LOGIN REQUIRED --------------------
# def login_required(f):
#     def wrapper(*args, **kwargs):
#         if "user" not in session:
#             return redirect("/login")
#         return f(*args, **kwargs)
#     return wrapper


# # --------------------- AUTH --------------------
# @app.route("/login", methods=["GET", "POST"])
# def login():
#     if request.method == "POST":
#         u = request.form["username"]
#         p = request.form["password"]

#         conn = sqlite3.connect("users.db")
#         cur = conn.cursor()
#         cur.execute("SELECT * FROM users WHERE username=? AND password=?", (u, p))
#         user = cur.fetchone()
#         conn.close()

#         if user:
#             session["user"] = u
#             return redirect("/")
#         else:
#             return "Invalid Login"

#     return render_template("login.html")


# @app.route("/signup", methods=["GET", "POST"])
# def signup():
#     if request.method == "POST":
#         u = request.form["username"]
#         p = request.form["password"]

#         conn = sqlite3.connect("users.db")
#         cur = conn.cursor()
#         try:
#             cur.execute("INSERT INTO users(username,password) VALUES(?,?)", (u,p))
#             conn.commit()
#             conn.close()
#             return redirect("/login")
#         except:
#             return "Username already exists"

#     return render_template("signup.html")


# @app.route("/logout")
# def logout():
#     session.clear()
#     return redirect("/login")


# # --------------------- HOME --------------------
# @app.route("/")
# @login_required
# def home():
#     return render_template("index.html", crowd_count=None)


# # --------------------- PREDICT --------------------
# @app.route("/predict", methods=["POST"])
# @login_required
# def predict():
#     file = request.files["file"]
#     filename = secure_filename(file.filename)
#     img_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
#     file.save(img_path)

#     density_name = "dens_" + filename + ".png"
#     density_path = os.path.join(app.config["DENSITY_FOLDER"], density_name)

#     count, saved_path = predict_density_map(model, img_path, density_path)

#     return render_template(
#         "index.html",
#         crowd_count=int(count),
#         input_image="/" + img_path,
#         density_image="/" + saved_path
#     )


# # --------------------- HISTORY --------------------
# @app.route("/history")
# @login_required
# def history():
#     conn = sqlite3.connect("history.db")
#     cur = conn.cursor()
#     cur.execute("SELECT * FROM predictions ORDER BY id DESC")
#     rows = cur.fetchall()
#     conn.close()
#     return render_template("history.html", rows=rows)


# app.run(debug=True)
































# app.py
from flask import Flask, render_template, request, redirect, url_for, session
import os
import sqlite3
from functools import wraps
from werkzeug.utils import secure_filename
from model_utils import load_model, predict_density_map

app = Flask(__name__)
app.secret_key = "replace_this_with_a_real_secret"  # change in production

# folders
app.config['UPLOAD_FOLDER'] = os.path.join("static", "uploads")
app.config['DENSITY_FOLDER'] = os.path.join("static", "density_maps")

os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['DENSITY_FOLDER'], exist_ok=True)

# load model (will search default locations inside model_utils)
model = load_model(None, device="cpu")


# ----------------------------
# Database init
# ----------------------------
def init_db():
    conn = sqlite3.connect("app_data.db")
    cur = conn.cursor()

    # users table
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE,
            password TEXT
        )
    """)

    # predictions table
    cur.execute("""
        CREATE TABLE IF NOT EXISTS predictions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            image_path TEXT,
            density_path TEXT,
            count REAL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conn.commit()
    conn.close()

init_db()


# ----------------------------
# helpers
# ----------------------------
def login_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if "user" not in session:
            return redirect("/login")
        return fn(*args, **kwargs)
    return wrapper


def save_prediction_record(image_webpath, density_webpath, count):
    conn = sqlite3.connect("app_data.db")
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO predictions (image_path, density_path, count) VALUES (?, ?, ?)",
        (image_webpath, density_webpath, float(count))
    )
    conn.commit()
    conn.close()


# ----------------------------
# Routes: auth
# ----------------------------
@app.route("/", methods=["GET"])
def root():
    # redirect to login page by default
    return redirect("/login")


@app.route("/login", methods=["GET", "POST"])
def login():
    # Accept either 'username' or 'email' field in form
    if request.method == "POST":
        # use get to avoid KeyError
        uname = request.form.get("username") or request.form.get("email")
        pwd = request.form.get("password")

        if not uname or not pwd:
            return render_template("login.html", error="Please enter username/email and password.")

        conn = sqlite3.connect("app_data.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM users WHERE username=? AND password=?", (uname, pwd))
        user = cur.fetchone()
        conn.close()

        if user:
            session["user"] = uname
            return redirect("/index")
        else:
            return render_template("login.html", error="Invalid credentials. Try again.")

    return render_template("login.html")


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        uname = request.form.get("username") or request.form.get("email")
        pwd = request.form.get("password")

        if not uname or not pwd:
            return render_template("signup.html", error="Please choose a username/email and password.")

        conn = sqlite3.connect("app_data.db")
        cur = conn.cursor()
        try:
            cur.execute("INSERT INTO users (username, password) VALUES (?, ?)", (uname, pwd))
            conn.commit()
            conn.close()
            return redirect("/login")
        except Exception as e:
            conn.close()
            return render_template("signup.html", error="Username already exists or invalid input.")

    return render_template("signup.html")


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")


# ----------------------------
# Index / Upload (protected)
# ----------------------------
@app.route("/index", methods=["GET"])
@login_required
def index():
    # show upload form
    return render_template("index.html", crowd_count=None)


# ----------------------------
# Predict (protected)
# ----------------------------
@app.route("/predict", methods=["POST"])
@login_required
def predict():
    if "file" not in request.files:
        return redirect("/index")

    file = request.files["file"]
    if file.filename == "":
        return redirect("/index")

    # save uploaded image
    filename = secure_filename(file.filename)
    input_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(input_path)

    # build density output path (static/density_maps/dens_<filename>.png)
    base, _ = os.path.splitext(filename)
    density_name = f"dens_{base}.png"
    density_path = os.path.join(app.config['DENSITY_FOLDER'], density_name)

    # call model util (it will save density image to density_path)
    try:
        count, saved_path = predict_density_map(model, input_path, density_path, device="cpu")
    except Exception as e:
        # if model fails, return error page or render index with message
        return render_template("index.html", crowd_count=None, error=f"Model error: {e}")

    # saved_path may be absolute or relative; convert to web path starting with '/'
    # we constructed density_path using app.config so saved_path usually equals density_path
    web_input = "/" + input_path.replace("\\", "/")
    web_density = "/" + density_path.replace("\\", "/")

    # save to DB (store web paths)
    save_prediction_record(web_input, web_density, count)

    return render_template("index.html",
                           crowd_count=int(round(count)),
                           input_image=web_input,
                           density_image=web_density)


# ----------------------------
# History (protected)
# ----------------------------
@app.route("/history", methods=["GET"])
@login_required
def history():
    conn = sqlite3.connect("app_data.db")
    cur = conn.cursor()
    cur.execute("SELECT id, image_path, density_path, count, created_at FROM predictions ORDER BY id DESC")
    rows = cur.fetchall()
    conn.close()
    # rows: list of tuples
    return render_template("history.html", rows=rows)


# ----------------------------
# Run
# ----------------------------
if __name__ == "__main__":
    app.run(debug=True)
