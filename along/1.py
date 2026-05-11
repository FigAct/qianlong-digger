import initlogger

loger = initlogger.get(__name__)

def main():
    loger.info("info")
    loger.debug("debug")
    loger.warning("warning")
    loger.error("error")
    loger.critical("critical")

if __name__ == '__main__':
    main()