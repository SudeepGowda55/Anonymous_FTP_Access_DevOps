from ftplib import FTP

def scan_host(hostname):
    try:
        ftp = FTP(hostname)
        ftp.login('anonymous')
        print(str(hostname) + " This FTP Server is having Anonymous Access")
    except Exception:
         print(str(hostname) + " This FTP Server is NOT having Anonymous Access")

if __name__ == "__main__":
    host_ip = input("Please Enter the host ip address : ")
    scan_host(host_ip)

#128.148.32.111