from substrateinterface import SubstrateInterface

substrate = SubstrateInterface(
    url="wss://kusama-rpc.polkadot.io/",
    address_type=2,
    type_registry_preset='kusama'
)

print(substrate.get_block_number)