from itertools import chain
import pytest
import tomli
import requests

from test.Chain import Chain

url_list = ['https://calibration-mcs-api.filswan.com', 'https://calibration-mcs-bsc.filswan.com']

@pytest.fixture
def chain_info():
    with open("test/chain.toml", mode="rb") as fp:
        chain_info = tomli.load(fp)
    return chain_info


@pytest.fixture
def server_config_info() -> Chain:
    server_config = []

    for url in url_list:
        r = requests.get(url+'/api/v1/common/system/params')
        response = r.json()
        data = response['data']
        print(data)
        server_config.append(Chain(url, network=data['chain_name'],
                            payment_contract_address=data['payment_contract_address'],
                            signer_contract_address=data['dao_contract_address']))
    return server_config


# Need to test it polygon mumbai online matches the document defined in chain.toml
def test_mumbai_config(chain_info, server_config_info):
    keys = list(chain_info['environments'].keys())
    n=0
    for server in server_config_info:
        print(chain_info)
        assert chain_info['environments'][keys[n]]['network'] == server.network
        assert chain_info['environments'][keys[n]]['payment_contract_address'] == server.payment_contract_address
        assert chain_info['environments'][keys[n]]['signer_contract_address'] == server.signer_contract_address
        n+=1

# Test if addresses and networks are unique (no reused addresses)
def test_address_uniqueness(chain_info):
    network = []
    payment_address = []
    signer_address = []
    print(chain_info)
    for env in chain_info['environments']:
        print(env)
        network.append(chain_info['environments'][env]['network'])
        payment_address.append(chain_info['environments'][env]['payment_contract_address'])
        signer_address.append(chain_info['environments'][env]['signer_contract_address'])
    assert not any(network.count(x) > 1 for x in network)
    assert not any(payment_address.count(x) > 1 for x in payment_address)
    assert not any(signer_address.count(x) > 1 for x in signer_address)