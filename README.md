# pyUT2WebAdmin
UT2004 (and UT2003?) WebAdmin command-line access through Python 2.7

## Usage
This does very little more than POST directly to the webadmin command line, taking care of the http stuff for you. 

WebAdminAccess.console(command_to_send) returns a HTTPResponse object, received as a response to the POST. 

```
with WebAdminAccess("192.168.1.100", 80, "Username:Password") as w:
    print w.console("say Hello, world!").reason
```
```
OK
```

## A Note on Security
Yes, your password for WebAdmin is sent in plaintext over the Internet. The game was written in 2004, strong HTTPS security was not really a concern of Epic Games. It's not my problem, and this isn't less secure than normal WebAdmin access. 
