# experiment-compress-1M-text-as-qr-code
Can I compress 1M of text into something that can be parsed as a QR code?

```
$ openssl rand -out sample.txt -base64 $(( 2**20 ))
```
