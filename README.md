# key-validator

A tool validating the deployment from the blockchain config.

## Install

```commandline
pip install -r requirements.txt
```

## MCS server config list

The server config is in `test/chain.toml`

## Testing

- Test script

Testing script is under test folder

```shell
pytest test/key_validation_test.py
```

For Mac
```
python3 -m pytest test/key_validation_test.py
```

- Start a web server

You can also start your own server to test the functionality of the key \
validator.

The config is within the config.toml you can copy it to the chain.toml \
then switch the url in key_validation_test.py to your local port and run \
the pytest.

A sample web server is under web-sample, to start it, run the following command

```commandline
cd web-sample
python -m web-sample/main.py
```