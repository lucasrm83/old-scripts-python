#qpy:console
try:
    from injector import FreedomCreative 
except:
    from injector import FreedomCreative 

fc = FreedomCreative()
fc.set_config('virtualgames.wapka.mobi/server.ini')
fc.jalankan()