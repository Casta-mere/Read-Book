import requests
from bs4 import BeautifulSoup as Bs

class book():
    def __init__(self):
        self.id=0
        self.name=""
        self.author=""
        self.country=""
        self.publisher=""
        self.year=""
        self.page=""
        self.price=""
        self.frame=""
        self.category=""
        self.isbn=""
        self.star=0
        self.comment_num=0
        self.brief=""
        self.douban_bookid=""
        self.link=""
        self.name_o=""
        self.trans=""

    def output(self):
        ans=[]
        ans.append(self.id)
        ans.append(f'"{self.name}"')
        ans.append(f'"{self.author}"')
        ans.append(f'"{self.country}"')
        ans.append(f'"{self.publisher}"')
        ans.append(f'"{self.year}"')
        ans.append(f'"{self.page}"')
        ans.append(f'"{self.price}"')
        ans.append(f'"{self.frame}"')
        ans.append(f'"{self.category}"')
        ans.append(f'"{self.isbn}"')
        ans.append(self.star)
        ans.append(self.comment_num)
        ans.append(f'"{self.brief}"')
        ans.append(f'"{self.douban_bookid}"')
        ans.append(f'"{self.link}"')
        ans.append(f'"{self.name_o}"')
        ans.append(f'"{self.trans}"')


        return ans

