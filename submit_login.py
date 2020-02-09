import requests
import multiprocessing
from exploit_login import exploit

TEAMS = 11


def submit(flag: str):
    credentials = {
        "team": "mentimun_mentah",
        "token": "pzZ3KHJk",
    }
    headers = {
        "Authorization": "mtUJh44ViZCilVOh_QMvdoSpcoSxURLU_wcrQuq_-sFFFHR_aw7mMQ"}
    with requests.Session() as s:
        r = s.post("http://172.31.1.1/api/flag/submit", json={
            "flag": flag
        }, headers=headers)
        # print(r)
        return str(r.text)


def main():
    with multiprocessing.Pool() as p:
        flags = p.map(exploit, range(1, TEAMS+1))

    flags = list(set(flags))
    print(type(flags[0]))
    print(flags)

    with multiprocessing.Pool() as p:
        response = p.map(submit, flags)

    print(response)


if __name__ == "__main__":
    main()
