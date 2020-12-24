from flask import Flask, make_response, render_template, request
import sqlite3
app = Flask(__name__)
sql = sqlite3.connect('example.db')

app.jinja_env.add_extension('pypugjs.ext.jinja.PyPugJSExtension')
app.debug = True

# テーブル初期操作
query = sql.cursor()
query.execute('''CREATE TABLE IF NOT EXISTS `log`(
	`id` INTEGER PRIMARY KEY AUTOINCREMENT,
	`date` TEXT,
	`name` TEXT,
	`chat` TEXT
);''')

query.execute('''CREATE TABLE IF NOT EXISTS `user` (
	`id`	INTEGER PRIMARY KEY AUTOINCREMENT,
	`name`	TEXT NOT NULL,
	`password`	TEXT NOT NULL,
	`date_join`	TEXT NOT NULL
);''')


# 実行内容を反映
sql.commit()

@app.route('/')
def index():
	return render_template('index.pug')


@app.route('/login', methods=['POST'])
def login():
	print(request.form)
	return render_template('index.pug')

## おまじない
if __name__ == "__main__":
    app.run(debug=True)
