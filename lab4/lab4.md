# Hackthebox

## TIER 0

### Meow

1. What does the acronym VM stand for?  
   Virtual Machine
2. What tool do we use to interact with the operating system in order to issue commands via the command line, such as 
   the one to start our VPN connection? It's also known as a console or shell.  
   Terminal
3. What service do we use to form our VPN connection into HTB labs?  
   openvpn
4. What is the abbreviated name for a 'tunnel interface' in the output of your VPN boot-up sequence output?  
   tun
5. What tool do we use to test our connection to the target with an ICMP echo request?  
   ping
6. What is the name of the most common tool for finding open ports on a target?  
   nmap
7. What service do we identify on port 23/tcp during our scans?  
   telnet
8. What username is able to log into the target over telnet with a blank password?  
   root
9. Submit root flag  
   b40abdfe23665f766f9c61ecba8a4c19
![img.png](images/img.png)
![img_1.png](images/img_1.png)
![img_2.png](images/img_2.png)

### Fawn

1. What does the 3-letter acronym FTP stand for?  
   File Transfer Protocol
2. Which port does the FTP service listen on usually?  
   21
3. What acronym is used for the secure version of FTP?  
   SFTP
4. What is the command we can use to send an ICMP echo request to test our connection to the target?  
   ping
5. From your scans, what version is FTP running on the target?  
   vsftpd 3.0.3
6. From your scans, what OS type is running on the target?  
   Unix
7. What is the command we need to run in order to display the 'ftp' client help menu?  
   ftp -h
8. What is username that is used over FTP when you want to log in without having an account?  
   anonymous
9. What is the response code we get for the FTP message 'Login successful'?   
   230
10. There are a couple of commands we can use to list the files and directories available on the FTP server.
    One is dir. What is the other that is a common way to list files on a Linux system.  
    ls
11. What is the command used to download the file we found on the FTP server?  
    get
12. Submit root flag  
    035db21c881520061c53e0536e44f815
![img_3.png](images/img_3.png)
![img_4.png](images/img_4.png)

### Dancing

1. What does the 3-letter acronym SMB stand for?  
   Server Message Block
2. What port does SMB use to operate at?  
   445
3. What is the service name for port 445 that came up in our Nmap scan?  
   microsoft-ds
4. What is the 'flag' or 'switch' we can use with the SMB tool to 'list' the contents of the share?  
   -L
5. How many shares are there on Dancing?  
   2
6. What is the name of the share we are able to access in the end with a blank password?  
   anonymous
7. What is the command we can use within the SMB shell to download the files we find?  
   get
8. Submit root flag  
   5f61c10dffbc77a704d76016a22f1664
![img_5.png](images/img_5.png)
![img_6.png](images/img_6.png)
![img_7.png](images/img_7.png)

### Redeemer

1. Which TCP port is open on the machine?  
   6379
2. Which service is running on the port that is open on the machine?  
   redis
3. What type of database is Redis? Choose from the following options: (i) In-memory Database, (ii) Traditional Database  
   In-memory Database
4. Which command-line utility is used to interact with the Redis server? Enter the program name you would enter into
   the terminal without any arguments.  
   redis-cli
5. Which flag is used with the Redis command-line utility to specify the hostname?  
   -h
6. Once connected to a Redis server, which command is used to obtain the information and statistics about the
   Redis server?  
   info
7. What is the version of the Redis server being used on the target machine?  
   5.0.7
8. Which command is used to select the desired database in Redis?  
   select
9. How many keys are present inside the database with index 0?  
   4
10. Which command is used to obtain all the keys in a database?  
    keys *
11. Submit root flag  
    03e1d2b376c37ab3f5319922053953eb
![img_8.png](images/img_8.png)
![img_9.png](images/img_9.png)
![img_10.png](images/img_10.png)
![img_11.png](images/img_11.png)

    
## TIER 1

### Appointment

1. What does the acronym SQL stand for?  
   Structured Query Language
2. What is one of the most common type of SQL vulnerabilities?  
   SQL Injection
3. What does PII stand for?  
   Personally Identifiable Information
4. What does the OWASP Top 10 list name the classification for this vulnerability?  
   A03:2021-Injection
5. What service and version are running on port 80 of the target?  
   Apache httpd 2.4.38 ((Debian))
6. What is the standard port used for the HTTPS protocol?  
   443
7. What is one luck-based method of exploiting login pages?  
   brute-forcing
8. What is a folder called in web-application terminology?  
   directory
9. What response code is given for "Not Found" errors?  
   404
10. What switch do we use with Gobuster to specify we're looking to discover directories, and not subdomains?  
    dir
11. What symbol do we use to comment out parts of the code?  
    #
12. Submit root flag  
    e3d0796d002a446c0e622226f42e9672
