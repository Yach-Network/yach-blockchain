from setuptools import setup

dependencies = [
    "blspy==1.0.2",  # Signature library
    "yachvdf==1.0.1",  # timelord and vdf verification
    "yachbip158==1.0",  # bip158-style wallet filters
    "yachpos==1.0.2",  # proof of space
    "clvm==0.9.6",
    "clvm_rs==0.1.7",
    "clvm_tools==0.4.3",
    "aiohttp==3.7.4",  # HTTP server for full node rpc
    "aiosqlite==0.17.0",  # asyncio wrapper for sqlite, to store blocks
    "bitstring==3.1.7",  # Binary data management library
    "colorlog==5.0.1",  # Adds color to logs
    "concurrent-log-handler==0.9.19",  # Concurrently log and rotate logs
    "cryptography==3.4.7",  # Python cryptography library for TLS - keyring conflict
    "keyring==23.0.1",  # Store keys in MacOS Keychain, Windows Credential Locker
    "keyrings.cryptfile==1.3.4",  # Secure storage for keys on Linux (Will be replaced)
    #  "keyrings.cryptfile==1.3.8",  # Secure storage for keys on Linux (Will be replaced)
    #  See https://github.com/frispete/keyrings.cryptfile/issues/15
    "PyYAML==5.4.1",  # Used for config file format
    "setproctitle==1.2.2",  # Gives the yach processes readable names
    "sortedcontainers==2.3.0",  # For maintaining sorted mempools
    "websockets==8.1.0",  # For use in wallet RPC and electron UI
    "click==7.1.2",  # For the CLI
    "dnspython==2.1.0",  # Query DNS seeds
]

upnp_dependencies = [
    "miniupnpc==2.1",  # Allows users to open ports on their router
]

dev_dependencies = [
    "pytest",
    "pytest-asyncio",
    "flake8",
    "mypy",
    "black",
    "aiohttp_cors",  # For blackd
    "ipython",  # For asyncio debugging
]

kwargs = dict(
    name="yach-blockchain",
    author="Mariano Sorgente",
    author_email="mariano@yach.net",
    description="Yach blockchain full node, farmer, timelord, and wallet.",
    url="https://yach.net/",
    license="Apache License",
    python_requires=">=3.7, <4",
    keywords="yach blockchain node",
    install_requires=dependencies,
    setup_requires=["setuptools_scm"],
    extras_require=dict(
        uvloop=["uvloop"],
        dev=dev_dependencies,
        upnp=upnp_dependencies,
    ),
    packages=[
        "build_scripts",
        "yach",
        "yach.cmds",
        "yach.consensus",
        "yach.daemon",
        "yach.full_node",
        "yach.timelord",
        "yach.farmer",
        "yach.harvester",
        "yach.introducer",
        "yach.plotting",
        "yach.protocols",
        "yach.rpc",
        "yach.server",
        "yach.simulator",
        "yach.types.blockchain_format",
        "yach.types",
        "yach.util",
        "yach.wallet",
        "yach.wallet.puzzles",
        "yach.wallet.rl_wallet",
        "yach.wallet.cc_wallet",
        "yach.wallet.did_wallet",
        "yach.wallet.settings",
        "yach.wallet.trading",
        "yach.wallet.util",
        "yach.ssl",
        "mozilla-ca",
    ],
    entry_points={
        "console_scripts": [
            "yach = yach.cmds.yach:main",
            "yach_wallet = yach.server.start_wallet:main",
            "yach_full_node = yach.server.start_full_node:main",
            "yach_harvester = yach.server.start_harvester:main",
            "yach_farmer = yach.server.start_farmer:main",
            "yach_introducer = yach.server.start_introducer:main",
            "yach_timelord = yach.server.start_timelord:main",
            "yach_timelord_launcher = yach.timelord.timelord_launcher:main",
            "yach_full_node_simulator = yach.simulator.start_simulator:main",
        ]
    },
    package_data={
        "yach": ["pyinstaller.spec"],
        "yach.wallet.puzzles": ["*.clvm", "*.clvm.hex"],
        "yach.util": ["initial-*.yaml", "english.txt"],
        "yach.ssl": ["yach_ca.crt", "yach_ca.key", "dst_root_ca.pem"],
        "mozilla-ca": ["cacert.pem"],
    },
    use_scm_version={"fallback_version": "unknown-no-.git-directory"},
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    zip_safe=False,
)


if __name__ == "__main__":
    setup(**kwargs)
