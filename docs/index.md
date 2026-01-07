# k3awssign

[![Action-CI](https://github.com/pykit3/k3awssign/actions/workflows/python-package.yml/badge.svg)](https://github.com/pykit3/k3awssign/actions/workflows/python-package.yml)
[![Documentation Status](https://readthedocs.org/projects/k3awssign/badge/?version=stable)](https://k3awssign.readthedocs.io/en/stable/?badge=stable)
[![Package](https://img.shields.io/pypi/pyversions/k3awssign)](https://pypi.org/project/k3awssign)

A python lib for adding AWS signature version 4 to requests.

k3awssign is a component of [pykit3](https://github.com/pykit3) project: a python3 toolkit set.

## Installation

```bash
pip install k3awssign
```

## Quick Start

```python
import k3awssign

access_key = 'your access key'
secret_key = 'your secret key'

signer = k3awssign.Signer(access_key, secret_key)

request = {
    'verb': 'PUT',
    'uri': '/test-bucket/test-key',
    'headers': {
        'Host': 'bscstorage.com',
        'Content-Length': 7,
    },
    'body': 'bla bla',
}

signer.add_auth(request, sign_payload=True)
# request['headers'] now contains AWS signature headers
```

## API Reference

::: k3awssign

## License

The MIT License (MIT) - Copyright (c) 2015 Zhang Yanpo (张炎泼)
