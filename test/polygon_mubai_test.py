import pytest
import tomli
import requests

from test.Chain import Chain


@pytest.fixture
def chain_info():
    with open("test/chain.toml", mode="rb") as fp:
        chain_info = tomli.load(fp)
    return chain_info


@pytest.fixture
def server_config_info() -> Chain:
    r = requests.get('http://127.0.0.1:5000/config')
    data = r.json()
    server_config = Chain(data['environment'], network=data['network'],
                          payment_contract_address=data['payment_contract_address'],
                          signer_contract_address=data['signer_contract_address'])
    return server_config


# Need to test it polygon mumbai online matches the document defined in chain.toml
def test_mumbai_config(chain_info, server_config_info):
    print(chain_info)
    assert chain_info['environments']['staging']['network'] == server_config_info.network
