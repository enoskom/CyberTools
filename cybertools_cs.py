from colorama import Fore, Style, init

init(autoreset=True)

def print_cheat_sheet(title, cheat_sheet):
    print(f"{Fore.RED}\n{title} Cheat Sheet:{Style.RESET_ALL}")
    print(f"{Fore.WHITE}{'Komut':<25} {'Açıklama':<70} {'Örnek'}{Style.RESET_ALL}")
    print(f"{Fore.WHITE}{'-'*25} {'-'*70} {'-'*30}{Style.RESET_ALL}")
    for command, (description, example) in cheat_sheet.items():
        print(f"{Fore.WHITE}{command:<25} {Fore.GREEN}{description:<70} {Fore.WHITE}{example}{Style.RESET_ALL}")

def nmap_cheat_sheet():
    cheat_sheet = {
        "nmap": ("Ağ keşif ve güvenlik tarayıcısıdır.", "Örnek: nmap -sS -p 22,80 192.168.1.1"),
        "-sS": ("SYN taraması yapar.", "Örnek: nmap -sS 192.168.1.1"),
        "-sT": ("TCP bağlantı taraması yapar.", "Örnek: nmap -sT 192.168.1.1"),
        "-sU": ("UDP taraması yapar.", "Örnek: nmap -sU 192.168.1.1"),
        "-p": ("Belirli portları tarar.", "Örnek: nmap -p 22,80 192.168.1.1"),
        "--open": ("Sadece açık portları gösterir.", "Örnek: nmap --open 192.168.1.1"),
        "-A": ("Ağ keşfi ve OS tespiti yapar.", "Örnek: nmap -A 192.168.1.1"),
        "-O": ("İşletim sistemini belirlemeye çalışır.", "Örnek: nmap -O 192.168.1.1"),
        "-v": ("Ayrıntılı çıktı alır.", "Örnek: nmap -v 192.168.1.1"),
        "-Pn": ("Canlı kontrol etmeden tarama yapar.", "Örnek: nmap -Pn 192.168.1.1"),
        "--script": ("Nmap script motorunu kullanır.", "Örnek: nmap --script http-methods 192.168.1.1"),
        "-oN": ("Çıktıyı normal formatta kaydeder.", "Örnek: nmap -oN output.txt 192.168.1.1"),
        "-oX": ("Çıktıyı XML formatında kaydeder.", "Örnek: nmap -oX output.xml 192.168.1.1"),
        "--help": ("Yardım menüsünü gösterir.", "Örnek: nmap --help")
    }
    print_cheat_sheet("Nmap", cheat_sheet)

def nikto_cheat_sheet():
    cheat_sheet = {
        "nikto": ("Web sunucularını tarar.", "Örnek: nikto -h http://example.com"),
        "-h": ("Hedef URL'yi belirtir.", "Örnek: nikto -h http://example.com"),
        "-p": ("Belirli bir portu tarar.", "Örnek: nikto -h http://example.com -p 8080"),
        "-Tuning": ("Tarama ayarlarını belirtir.", "Örnek: nikto -h http://example.com -Tuning 2"),
        "-o": ("Çıktıyı bir dosyaya kaydeder.", "Örnek: nikto -h http://example.com -o output.txt"),
        "-Format": ("Çıktı formatını belirtir.", "Örnek: nikto -h http://example.com -Format html"),
        "-e": ("Belirli bir URL'yi hariç tutar.", "Örnek: nikto -h http://example.com -e /path/to/exclude"),
        "-no404": ("404 hatalarını hariç tutar.", "Örnek: nikto -h http://example.com -no404"),
        "--update": ("Nikto'yu günceller.", "Örnek: nikto --update"),
        "--version": ("Nikto versiyonunu gösterir.", "Örnek: nikto --version"),
        "--help": ("Yardım menüsünü gösterir.", "Örnek: nikto --help")
    }
    print_cheat_sheet("Nikto", cheat_sheet)

def sqlmap_cheat_sheet():
    cheat_sheet = {
        "sqlmap": ("SQL enjeksiyon ve veritabanı alımı için kullanılır.", "Örnek: sqlmap -u 'http://example.com?id=1'"),
        "-u": ("Hedef URL'yi belirtir.", "Örnek: sqlmap -u 'http://example.com?id=1'"),
        "--data": ("POST verisini belirtir.", "Örnek: sqlmap -u 'http://example.com' --data='id=1'"),
        "--cookie": ("Cookie bilgilerini belirtir.", "Örnek: sqlmap -u 'http://example.com' --cookie='PHPSESSID=abcd'"),
        "--dbs": ("Veritabanı isimlerini listelemek için kullanılır.", "Örnek: sqlmap -u 'http://example.com?id=1' --dbs"),
        "--tables": ("Belirtilen veritabanındaki tabloları listeler.", "Örnek: sqlmap -u 'http://example.com?id=1' --dbs --tables"),
        "--columns": ("Belirtilen tabloda sütunları listeler.", "Örnek: sqlmap -u 'http://example.com?id=1' --tables --columns"),
        "--dump": ("Veritabanındaki verileri almak için kullanılır.", "Örnek: sqlmap -u 'http://example.com?id=1' --dump"),
        "--level": ("Tarama seviyesini belirler (1-5).", "Örnek: sqlmap -u 'http://example.com?id=1' --level=5"),
        "--risk": ("Risk seviyesini belirler (0-3).", "Örnek: sqlmap -u 'http://example.com?id=1' --risk=3"),
        "--help": ("Yardım menüsünü gösterir.", "Örnek: sqlmap --help"),
        "--tor": ("Tor üzerinden tarama yapar.", "Örnek: sqlmap -u 'http://example.com?id=1' --tor")
    }
    print_cheat_sheet("SQLMap", cheat_sheet)