![img_12.png](images/img_12.png)
![img_13.png](images/img_13.png)
![img_14.png](images/img_14.png)


### Sequel

1. What does the acronym SQL stand for?  
   Structured Query Language
2. During our scan, which port running mysql do we find?  
   3306
3. What community-developed MySQL version is the target running?  
   MariaDB
4. What switch do we need to use in order to specify a login username for the MySQL service?  
   -u
5. Which username allows us to log into MariaDB without providing a password?  
   root
6. What symbol can we use to specify within the query that we want to display everything inside a table?  
   *
7. What symbol do we need to end each query with?  
   ;
8. Submit root flag  
   7b4bec00d1a39e3dd4e021ec3d915da8
![img_15.png](images/img_15.png)
![img_16.png](images/img_16.png)


### Crocodile

1. What nmap scanning switch employs the use of default scripts during a scan?  
   -sC
2. What service version is found to be running on port 21?  
   vsftpd 3.0.3
3. What FTP code is returned to us for the "Anonymous FTP login allowed" message?  
   230
4. What command can we use to download the files we find on the FTP server?  
   get
5. What is one of the higher-privilege sounding usernames in the list we retrieved?  
   admin
6. What version of Apache HTTP Server is running on the target host?  
   2.4.41
7. What is the name of a handy web site analysis plug-in we can install in our browser?  
   Burp Suite
8. What switch can we use with gobuster to specify we are looking for specific filetypes?  
   -x
9. What file have we found that can provide us a foothold on the target?  
   login.php
10. Submit root flag  
    c7110277ac44d78b6a9fff2232434d16
![img_17.png](images/img_17.png)
![img_18.png](images/img_18.png)
![img_19.png](images/img_19.png)
![img_20.png](images/img_20.png)
![img_21.png](images/img_21.png)


### Responder

1. When visiting the web service using the IP address, what is the domain that we are being redirected to?  
   unika.htb
2. Which scripting language is being used on the server to generate webpages?  
   PHP
3. What is the name of the URL parameter which is used to load different language versions of the webpage?  
   page
4. Which of the following values for the `page` parameter would be an example of exploiting a Local File Include (LFI)
   vulnerability: "french.html", "//10.10.14.6/somefile", "../../../../../../../../windows/system32/drivers/etc/hosts",
   "minikatz.exe"  
    ../../../../../../../../windows/system32/drivers/etc/hosts
5. Which of the following values for the `page` parameter would be an example of exploiting a Remote File Include (RFI)
   vulnerability: "french.html", "//10.10.14.6/somefile", "../../../../../../../../windows/system32/drivers/etc/hosts",
   "minikatz.exe"  
   //10.10.14.6/somefile
6. What does NTLM stand for? 
   New Technology Lan Manager
7. Which flag do we use in the Responder utility to specify the network interface?  
   -I
8. There are several tools that take a NetNTLMv2 challenge/response and try millions of passwords to see if any of them
   generate the same response. One such tool is often referred to as `john`, but the full name is what?.  
   John The Ripper
9. What is the password for the administrator user?  
   badminton
10. We'll use a Windows service (i.e. running on the box) to remotely access the Responder machine using the password
    we recovered. What port TCP does it listen on?  
    5985
11. Submit root flag  
    ea81b7afddd03efaa0945333ed147fac
![img_22.png](images/img_22.png)
![img_23.png](images/img_23.png)
![img_24.png](images/img_24.png)
![img_25.png](images/img_25.png)
![img_26.png](images/img_26.png)
![img_27.png](images/img_27.png)
![img_28.png](images/img_28.png)
![img_29.png](images/img_29.png)


### Three

1. How many TCP ports are open?  
   2
2. What is the domain of the email address provided in the "Contact" section of the website?  
   thetoppers.htb
3. In the absence of a DNS server, which Linux file can we use to resolve hostnames to IP addresses in order to be able
   to access the websites that point to those hostnames?  
   /etc/hosts
4. Which sub-domain is discovered during further enumeration?  
   s3.thetoppers.htb
5. Which service is running on the discovered sub-domain?  
   Amazon S3
6. Which command line utility can be used to interact with the service running on the discovered sub-domain?  
   awscli
7. Which command is used to set up the AWS CLI installation?  
   aws configure
8. What is the command used by the above utility to list all of the S3 buckets?  
   aws s3 ls
9. This server is configured to run files written in what web scripting language?  
   PHP
10. Submit root flag  
    a980d99281a28d638ac68b9bf9453c2b
![img_30.png](images/img_30.png)
![img_31.png](images/img_31.png)
![img_32.png](images/img_32.png)
![img_33.png](images/img_33.png)
![img_34.png](images/img_34.png)
![img_35.png](images/img_35.png)
![img_36.png](images/img_36.png)
![img_37.png](images/img_37.png)





