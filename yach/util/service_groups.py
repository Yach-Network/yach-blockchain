from typing import KeysView, Generator

SERVICES_FOR_GROUP = {
    "all": "yach_harvester yach_timelord_launcher yach_timelord yach_farmer yach_full_node yach_wallet".split(),
    "node": "yach_full_node".split(),
    "harvester": "yach_harvester".split(),
    "farmer": "yach_harvester yach_farmer yach_full_node yach_wallet".split(),
    "farmer-no-wallet": "yach_harvester yach_farmer yach_full_node".split(),
    "farmer-only": "yach_farmer".split(),
    "timelord": "yach_timelord_launcher yach_timelord yach_full_node".split(),
    "timelord-only": "yach_timelord".split(),
    "timelord-launcher-only": "yach_timelord_launcher".split(),
    "wallet": "yach_wallet yach_full_node".split(),
    "wallet-only": "yach_wallet".split(),
    "introducer": "yach_introducer".split(),
    "simulator": "yach_full_node_simulator".split(),
}


def all_groups() -> KeysView[str]:
    return SERVICES_FOR_GROUP.keys()


def services_for_groups(groups) -> Generator[str, None, None]:
    for group in groups:
        for service in SERVICES_FOR_GROUP[group]:
            yield service


def validate_service(service: str) -> bool:
    return any(service in _ for _ in SERVICES_FOR_GROUP.values())
