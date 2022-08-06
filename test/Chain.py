class Chain:
    environment = ''
    network = ""
    payment_contract_address = 0
    signer_contract_address = ""

    def __init__(self, environment, network, payment_contract_address, signer_contract_address):
        self.environment = environment
        self.network = network
        self.payment_contract_address = payment_contract_address
        self.signer_contract_address = signer_contract_address

    def get_network(self):
        return self.network

    def __str__(self):
        return "network: %s, environment: %s " % (self.network, self.environment)


if __name__ == "__main__":
    polygon = Chain("testnet", 'polygon.mumai', '0x00000000', '0x00000')
    print(polygon)
