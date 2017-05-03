def tcp_server(local_addr, lport, remote_addr, rport):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.bind((local_addr, int(lport)))
        sock.listen(3)
        print('[*] Listening on {0} {1}'  .format(local_addr,lport))
        while True:
            client, addr =  sock.accept()
            print('Accepted connection {0} {1}'.format(addr[0], addr[1]))
            new_connec = threading.Thread(target=tcp_proxy, args=(client, remote_addr, rport))
            new_connec.start()
    except:
        print('Failed to listen on {}:{}'.format(local_addr, lport))
        sys.exit(0)