def burpsuite_cheat_sheet():
    cheat_sheet = {
        "burpsuite": ("Web uygulamaları güvenliği için platformdur.", "Örnek: java -jar burpsuite.jar"),
        "-p": ("Proxy ayarlarını belirtir.", "Örnek: burpsuite -p 8080"),
        "--scan": ("Tarama başlatır.", "Örnek: burpsuite --scan http://example.com"),
        "--repeater": ("HTTP isteklerini yeniden göndermek için kullanılır.", "Örnek: burpsuite --repeater"),
        "--intruder": ("Zorlamalar için istekleri gönderir.", "Örnek: burpsuite --intruder"),
        "--help": ("Yardım menüsünü gösterir.", "Örnek: burpsuite --help")
    }
    print_cheat_sheet("Burp Suite", cheat_sheet)

def metasploit_cheat_sheet():
    cheat_sheet = {
        "metasploit": ("Güvenlik açığı istismarları için araçtır.", "Örnek: msfconsole"),
        "msfconsole": ("Metasploit konsolunu başlatır.", "Örnek: msfconsole"),
        "use": ("Belirli bir modülü kullanmak için.", "Örnek: use exploit/windows/smb/ms17_010_eternalblue"),
        "search": ("Modülleri aramak için.", "Örnek: search smb"),
        "exploit": ("Belirli bir açığı istismar etmek için.", "Örnek: exploit"),
        "sessions": ("Açık oturumları görüntülemek için.", "Örnek: sessions"),
        "exit": ("Konsoldan çıkmak için.", "Örnek: exit")
    }
    print_cheat_sheet("Metasploit", cheat_sheet)

def wireshark_cheat_sheet():
    cheat_sheet = {
        "wireshark": ("Ağ protokollerini analiz etmek için araçtır.", "Örnek: wireshark"),
        "display filters": ("Filtreleri görüntülemek için kullanılır.", "Örnek: http"),
        "capture filters": ("Ağ trafiğini filtrelemek için kullanılır.", "Örnek: tcp port 80"),
        "follow TCP stream": ("TCP akışını takip eder.", "Örnek: sağ tık -> Follow -> TCP Stream"),
        "export": ("Verileri dışa aktarmak için kullanılır.", "Örnek: File -> Export Specified Packets"),
        "statistics": ("İstatistikleri görüntülemek için.", "Örnek: Statistics -> Protocol Hierarchy")
    }
    print_cheat_sheet("Wireshark", cheat_sheet)

def dirb_cheat_sheet():
    cheat_sheet = {
        "dirb": ("DIRB, dizin ve dosya taraması için kullanılan bir araçtır.", "Örnek: dirb http://example.com"),
        "-u": ("Hedef URL'yi belirtir.", "Örnek: dirb -u http://example.com"),
        "-w": ("Kullanılacak kelime listesini belirtir.", "Örnek: dirb -w wordlist.txt http://example.com"),
        "-r": ("Dizinlerdeki geçerli yanıtları yeniden tarar.", "Örnek: dirb -r http://example.com"),
        "-o": ("Sonuçları bir dosyaya kaydeder.", "Örnek: dirb -o output.txt http://example.com"),
        "-t": ("Eşzamanlı istek sayısını ayarlar.", "Örnek: dirb -t 20 http://example.com"),
        "--help": ("Yardım menüsünü gösterir.", "Örnek: dirb --help")
    }
    print_cheat_sheet("DIRB", cheat_sheet)

def hydra_cheat_sheet():
    cheat_sheet = {
        "hydra": ("Hydra, parola kırma için kullanılan bir araçtır.", "Örnek: hydra"),
        "-l": ("Kullanıcı adını belirtir.", "Örnek: hydra -l admin"),
        "-L": ("Kullanıcı adı listesini belirtir.", "Örnek: hydra -L users.txt"),
        "-p": ("Parolayı belirtir.", "Örnek: hydra -p password"),
        "-P": ("Parola listesini belirtir.", "Örnek: hydra -P passwords.txt"),
        "-s": ("Hedefin portunu belirtir.", "Örnek: hydra -s 80"),
        "-v": ("Ayrıntılı çıktı almak için kullanılır.", "Örnek: hydra -v"),
        "-t": ("Eşzamanlı istek sayısını ayarlar.", "Örnek: hydra -t 4"),
        "--help": ("Yardım menüsünü gösterir.", "Örnek: hydra --help")
    }
    print_cheat_sheet("Hydra", cheat_sheet)

