print "------------------------------------------"
print "|  Modificado por: @Wellington69xnx"
print "|  Site: \033[45mhttp://virtualgames.wapka.mobi"
print "\033[0;0m|  Canal: @VirtualGamesCanal"
print "|  Grupo: @VirtualGames"

print "|  FB: http://facebook.com/wellington69xnx"
import BaseHTTPServer, ConfigParser, os, SocketServer, select, socket
configfile = 'virtualgames.wapka.mobi/server.ini'
cfg_lastmodif = ''
reqheaderadd = ''
cfg = {}
cfg_general = {}
cfg_debug = False
cfg_listen = 8799
cfg_proxy = ''
cfg_queryurl = {}
cfg_queryurl_enable = False
cfg_queryurl_urlpath = False
cfg_queryheader = {}
cfg_queryheader_enable = False
cfg_reqheader = {}
cfg_reqheader_enable = False
cfg_loglevel = 0
cfg_skipres = 0
cfg_bufsize = 8192
cfg_timeout = 60
cfg_swait = False
cfg_maxwait = 20

class renk:
    pembe = '\033[95m'
    mavi = '\033[94m'
    yesil = '\033[92m'
    sari = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    beyaz='\x1b[m'

class FreedomCreative:

    def set_config(self, fileconfig):
        global configfile
        if os.path.isfile(os.path.realpath(fileconfig)):
            configfile = os.path.realpath(fileconfig)
        elif os.path.isfile(os.path.realpath(os.path.join(os.path.dirname(__file__), fileconfig))):
            configfile = os.path.realpath(os.path.join(os.path.dirname(__file__), fileconfig))
        else:
            print 'ERROR: Config file not found (' + os.path.realpath(fileconfig) + ')'
            print 'Or'
            print 'ERROR: Config file not found (' + os.path.realpath(os.path.join(os.path.dirname(__file__), fileconfig)) + ')'
            exit()

    def __init__(self):
        pass

    def build_cfg(self):
        cfg_var = {}
        config = ConfigParser.RawConfigParser()
        try:
            config.read(configfile)
            for section in config.sections():
                cfg_var[section] = {}
                for option in config.options(section):
                    cfg_var[section].setdefault(option, config.get(section, option))

            return cfg_var
        except ConfigParser.ParsingError as e:
            print e

    def cfg_definition(self):
        global cfg_swait
        global cfg
        global cfg_loglevel
        global cfg_queryurl_enable
        global cfg_queryurl_urlpath
        global cfg_queryheader_enable
        global cfg_queryurl
        global cfg_bufsize
        global cfg_maxwait
        global cfg_timeout
        global cfg_queryheader
        global cfg_proxy
        global cfg_debug
        global cfg_reqheader_enable
        global cfg_reqheader
        global cfg_general
        global cfg_skipres
        global cfg_listen
        print renk.yesil,"Check sua APN"
        try:
            cfg = self.build_cfg()
            cfg_general = cfg['GENERAL']
            cfg_debug = bool(int(cfg_general['debug']))
            cfg_proxy = str(cfg_general['proxy'])
            cfg_listen = int(cfg_general['listen'])
            cfg_queryurl = cfg['QUERY_URL']
            cfg_queryurl_enable = bool(int(cfg_queryurl['enable']))
            cfg_queryurl_urlpath = bool(int(cfg_queryurl['urlpath']))
            cfg_queryheader = cfg['QUERY_HEADER']
            cfg_queryheader_enable = bool(int(cfg_queryheader['enable']))
            cfg_reqheader = cfg['REQ_HEADER']
            cfg_reqheader_enable = bool(int(cfg_reqheader['enable']))
            cfg_loglevel = int(cfg_general['loglevel'])
            cfg_skipres = bool(int(cfg_general['skipres']))
            cfg_bufsize = int(cfg_general['bufsize'])
            cfg_timeout = int(cfg_general['timeout'])
            cfg_maxwait = int(cfg_general['maxwait'])
            cfg_swait = bool(int(cfg_general['swait']))
        except ValueError as e:
            print 'Error Config sob: '
            print e
            exit()

    def jalankan(self):
        global cfg_lastmodif
        cfg_lastmodif = os.path.getmtime(configfile)
        print renk.beyaz,"-----------------------------------------"
        print renk.FAIL,"----------------[Injetando]---------------"
        print renk.beyaz,"-----------------------------------------"
        self.cfg_definition()
        print '# Config: ' + configfile
        print '# Nome: Qpython VirtualGames'
        print '# APN: ' + cfg['INFO']['elsalvador']
        print '# Proxy: ' + cfg['INFO']['proty']
        print '# Porta: %s' % cfg_listen
        print '#-----------------------------------------#\r\n\r\n'
        httpd = ThreadingHTTPServer(('', cfg_listen), FC_HTTP_HANDLE)
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            httpd.server_close()
        finally:
            httpd.server_close()

        print 'Freedom stop :p'
        exit()


