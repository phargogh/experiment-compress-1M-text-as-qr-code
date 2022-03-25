# experiment-compress-1M-text-as-qr-code
Can I compress 1M of text into something that can be parsed as a QR code?

```
$ openssl rand -out sample.txt -base64 $(( 2**20 ))
```

No.  A QR code can [only store about 3Kb of data](https://www.google.com/search?client=firefox-b-1-d&q=how+much+data+can+be+stored+in+a+qr+code).
