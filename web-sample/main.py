from flask import Flask
import tomli

app = Flask(__name__)


@app.route('/config')
def config():
    with open("config.toml", mode="rb") as fp:
        sys_config = tomli.load(fp)
        return sys_config


if __name__ == '__main__':
    app.run(debug=True)