class FC_HTTP_HANDLE(BaseHTTPServer.BaseHTTPRequestHandler, FreedomCreative):
    server_version = 'FreedomCreative/1.04'
    default_request_version = 'HTTP/1.1'

    def do_GET(self):
        newcfgmodif = os.path.getmtime(configfile)
        if cfg_lastmodif and cfg_lastmodif != newcfgmodif:
            self.cfg_definition()
        method, url, version = self.requestline.split()
        scm, _, hosturl = url.partition('://')
        if _:
            scm = scm + _
            host, _, path = hosturl.partition('/')
            path = _ + path
        elif self.path.startswith('/'):
            scm = 'http://'
            host = self.headers['Host']
            path = url
        else:
            scm = 'ssl://'
            host = url
            path = '/'
        urlbuild = self.path
        if cfg_queryurl_enable:
            if cfg_queryurl_urlpath:
                urlbuild = path
            if cfg_queryurl['midle']:
                scm, _, hosturl = urlbuild.partition(':443')
                if _:
                    urlbuild = scm + cfg_queryurl['midle'] + _ + hosturl
                else:
                    urlbuild = urlbuild + cfg_queryurl['midle']
            if cfg_queryurl['front']:
                scm, _, hosturl = urlbuild.partition('://')
                if _:
                    urlbuild = scm + _ + cfg_queryurl['front'] + hosturl
                else:
                    urlbuild = cfg_queryurl['front'] + urlbuild
            if cfg_queryurl['back']:
                urlbuild = urlbuild + cfg_queryurl['back']
        methodbuild = method
        if cfg_general['method']:
            methodbuild = cfg_general['method'].replace('$default', method)
        requestlinebuild = methodbuild.strip() + ' ' + urlbuild.strip() + ' ' + version.strip()
        if cfg_proxy:
            host_connect = cfg_proxy.strip()
        else:
            host_connect = host
        soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            if self._new_connection(host_connect, soc):
                if cfg_loglevel == 0:
                    print '----+connect: ' + host
                    print method + ' ' + self.path
                    print '------------------------------------------'
                if cfg_loglevel == 1:
                    print '----+connect: ' + host
                    print self.requestline
                    print self.headers
                    print '------------------------------------------'
                self.reqheaderadd = ''
                if cfg_reqheader_enable:
                    self.cfgreq_header()
                self.req = ''
                if cfg_queryheader_enable and cfg_queryheader['front']:
                    self.req += str(cfg_queryheader['front']).replace('\\r\\n', '\r\n')
                self.req += requestlinebuild + '\r\n'
                if cfg_queryheader_enable and cfg_queryheader['midle']:
                    self.req += str(cfg_queryheader['midle']).replace('\\r\\n', '\r\n')
                self.headers['Connection'] = 'close'
                self.headers['Proxy-Connection'] = 'Keep-Alive'
                self.req += str(self.headers).strip()
                self.req += self.reqheaderadd
                self.req += '\n\n'
                for header in self.headers:
                    if header.lower() == 'content-length':
                        post_data_len = int(self.headers[header])
                        post_data = self.rfile.read(post_data_len)
                        self.req += post_data
                        self.req += '\r\n'
                        break

                if cfg_queryheader_enable and cfg_queryheader['back']:
                    self.req += str(cfg_queryheader['back']).replace('\\r\\n', '\r\n')
                if cfg_loglevel == 2:
                    print '----+connect: ' + host_connect
                    print self.req
                    print '------------------------------------------'
                soc.sendall(self.req)
                iw = [self.connection, soc]
                ow = []
                count = 0
                sendc = 0
                if cfg_skipres:
                    soc.recv(cfg_bufsize)
                while 1:
                    count += 1
                    ins, _, exs = select.select(iw, ow, iw, 3)
                    if exs:
                        break
                    if ins:
                        for i in ins:
                            if i is soc:
                                out = self.connection
                            else:
                                out = soc
                            data = i.recv(cfg_bufsize)
                            if data:
                                if sendc == 0:
                                    headers, __, contents = data.partition('\r\n\r\n')
                                    if __:
                                        if cfg_debug and self.command != 'CONNECT':
                                            print '----+FCDEBUG-------------------------------------'
                                            self.end_headers()
                                            fcd = ''
                                            fcd += '#-------------------------------------------------------------------#\r\n'
                                            fcd += '#------------------------FREEDOM CREATIVE DEBUG---------------------#\r\n'
                                            fcd += '#-------------------------------------------------------------------#\r\n\r\n'
                                            fcd += '----+REQUEST--------------------------------------------------\r\n'
                                            fcd += self.req
                                            fcd += '\r\n\r\n'
                                            fcd += '----+RESPONSE-------------------------------------------------\r\n'
                                            if __:
                                                fcd += headers
                                                fcd += '\r\n\r\n'
                                                fcd += contents
                                            else:
                                                fcd += data
                                            out.send(fcd)
                                        else:
                                            hsend = ''
                                            for h in headers.split('\r\n'):
                                                if h:
                                                    hsend += h + '\r\n'

                                            out.send(hsend + '\r\n')
                                            out.send(contents)
                                    else:
                                        out.send(data)
                                else:
                                    out.send(data)
                                sendc += 1
                                count = 0

                    elif cfg_swait:
                        print '--' + host + ': ', count
                    if count == cfg_maxwait:
                        break


        finally:
            print '---+DONE-----------------------------------------'
            soc.close()
            self.connection.close()

    def cfgreq_header(self):
        for rh in cfg_reqheader:
            if cfg_reqheader[rh]:
                if rh.startswith('del'):
                    del self.headers[cfg_reqheader[rh]]
                elif rh.startswith('rep'):
                    name, _, value = cfg_reqheader[rh].partition(':')
                    try:
                        exsish = self.headers[name.strip()]
                    except:
                        exsish = False

                    if _ and exsish:
                        self.headers[name.strip()] = value.strip()
                elif rh.startswith('addrep'):
                    name, _, value = cfg_reqheader[rh].partition(':')
                    if _:
                        self.headers[name.strip()] = value.strip()
                elif rh.startswith('add'):
                    self.reqheaderadd += '\r\n' + cfg_reqheader[rh].strip()

    def _new_connection(self, netloc, soc):
        i = netloc.find(':')
        if i >= 0:
            host_port = (netloc[:i], int(netloc[i + 1:]))
        else:
            host_port = (netloc, 80)
        try:
            soc.settimeout(cfg_timeout)
            soc.connect(host_port)
        except:
            print '#####---GAGAL KIRIM REQUEST---#####'
            return 0

        return 1

    do_GET = do_GET
    do_PUT = do_GET
    do_MOVE = do_GET
    do_COPY = do_GET
    do_POST = do_GET
    do_HEAD = do_GET
    do_OPTIONS = do_GET
    do_DELETE = do_GET
    do_TRACE = do_GET
    do_CONNECT = do_GET


class ThreadingHTTPServer(SocketServer.ThreadingMixIn, BaseHTTPServer.HTTPServer):
    pass


if __name__ == '__main__':
    fc = FreedomCreative()
    fc.jalankan()
