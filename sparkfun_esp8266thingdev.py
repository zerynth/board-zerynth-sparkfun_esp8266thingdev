from base import *
from devices import *

class SparkfunEsp8266ThingDev(Board):

    @staticmethod
    def match(dev):
        return dev["vid"]=="0403" and dev["pid"] in ("6015")
    

    def reset(self):
        import time
        conn = ConnectionInfo()
        conn.set_serial(self.port,**self.connection)
        ch = Channel(conn)
        try:
            ch.open(timeout=2)
        except:
            fatal("Can't open serial:",self.port)
        ch.setDTR(False)
        ch.setRTS(True)
        time.sleep(0.05)
        ch.close()
        time.sleep(1)


    def burn(self,bin,outfn=None):
        rom = bin[0]
        irom = bin[1]
        brom = bin[2]
        prom = bin[3]
        romf = fs.get_tempfile(rom)
        iromf = fs.get_tempfile(irom)
        bromf = fs.get_tempfile(brom)
        promf = fs.get_tempfile(prom)
        prom_addr = len(irom)
        if prom_addr % 0x1000 != 0:
            #align
            prom_addr = prom_addr + (0x1000 - (prom_addr%0x1000))
            #add origin
            prom_addr+=0x20000
        res,out,err = proc.runcmd("python",tools["esptool"],"--port",self.port,"write_flash","--flash_freq","40m","--flash_mode","dio","--flash_size","4m","--verify", "0x00000",romf, "0x20000", iromf, "0x3fc000",bromf,hex(prom_addr),promf,outfn=outfn)
        fs.del_tempfile(romf)
        fs.del_tempfile(iromf)
        fs.del_tempfile(bromf)
        fs.del_tempfile(promf)
        if res:
            return False,out
        return True,out

    def erase(self,outfn=None):
        res,out,err = proc.runcmd("python",tools["esptool"],"--port",self.port,"erase_flash",outfn=outfn)
        if res:
            return False,out
        return True,out