def get_bookherf():
    url = "https://book.douban.com/top250?start="
    i = 0
    urllist = []
    while(i < 200):
        urllist.append(url+str(i))
        i = i+25
    headers = {
        "cookies": "SRCHD=AF=NOFORM; SRCHUID=V=2&GUID=41E060320BE94F829AC2DD21A3D21AF0&dmnchg=1; MUID=02B792634CBA6A751C1D9D7C4DC56B7F; _ITAB=STAB=TR; MUIDV=NU=1; _TTSS_IN=hist=WyJ6aC1IYW5zIiwiZW4iLCJhdXRvLWRldGVjdCJd; MUIDB=02B792634CBA6A751C1D9D7C4DC56B7F; SnrOvr=X=rebateson; _RwBf=W=1&r=1&mta=0&rc=126&rb=126&gb=0&rg=0&pc=126&mtu=0&rbb=0.0&g=0&cid=&v=2&l=2021-11-23T08:00:00.0000000Z&lft=00010101&aof=0&o=0&p=MSRLAUNCHERAPP201805&c=MR000I&t=4945&s=2021-03-20T23:27:43.6748591+00:00&ts=2021-11-24T07:20:12.9037975+00:00&rwred=0&e=2RJbUeT8NCYtKCfJJYgHOHFw0i1UIP8XDsAQ49Kztj_4ybrnkTyGuoPHwA-1R-65nVzgcDAFavWWwGhoJWBRdg&A=220A99376FB293C916B649F8FFFFFFFF; _tarLang=default=zh-Hans; _TTSS_OUT=hist=WyJlbiIsInpoLUhhbnQiLCJ6aC1IYW5zIl0=; _EDGE_CD=u=zh-hans&m=zh-cn; _UR=MC=1&QS=3&TC=C0&TQS=3; _clck=fsoq58|1|f1q|0; imgv=lodlg=5&gts=20210826&flts=20220616; ANON=A=220A99376FB293C916B649F8FFFFFFFF&E=1b25&W=1; _HPVN=CS=eyJQbiI6eyJDbiI6MCwiU3QiOjIsIlFzIjoxLCJQcm9kIjoiUCJ9LCJTYyI6eyJDbiI6MCwiU3QiOjEsIlFzIjoxLCJQcm9kIjoiSCJ9LCJReiI6eyJDbiI6MzcsIlN0IjoxLCJRcyI6MCwiUHJvZCI6IlQifSwiQXAiOnRydWUsIk11dGUiOnRydWUsIkxhZCI6IjIwMjItMDctMjFUMDA6MDA6MDBaIiwiSW90ZCI6MCwiR3diIjowLCJEZnQiOm51bGwsIk12cyI6MCwiRmx0IjowLCJJbXAiOjQyfQ==; BFB=AhBwoSdXKbnRXi768ticlR8tliyXnuF_SzEs1jYXh5LkkJjOjZAh_iZ4p6LRrb_5G9Zn5z-uk54dzmOfrcSIVpEzHu2vpbt-VSbQGR33aacaAxgQ3hmmocDVbs7Gzv447dpDNq3LLnGs50URgBH19oh1EOWy8Ft-dzCw0zYHSs9huA; OIDR=ghAJ3yG9eulJLCpxBDPgNWe9YGv1iFUmkfrHfjo2Rm4dI8s-CujV6tnVA4si1VO6ag5LDRqDzcsiujMBiF7v59nBNQ6QvuN4Gh_IfqX-mldpUVHX5t543fDvJDmwXK0djKc6ew2IdG7zdWAVuGVBe7jfmnS-4QYxnLZuljLKCiGUa0gl_Y9aTJF3HTFCxHOcoqLVqQvF4AW5d7fIASXxosQzSQgZuGjnIqD2-iyuUx1PRHLWvi-W7LXGNzhHUlRsk75099aTnfV-kfMn5cuPpp1tOQuFjs08yUnTdmMCyy1kOj2qToHTwpjCC8l4cpxoo-IidCOImc0s0Ijtj7YAv4hDch178LMKKzLQ0AP5tDCNOw9KdCfioMvsduCLYuhFfrYwBsPco65fkLkZ0HqM5HIyKiPLYT9pHOLqyAfxQfPut4jHM13CCbKrFobKcOlqrDy6tN6qw3xxUwdnypaU1wi_U6qlXDvXteMd0SU6R0wNS1TenrM8SIu5IFGzTadWeiwLdXb4Hdbq92CYiETZVwE0EOtugtNRGOXtQP6tB4Z4Dm3aNCHxlSb-actnve7PR2yw_zmy-pD0ov7YloTxjfI-B2ebsTC-w3k9vjYNoWF3xdmQTdO91hL-RTcBoGgrSBsnTQ9euc-IHDyVU0lN8iW2y-5nPIn7TYFxLg0890kjCnAFeMRQaapVkVA2Cd12B3D3GwEQGYBJ7lXjc9JuQQ7yvwaAwE8055sQgWfAPBDx45ShpgzvLeUMpB9peyb9eldmDA5h70qBKMU9ievXGsb4hBABYeSaia_-3DBVEvplmmhcJ7k_bQ8R3h7dmNJOVFNo1RqKsfjvrGMY_HBpMVQoPEEQXY3BkTK5BhDjYTaopTfqApzQMuoRrEwjFADarMtY2rwrw5hXel35C3V3ZE4tUD00qvZ9xFxarAUtoUaY35IpOUu0rbxMPW91ya28QdJ6Cx3E4MB1LmglPo9hXIgxT4v_2_972pMHl3EUEEzys45MX5vnqskrvbAacHaF9iSscTIogKwM7uGc4dKo3FjTtp06z1Bwz2UiAasgs0uJnC1333iuek24_e2wdJr_KVJhzFx6aIVi2NyrfGDRtEkcLo3EcpBVR9hV3g6V6SSINzQEjmsarraT5yzCsgoBiL--dUe_94t4IrZpOask4cze; SRCHUSR=DOB=20200807&T=1632741452000&POEX=W; BFBUSR=BAWAS=1&BAWFS=1; ZHCHATSTRONGATTRACT=TRUE; HOOKBLOCKINDICATOR=TRUE; ABDEF=V=13&ABDV=11&MRNB=1658988915033&MRB=0; SUID=A; ZHCHATWEAKATTRACT=TRUE; WLS=C=edac5ceb5db4f577&N=%e6%97%ad%e5%88%9a; _SS=SID=0996E115B28D6CA82620F0E7B3CE6DBD&PC=EDGEDSE; SRCHS=PC=EDGEDSE; _EDGE_S=SID=0996E115B28D6CA82620F0E7B3CE6DBD&mkt=zh-cn; _U=17u4gEBOVrZfL6D1YR1XR4P44YWZ63rliqJWmwucuPXLk-JNeFhzprO1VTaBhLnGCrFYTTpXgAist4PM1c7E6FgkHd1g2rmSzZO-uoM66Io6cwAyews98Xgm1P_LE1LHyXLHVE4HTLTAcZnWvTc86F0m0oppkanvPnylPAGUiJnbyvehkMLWJawja6DOpDDz6ceMWOI02rauWY1DyA6LfoA; ipv6=hit=1659246496999&t=4; SNRHOP=I=&TS=; USRLOC=HS=1&RL=0&DLOC=LAT=30.316324609128348|LON=120.3489917887236|A=83|N=%e6%9d%ad%e5%b7%9e%e5%b8%82%e9%92%b1%e5%a1%98%e5%8c%ba|C=|S=|TS=220731045118|ETS=220731050118|; OID=ghDrCs3ybRpd-p0q73npqH-gY64gb_wfQaxp9SOwiid565_wTDhyFnTaS7xIylD2WknKrWSeit9jjq5a2B5tyCEwmViqNOoYKMrE3OW58zNyWqVKXStSp7EsH8nSoSBHfGGA6WkgDE_SUfoUYi6T3ZHT56Jux_bmfw4u0lc1apmKhPvdpfMbi8X8YTdEosRxBQfCxQoZCV6BJVI6eHCmQaXmVvLP6nNydgcE_oMXTo_FvPIo26CMOz0dl4zCkf_gyR37ZQn81uA5_W9XjyqrIfMzv_rfAAQ49mZIBeLYTOjX1zuI4BXfHjjmmPm8jhP-OTBoz6x5E6C8gUyeU4rnIDrx1YAmmQcxC5PM39akrV5ITPGni6rQSfbqsLLtXLU2PoeExaYbfbM-WAu13thyq7iPEN0kZ0J64W0Rxu3A5MIgUvNnC1rOVe1y1FvUEaGJcOA0Gb_oaH6KsWRTeCxCLs2nLklQhYKpk1K3IEySsQQcTgkL_5HqE3Iy2BrT600kY89RuVyk9lrfD0uQ5o8QgDaE_FJ_rFq6qlBq6TA2WGj52CQM0L6uD3q1reB3hzyRin7Q8jNRih5IqtukGRaDiv9Hlap-UBfcCgAoAauVpaYzRURQvDmSMda-KHPWTWzCaIDFNc1IV9r_k_61qeKB95cMsW-7SX-8RV5UsV9CVQ-VUsssaSWYrhi4MYyQqiMb_K0coGyBJLm669UnM0Mhaj8ri3sgkFNQe4Xsqc-NNtFMbnN2eFakP2OZ4Mq6WF9_1cgPREpl-6uiiso7IoChx8qqKSSx4T3YcsCE5kLRwHehgm-rUuaa5V_rOQSVl8tOIVVhy1aAFjDi8k9fdSGbkN0BRumM62JLX0n2EPw576SNvQEogHgNhc3_i4H5AMpYxuaFGrLq0tSsHEsGom3YAAW1s-iWYXvVgKTR_VUV9Uchg7QPjPIyER7-zS_hcnD_XWhOKK-HbiNz8bVIadhfF929Hliveb3Yv8DrU3KuP1w7-q1HB5tEh6TYDPEKp7wsIVIE0BZ_HcVr3nzBl-EDyyQBMXFjOeldKnmbSPtH8HOdC66zHGjsPhjRZTi0p2xE_XmsCfP6ZR04tEeHQoK2BOk4XDg-HNcYjfJthbDHpJ43IdQDerFg009EFWY5yXY4tDHWkgREluOhfai0nyycBnPjYSiS9raw_cu9JYmsT_Q4NP33fsLNceilIN45dut8yYWHhqDLT-GNVZPSNE8SDhpI-gwUB-LpcgQg87lxwCV-Ls3CoxgBZIps9qUAqcG-q38GoaTkxrITqjFBAfyCzDREwjM6ekvNKblQmmqLXl7P78pY8c9Fx5lM94KwWR2z68Ggce8daKUFZW2pAV4jwV13Mj4WLMNEw9ERzSJ-YXhb5wn7KA0MgWSZ3jZflA6eRjTJBiDa573sGM9CdbkGK8wg6k9o-el8bZcj6Z9XobJlRc0nzVuSikyfVlOS3SqY1Bdg5yIofzcfPSyirwdf2YSj1N9MmRBxqXeG5zblE00Ym-wn0tmO5OgTpradoA9ULkZrnkRy6773yW3woIjcNBUx0s5Nvfphgmdrm4lFa7ctnd9Yi4CR2zV2wnTFZs5bFsXW4S99sQzWvKqek52dqYc18xSI8LGgbLyX3rmN_u4dvfJmdZKI8kgR6kHcB01HZ93l6Ztr3kQDWil7XrkO3LuLu6l9nj0i1WJoddEMnoxIG5pLp8KpPNC3x9W8-mj9xDti0JFg_sEoLjuYwm1e-rjmD9GRKKwNeVN5XEd9BlHbw4pfoUFR89LL0dq2B8io5381Kzhkv5cq9xFMvUCvnC31eBtzJhsY7f84bVppliUL_HkaHMXWY78uTX2HPbd91j7jqORKuYjopr_BHZ8trOUDIxzZEH7M1Og_7a5VGm-0t1gFV1abuc18RDHH1zcuHn-XshUNUPLtA04QWCVYiFuqxW1iU6nIZlewQUf7SmXvqhzctBBtnTb59vXoQC7KJzN4JQ_nnlqHwgOnCTYWucXn23K7HTvJMx22OkDvJKT3cbh1ZNM-K2TXrcXGJMaVPIPYdYMKupYgk2x35AnkCzaywVEp7WFDSg1PAfXk1mm0uA; OIDI=AhDHYk-8dNF3abyUm1ZzsVlaMqzaICOBe_XyPi890W42lg; SRCHHPGUSR=SRCHLANG=zh-Hans&PV=10.0.0&BRW=HTP&BRH=T&CW=962&CH=1014&SW=1920&SH=1080&DPR=1&UTC=480&DM=0&EXLTT=23&HV=1659243078&BZA=0",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36 Edg/103.0.1264.77"
    }
    dir = f"code/webcrawer/ans/bookherf.txt"
    ans = []
    for l in urllist:
        Douban_response = requests.get(l, headers=headers)
        soup = Bs(Douban_response.text, "html.parser")

        herfs = soup.find_all("a", class_="nbg")

        for i in herfs:
            ans.append(i.get("href")+"\n")
    with open(dir, "a", encoding="utf-8") as f:
        for i in ans:
            f.write(i)

