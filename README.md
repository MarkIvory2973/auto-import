# Auto Import

Auto import subscription from providers.

## Installation

Clone this repository:

```bash
git clone https://github.com/MarkIvory2973/auto-import.git
```

## Usage

```bash
cd auto-import
docker compose up -d
```

## Ports

|Type||Description|Port|
|:-|:-|:-|:-|
|Server|Backend|Backend API to auto import subscription|8080|

## Providers

Supported providers:

|Name|URL|Format|
|:-|:-|:-|
|XFLTD|https://my.xfltd.org/#/login|http://127.0.0.1:8080/xfltd?email= `Email` [&password=]() `Password (Base64)`|