def john_the_ripper_cheat_sheet():
    cheat_sheet = {
        "john": ("John the Ripper, parola kırma için kullanılan bir araçtır.", "Örnek: john --wordlist=wordlist.txt hashes.txt"),
        "--wordlist": ("Kullanılacak kelime listesini belirtir.", "Örnek: john --wordlist=mylist.txt"),
        "--rules": ("Kelime listesi kurallarını uygular.", "Örnek: john --rules"),
        "--format": ("Kullanılacak dosya formatını belirtir.", "Örnek: john --format=raw-md5 hashes.txt"),
        "--show": ("Kırılan parolaları gösterir.", "Örnek: john --show hashes.txt"),
        "--status": ("Kırma işleminin durumunu gösterir.", "Örnek: john --status"),
        "--help": ("Yardım menüsünü gösterir.", "Örnek: john --help")
    }
    print_cheat_sheet("John the Ripper", cheat_sheet)

def nessus_cheat_sheet():
    cheat_sheet = {
        "nessus": ("Nessus, güvenlik tarama aracı olarak kullanılır.", "Örnek: nessus"),
        "--scan": ("Belirli bir tarama başlatır.", "Örnek: nessus --scan myscan"),
        "--targets": ("Tarama hedeflerini belirtir.", "Örnek: nessus --targets 192.168.1.1"),
        "--profile": ("Kullanılacak tarama profilini belirtir.", "Örnek: nessus --profile basic"),
        "--report": ("Tarama raporunu dışa aktarır.", "Örnek: nessus --report report.pdf"),
        "--help": ("Yardım menüsünü gösterir.", "Örnek: nessus --help")
    }
    print_cheat_sheet("Nessus", cheat_sheet)

def maltego_cheat_sheet():
    cheat_sheet = {
        "maltego": ("Maltego, veri keşif ve bağlantı analizi için kullanılan bir araçtır.", "Örnek: maltego"),
        "--import": ("Veri dosyasını içe aktarır.", "Örnek: maltego --import mydata.csv"),
        "--export": ("Veriyi dışa aktarır.", "Örnek: maltego --export mydata.xml"),
        "--help": ("Yardım menüsünü gösterir.", "Örnek: maltego --help")
    }
    print_cheat_sheet("Maltego", cheat_sheet)

def aircrack_ng_cheat_sheet():
    cheat_sheet = {
        "aircrack-ng": ("Aircrack-ng, WiFi ağlarının güvenliğini test etmek için kullanılan bir araçtır.", "Örnek: aircrack-ng capture.cap"),
        "-a": ("Şifreleme algoritmasını belirtir.", "Örnek: aircrack-ng -a 1 capture.cap"),
        "-b": ("Hedef ağın MAC adresini belirtir.", "Örnek: aircrack-ng -b 00:11:22:33:44:55 capture.cap"),
        "-w": ("Kullanılacak kelime listesini belirtir.", "Örnek: aircrack-ng -w wordlist.txt capture.cap"),
        "--help": ("Yardım menüsünü gösterir.", "Örnek: aircrack-ng --help")
    }
    print_cheat_sheet("Aircrack-ng", cheat_sheet)

def main():
    print("Hangi araç için cheat sheet görmek istersiniz?")
    print("1: Nmap")
    print("2: Nikto")
    print("3: SQLMap")
    print("4: Burp Suite")
    print("5: Metasploit")
    print("6: Wireshark")
    print("7: DIRB")
    print("8: Hydra")
    print("9: John the Ripper")
    print("10: Nessus")
    print("11: Maltego")
    print("12: Aircrack-ng")
    print("Q: Çıkış")
    
    while True:
        choice = input("Seçiminizi yapın (1-12 veya Q): ")
        
        if choice == '1':
            nmap_cheat_sheet()
        elif choice == '2':
            nikto_cheat_sheet()
        elif choice == '3':
            sqlmap_cheat_sheet()
        elif choice == '4':
            burpsuite_cheat_sheet()
        elif choice == '5':
            metasploit_cheat_sheet()
        elif choice == '6':
            wireshark_cheat_sheet()
        elif choice == '7':
            dirb_cheat_sheet()
        elif choice == '8':
            hydra_cheat_sheet()
        elif choice == '9':
            john_the_ripper_cheat_sheet()
        elif choice == '10':
            nessus_cheat_sheet()
        elif choice == '11':
            maltego_cheat_sheet()
        elif choice == '12':
            aircrack_ng_cheat_sheet()
        elif choice.upper() == 'Q':
            print("Çıkılıyor...")
            break
        else:
            print("Geçersiz seçim, lütfen tekrar deneyin.")

if __name__ == "__main__":
    main()
