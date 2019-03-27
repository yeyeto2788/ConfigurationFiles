# Atom configuration files

## How to install packages in ATOM
### Instructions:

In order to install packages in Atom open a terminal window and type: `apm install --packages-file Packages.txt`

## How to get the list of packages installed

`apm list --installed --bare > path/to/file`

## Add proxy setting to Atom

Create a file call `.apmrc` in the `~/.atom` directory with the following lines:
```
https-proxy=http://<IP>:<PORT> 314
http-proxy=http://<IP>:<PORT> 314
strict-ssl=false
```

