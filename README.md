# key-validator

A tool validating the deployment from the blockchain config.

## Install

```commandline
pip install -r requirements.txt
```

## MCS server config list

The server config is in `test/chain.toml`

## Testing

- Start a web server

A sample web server is under web-sample, to start it, run the following command

```commandline
cd web-sample
python -m web-sample/main.py
```

- Test script

Testing script is under test folder

```shell
pytest 
```
