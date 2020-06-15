pubkey = """-----BEGIN PUBLIC KEY-----
MIGeMA0GCSqGSIb3DQEBAQUAA4GMADCBiAKBgH23dqh1pHqv6AQ8HYz7I1L+owEv
hMEbGgj/ldsTXcVZAoNlMTqrrMFikczJP5ixj7sXymbp1yqblmWVOZXSjCGjad/9
x9tjZsuuqmSg8cgtgKlevbr9rrZn7lpd9/GWEA9w+njTI3fUaXGKZKtMPM0HGkH5
YpMRac/7jV+Y3gGvAgMBAAE=
-----END PUBLIC KEY-----"""

privkey = """-----BEGIN RSA PRIVATE KEY-----
MIICWgIBAAKBgH23dqh1pHqv6AQ8HYz7I1L+owEvhMEbGgj/ldsTXcVZAoNlMTqr
rMFikczJP5ixj7sXymbp1yqblmWVOZXSjCGjad/9x9tjZsuuqmSg8cgtgKlevbr9
rrZn7lpd9/GWEA9w+njTI3fUaXGKZKtMPM0HGkH5YpMRac/7jV+Y3gGvAgMBAAEC
gYB3VSwEMk9jyhAh3PJr/YOFZ4JRQMryBojLG9kisBpllt0k3mxBde4xTyB41FtS
1NFLVgThdXyxzCiR2nlj9wzeGIVAQaIZzgKWo2Rsw/Zi5i92KGgIUjKYNktL72wV
h7uV9v1d0pihpbQ9+RaXz1o1adU3OsFjpL+kuD8Ls/ffWQJBALrLsl7s/nSBv+rT
7stw6exZ6aa0cyYu6P1B7YEZFM16RUdeVVroi/pqD+CF2nArai+LX9ne5H5yirOw
C6Q/brsCQQCsStW0aJ7JG5G0jtGd743hAvISkamLALuZN9AhPFJw2oGBy+M1HCru
dFol3bWUmY/UKzSj8ifnp5uAg8tsNjudAkBlndJXGY4DS2JgGRLa0X4v+WnGKnxJ
1VMiEu9lP4O1lEKD5KmCXudnPrOMbMS8KKIHY0atezfKIf2aaraqj2dpAkBn8Kmm
MeuBJdmsFPEOl8N/OJizbR7cVe/XCl3Mfyi5Hok8tbT3iGu5+YWdDHkMEew8MmiK
c39xeKMOT/Q77yfdAkBzXH9L13Apv/ve6bBCO7uZE+4DNNWKQ1wXxDNsNobr1M0c
tFAkfWU/WvEDTSo0B1t/TI2MhCwtJaLnTnmZkUgM
-----END RSA PRIVATE KEY-----"""

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5 as Cipher_PKCS1_v1_5

msg = "code"
print("text : ", msg)
keyPub = RSA.import_key(pubkey)

cipher = Cipher_PKCS1_v1_5.new(keyPub)
cipher_text = cipher.encrypt(msg.encode())
print("cipher text : ", cipher_text)

keyPriv = RSA.import_key(privkey)
cipher = Cipher_PKCS1_v1_5.new(keyPriv)
decrypt_text = cipher.decrypt(cipher_text, None).decode()
print("Decrypt text : ", decrypt_text)