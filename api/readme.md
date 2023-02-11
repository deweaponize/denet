# Application Programing Layer(API)
contains two api endpoint and a documentation and testing endpoint

## API endpoint
both endpoint require api key a default key is provide with md5 hashing, default API key is `default`
1. build structure: `https://localhost/fetch_script`
2. command: `https://localhost/command`

example of `build structure` endpoint
```json
{
  "key": "string",
  "command": "string"
}
```

example of `command` endpoint
```json
{
  "detail": [
    {
      "loc": [
        "string",
        0
      ],
      "msg": "string",
      "type": "string"
    }
  ]
}
```

default reference rsa are stored in `rsa` folder containing two key `public.key` and `private.key`

## private.key

```
-----BEGIN PRIVATE KEY-----
MIICdQIBADANBgkqhkiG9w0BAQEFAASCAl8wggJbAgEAAoGBALpijp9Hbpj9aZrc
PB+e4J1kedDJIr525aRX8PFhUfr0JnYv25daNtwzjdFtbyUWL36TU9qR0ibqvthI
34/sdST+GI5sd0TIeUTqCqWMZkTj0y1OXKqUGjwf4oTrLv07F9AmRUebef4w02m8
DlaIrAhBPTPf1a31m2CF7svu87LnAgMBAAECgYBpD9ExO4S+PGpg3rANavNWBSMd
a6NoFYFQ6Dlq9t7NRP7BNCzl3fZ6nZzdZoB2OVFAWi+0TupVAZHePQW4DSPiZK80
xE838sRFMcK+N7l8b7QR/uIwcseDiTR6kyB/pkwoBswPCqpJT4CN5MAZzuSADEN0
/6gE3FMlfIbBpjF/UQJBAPK6HLdLg11Vb7sLyLApNZQeA5LExAQGeepsPyI7iSZJ
DN43DXeOT3/Shg4ZoM66ekQSw7CScKz2YB3U1pwGykMCQQDEk7lg/O+ndI0V/ktt
vP8PSO+Ovhae/YaUe6pd1jtq+VLDTt6GCYIiZ0Ki3kf+SG8JBOXUq2PzFuMN6mCQ
CcSNAkA4Y2YyateMwkFfqcAotJoe284mtZF4Ae0muZj9IemdvFDB+vYk9Smg306H
Tgrem9G1qMpPZeXJOL9hjsWAn88zAkAjtLF3bHobcJAv7oDE7g9mN1lMFDsHpgVL
8yp+4OrqA1+FGk5RCmkY1qjD7JwnFAEXIkyc1ITTItUbMfdYMm4BAkBe7iR4jj9h
sGXOzIuJzQ0WrQiIef937t9A5q4UVb/6rWFdHkZey9EP+SwMnDlkDWPNO54aRwPo
UsiiARtdqosK
-----END PRIVATE KEY-----

```

## public.key
```
-----BEGIN PUBLIC KEY-----
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQC6Yo6fR26Y/Wma3DwfnuCdZHnQ
ySK+duWkV/DxYVH69CZ2L9uXWjbcM43RbW8lFi9+k1PakdIm6r7YSN+P7HUk/hiO
bHdEyHlE6gqljGZE49MtTlyqlBo8H+KE6y79OxfQJkVHm3n+MNNpvA5WiKwIQT0z
39Wt9Ztghe7L7vOy5wIDAQAB
-----END PUBLIC KEY-----
```