def get_detail_info(count,url):
    ans = []
    b=book()
    headers = {
        "cookies": "SRCHD=AF=NOFORM; SRCHUID=V=2&GUID=41E060320BE94F829AC2DD21A3D21AF0&dmnchg=1; MUID=02B792634CBA6A751C1D9D7C4DC56B7F; _ITAB=STAB=TR; MUIDV=NU=1; _TTSS_IN=hist=WyJ6aC1IYW5zIiwiZW4iLCJhdXRvLWRldGVjdCJd; MUIDB=02B792634CBA6A751C1D9D7C4DC56B7F; SnrOvr=X=rebateson; _RwBf=W=1&r=1&mta=0&rc=126&rb=126&gb=0&rg=0&pc=126&mtu=0&rbb=0.0&g=0&cid=&v=2&l=2021-11-23T08:00:00.0000000Z&lft=00010101&aof=0&o=0&p=MSRLAUNCHERAPP201805&c=MR000I&t=4945&s=2021-03-20T23:27:43.6748591+00:00&ts=2021-11-24T07:20:12.9037975+00:00&rwred=0&e=2RJbUeT8NCYtKCfJJYgHOHFw0i1UIP8XDsAQ49Kztj_4ybrnkTyGuoPHwA-1R-65nVzgcDAFavWWwGhoJWBRdg&A=220A99376FB293C916B649F8FFFFFFFF; _tarLang=default=zh-Hans; _TTSS_OUT=hist=WyJlbiIsInpoLUhhbnQiLCJ6aC1IYW5zIl0=; _EDGE_CD=u=zh-hans&m=zh-cn; _UR=MC=1&QS=3&TC=C0&TQS=3; _clck=fsoq58|1|f1q|0; imgv=lodlg=5&gts=20210826&flts=20220616; ANON=A=220A99376FB293C916B649F8FFFFFFFF&E=1b25&W=1; _HPVN=CS=eyJQbiI6eyJDbiI6MCwiU3QiOjIsIlFzIjoxLCJQcm9kIjoiUCJ9LCJTYyI6eyJDbiI6MCwiU3QiOjEsIlFzIjoxLCJQcm9kIjoiSCJ9LCJReiI6eyJDbiI6MzcsIlN0IjoxLCJRcyI6MCwiUHJvZCI6IlQifSwiQXAiOnRydWUsIk11dGUiOnRydWUsIkxhZCI6IjIwMjItMDctMjFUMDA6MDA6MDBaIiwiSW90ZCI6MCwiR3diIjowLCJEZnQiOm51bGwsIk12cyI6MCwiRmx0IjowLCJJbXAiOjQyfQ==; BFB=AhBwoSdXKbnRXi768ticlR8tliyXnuF_SzEs1jYXh5LkkJjOjZAh_iZ4p6LRrb_5G9Zn5z-uk54dzmOfrcSIVpEzHu2vpbt-VSbQGR33aacaAxgQ3hmmocDVbs7Gzv447dpDNq3LLnGs50URgBH19oh1EOWy8Ft-dzCw0zYHSs9huA; OIDR=ghAJ3yG9eulJLCpxBDPgNWe9YGv1iFUmkfrHfjo2Rm4dI8s-CujV6tnVA4si1VO6ag5LDRqDzcsiujMBiF7v59nBNQ6QvuN4Gh_IfqX-mldpUVHX5t543fDvJDmwXK0djKc6ew2IdG7zdWAVuGVBe7jfmnS-4QYxnLZuljLKCiGUa0gl_Y9aTJF3HTFCxHOcoqLVqQvF4AW5d7fIASXxosQzSQgZuGjnIqD2-iyuUx1PRHLWvi-W7LXGNzhHUlRsk75099aTnfV-kfMn5cuPpp1tOQuFjs08yUnTdmMCyy1kOj2qToHTwpjCC8l4cpxoo-IidCOImc0s0Ijtj7YAv4hDch178LMKKzLQ0AP5tDCNOw9KdCfioMvsduCLYuhFfrYwBsPco65fkLkZ0HqM5HIyKiPLYT9pHOLqyAfxQfPut4jHM13CCbKrFobKcOlqrDy6tN6qw3xxUwdnypaU1wi_U6qlXDvXteMd0SU6R0wNS1TenrM8SIu5IFGzTadWeiwLdXb4Hdbq92CYiETZVwE0EOtugtNRGOXtQP6tB4Z4Dm3aNCHxlSb-actnve7PR2yw_zmy-pD0ov7YloTxjfI-B2ebsTC-w3k9vjYNoWF3xdmQTdO91hL-RTcBoGgrSBsnTQ9euc-IHDyVU0lN8iW2y-5nPIn7TYFxLg0890kjCnAFeMRQaapVkVA2Cd12B3D3GwEQGYBJ7lXjc9JuQQ7yvwaAwE8055sQgWfAPBDx45ShpgzvLeUMpB9peyb9eldmDA5h70qBKMU9ievXGsb4hBABYeSaia_-3DBVEvplmmhcJ7k_bQ8R3h7dmNJOVFNo1RqKsfjvrGMY_HBpMVQoPEEQXY3BkTK5BhDjYTaopTfqApzQMuoRrEwjFADarMtY2rwrw5hXel35C3V3ZE4tUD00qvZ9xFxarAUtoUaY35IpOUu0rbxMPW91ya28QdJ6Cx3E4MB1LmglPo9hXIgxT4v_2_972pMHl3EUEEzys45MX5vnqskrvbAacHaF9iSscTIogKwM7uGc4dKo3FjTtp06z1Bwz2UiAasgs0uJnC1333iuek24_e2wdJr_KVJhzFx6aIVi2NyrfGDRtEkcLo3EcpBVR9hV3g6V6SSINzQEjmsarraT5yzCsgoBiL--dUe_94t4IrZpOask4cze; SRCHUSR=DOB=20200807&T=1632741452000&POEX=W; BFBUSR=BAWAS=1&BAWFS=1; ZHCHATSTRONGATTRACT=TRUE; HOOKBLOCKINDICATOR=TRUE; ABDEF=V=13&ABDV=11&MRNB=1658988915033&MRB=0; SUID=A; ZHCHATWEAKATTRACT=TRUE; WLS=C=edac5ceb5db4f577&N=%e6%97%ad%e5%88%9a; _SS=SID=0996E115B28D6CA82620F0E7B3CE6DBD&PC=EDGEDSE; SRCHS=PC=EDGEDSE; _EDGE_S=SID=0996E115B28D6CA82620F0E7B3CE6DBD&mkt=zh-cn; _U=17u4gEBOVrZfL6D1YR1XR4P44YWZ63rliqJWmwucuPXLk-JNeFhzprO1VTaBhLnGCrFYTTpXgAist4PM1c7E6FgkHd1g2rmSzZO-uoM66Io6cwAyews98Xgm1P_LE1LHyXLHVE4HTLTAcZnWvTc86F0m0oppkanvPnylPAGUiJnbyvehkMLWJawja6DOpDDz6ceMWOI02rauWY1DyA6LfoA; ipv6=hit=1659246496999&t=4; SNRHOP=I=&TS=; USRLOC=HS=1&RL=0&DLOC=LAT=30.316324609128348|LON=120.3489917887236|A=83|N=%e6%9d%ad%e5%b7%9e%e5%b8%82%e9%92%b1%e5%a1%98%e5%8c%ba|C=|S=|TS=220731045118|ETS=220731050118|; OID=ghDrCs3ybRpd-p0q73npqH-gY64gb_wfQaxp9SOwiid565_wTDhyFnTaS7xIylD2WknKrWSeit9jjq5a2B5tyCEwmViqNOoYKMrE3OW58zNyWqVKXStSp7EsH8nSoSBHfGGA6WkgDE_SUfoUYi6T3ZHT56Jux_bmfw4u0lc1apmKhPvdpfMbi8X8YTdEosRxBQfCxQoZCV6BJVI6eHCmQaXmVvLP6nNydgcE_oMXTo_FvPIo26CMOz0dl4zCkf_gyR37ZQn81uA5_W9XjyqrIfMzv_rfAAQ49mZIBeLYTOjX1zuI4BXfHjjmmPm8jhP-OTBoz6x5E6C8gUyeU4rnIDrx1YAmmQcxC5PM39akrV5ITPGni6rQSfbqsLLtXLU2PoeExaYbfbM-WAu13thyq7iPEN0kZ0J64W0Rxu3A5MIgUvNnC1rOVe1y1FvUEaGJcOA0Gb_oaH6KsWRTeCxCLs2nLklQhYKpk1K3IEySsQQcTgkL_5HqE3Iy2BrT600kY89RuVyk9lrfD0uQ5o8QgDaE_FJ_rFq6qlBq6TA2WGj52CQM0L6uD3q1reB3hzyRin7Q8jNRih5IqtukGRaDiv9Hlap-UBfcCgAoAauVpaYzRURQvDmSMda-KHPWTWzCaIDFNc1IV9r_k_61qeKB95cMsW-7SX-8RV5UsV9CVQ-VUsssaSWYrhi4MYyQqiMb_K0coGyBJLm669UnM0Mhaj8ri3sgkFNQe4Xsqc-NNtFMbnN2eFakP2OZ4Mq6WF9_1cgPREpl-6uiiso7IoChx8qqKSSx4T3YcsCE5kLRwHehgm-rUuaa5V_rOQSVl8tOIVVhy1aAFjDi8k9fdSGbkN0BRumM62JLX0n2EPw576SNvQEogHgNhc3_i4H5AMpYxuaFGrLq0tSsHEsGom3YAAW1s-iWYXvVgKTR_VUV9Uchg7QPjPIyER7-zS_hcnD_XWhOKK-HbiNz8bVIadhfF929Hliveb3Yv8DrU3KuP1w7-q1HB5tEh6TYDPEKp7wsIVIE0BZ_HcVr3nzBl-EDyyQBMXFjOeldKnmbSPtH8HOdC66zHGjsPhjRZTi0p2xE_XmsCfP6ZR04tEeHQoK2BOk4XDg-HNcYjfJthbDHpJ43IdQDerFg009EFWY5yXY4tDHWkgREluOhfai0nyycBnPjYSiS9raw_cu9JYmsT_Q4NP33fsLNceilIN45dut8yYWHhqDLT-GNVZPSNE8SDhpI-gwUB-LpcgQg87lxwCV-Ls3CoxgBZIps9qUAqcG-q38GoaTkxrITqjFBAfyCzDREwjM6ekvNKblQmmqLXl7P78pY8c9Fx5lM94KwWR2z68Ggce8daKUFZW2pAV4jwV13Mj4WLMNEw9ERzSJ-YXhb5wn7KA0MgWSZ3jZflA6eRjTJBiDa573sGM9CdbkGK8wg6k9o-el8bZcj6Z9XobJlRc0nzVuSikyfVlOS3SqY1Bdg5yIofzcfPSyirwdf2YSj1N9MmRBxqXeG5zblE00Ym-wn0tmO5OgTpradoA9ULkZrnkRy6773yW3woIjcNBUx0s5Nvfphgmdrm4lFa7ctnd9Yi4CR2zV2wnTFZs5bFsXW4S99sQzWvKqek52dqYc18xSI8LGgbLyX3rmN_u4dvfJmdZKI8kgR6kHcB01HZ93l6Ztr3kQDWil7XrkO3LuLu6l9nj0i1WJoddEMnoxIG5pLp8KpPNC3x9W8-mj9xDti0JFg_sEoLjuYwm1e-rjmD9GRKKwNeVN5XEd9BlHbw4pfoUFR89LL0dq2B8io5381Kzhkv5cq9xFMvUCvnC31eBtzJhsY7f84bVppliUL_HkaHMXWY78uTX2HPbd91j7jqORKuYjopr_BHZ8trOUDIxzZEH7M1Og_7a5VGm-0t1gFV1abuc18RDHH1zcuHn-XshUNUPLtA04QWCVYiFuqxW1iU6nIZlewQUf7SmXvqhzctBBtnTb59vXoQC7KJzN4JQ_nnlqHwgOnCTYWucXn23K7HTvJMx22OkDvJKT3cbh1ZNM-K2TXrcXGJMaVPIPYdYMKupYgk2x35AnkCzaywVEp7WFDSg1PAfXk1mm0uA; OIDI=AhDHYk-8dNF3abyUm1ZzsVlaMqzaICOBe_XyPi890W42lg; SRCHHPGUSR=SRCHLANG=zh-Hans&PV=10.0.0&BRW=HTP&BRH=T&CW=962&CH=1014&SW=1920&SH=1080&DPR=1&UTC=480&DM=0&EXLTT=23&HV=1659243078&BZA=0",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36 Edg/103.0.1264.77"
    }
    Douban_response = requests.get(url, headers=headers)
    soup = Bs(Douban_response.text, "html.parser")

    b.id=count
    b.name = soup.find('span', property="v:itemreviewed").text

    div = str(soup.find('div', id='info')).replace("\n", "").replace(
        "br/", "br").replace("/br", "br").replace("\xa0", "")
    ans = div.split("<br>")
    for i in ans:
        x = Bs(i, 'html.parser')
        x=x.text.split(":")
        if('作者' in x[0]):
            x[1]=x[1].replace(" ","")
            b.author=x[1]
            if(x[1][0]=='['):
                b.country=x[1].split("[")[1].split("]")[0]
            else:
                b.country="中国"
        elif(x[0]=='出版社'):
            x[1]=x[1].replace(" ","")
            b.publisher=x[1]
        elif(x[0]=='出版年'):
            x[1]=x[1].replace(" ","")
            b.year=x[1]
        elif(x[0]=='页数'):
            x[1]=x[1].replace(" ","")
            b.page=x[1]
        elif(x[0]=='定价'):
            x[1]=x[1].replace(" ","")
            b.price=x[1]
        elif(x[0]=='装帧'):
            x[1]=x[1].replace(" ","")
            b.frame=x[1]
        elif(x[0]=='ISBN'):
            x[1]=x[1].replace(" ","")
            b.isbn=x[1]
        elif(x[0]=='丛书'):
            x[1]=x[1].replace(" ","")
            b.category=x[1]
        elif(x[0]=='原作名'):
            b.name_o=x[1]
        elif(x[0]=='译者'):
            x[1]=x[1].replace(" ","")
            b.trans=x[1]

    b.star=float(soup.find('strong', class_="ll rating_num").text)
    b.comment_num=int(soup.find('span', property="v:votes").text)
    div=soup.find('div',id="link-report")
    try:
        b.brief=div.find_all('div', class_="intro")[-1].text.replace("\n","").replace("\r","").replace("\t","").replace(" ","").replace("--","")
    except:
        print("no brief")
    b.link=url
    b.douban_bookid=url.split("/")[-2]

    ans=b.output()
    return ans


get_bookherf()
# get_detail_info()
