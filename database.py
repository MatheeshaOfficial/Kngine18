import sqlite3
import os
import logging
import sys
os.chdir(os.path.dirname(os.path.realpath(__file__)))

datalist = ['School', 'Team Name', 'Leader Name', 'Leader IGN', 'Leader Email', 'Leader Telephone', 'Player1 Name',
            'Player1 IGN', 'Player1 Email', 'Player1 Telephone', 'Player2 Name', 'Player2 IGN', 'Player2 Email',
            'Player2 Telephone', 'Player3 Name', 'Player3 IGN', 'Player3 Email', 'Player3 Telephone', 'Player4 Name',
            'Player4 IGN', 'Player4 Email', 'Player4 Telephone', 'Substitute Name', 'Substitute IGN',
            'Substitute Email', 'Substitute Telephone']


class Storage(object):
    def __init__(self):
        self.conn = sqlite3.connect('database.db')
        self.c = self.conn.cursor()
        self.c.execute("CREATE TABLE IF NOT EXISTS 'CyberCombat' ( `ID` INTEGER PRIMARY KEY AUTOINCREMENT, "
                       "`School` TEXT, `Team Name` TEXT, `Leader Name` TEXT, `Leader IGN` TEXT, `Leader Email` TEXT, "
                       "`Leader Telephone` INTEGER, `Player1 Name` TEXT, `Player1 IGN` TEXT, `Player1 Email` TEXT, "
                       "`Player1 Telephone` INTEGER, `Player2 Name` TEXT, `Player2 IGN` TEXT, `Player2 Email` TEXT, "
                       "`Player2 Telephone` INTEGER, `Player3 Name` TEXT, `Player3 IGN` TEXT, `Player3 Email` TEXT, "
                       "`Player3 Telephone` INTEGER, `Player4 Name` TEXT, `Player4 IGN` TEXT, `Player4 Email` TEXT, "
                       "`Player4 Telephone` INTEGER, `Substitute Name` TEXT, `Substitute IGN` TEXT, "
                       "`Substitute Email` TEXT, `Substitute Telephone` INTEGER)")
        self.c.execute("CREATE TABLE IF NOT EXISTS `Contact` ( `ID` INTEGER PRIMARY KEY AUTOINCREMENT, "
                       "`Name` TEXT, `Email` TEXT, `Phone` INTEGER, `Message` TEXT )")
        self.c.execute("CREATE TABLE IF NOT EXISTS 'Competitions' ( `ID` INTEGER PRIMARY KEY AUTOINCREMENT,"
                       "`Competition` TEXT, `School` TEXT, `Project Name` TEXT, `File Dir` TEXT,`Competitor Name` TEXT,"
                       " `Competitor Email` TEXT, `Competitor Telephone` INTEGER)")

    def get(self, query, *pars, readOne=False):
        LOG.log.debug("Reading Data --> {} - {}".format(query, pars))
        try:
            self.c.execute(query, pars)
            if readOne:
                return self.c.fetchone()
            else:
                return self.c.fetchall()
        except Exception as e:
            LOG.log.critical('{}, {}'.format(query, pars))
            LOG.log.exception(e)
            return str(type(e).__name__) + " : " + str(e)

    def put(self, query, pars):
        LOG.log.debug("Writing Data --> {} - {}".format(query, pars))
        try:
            self.c.execute(query, pars)
            self.conn.commit()
        except Exception as e:
            LOG.log.critical('{}, {}'.format(query, pars))
            LOG.log.exception(e)
            return str(type(e).__name__) + " : " + str(e)


class Logger(object):
    def __init__(self):
        try:
            self.buildFailed = False

            logFormatter = logging.Formatter(
                fmt='%(asctime)-10s %(levelname)-10s: %(module)s:%(lineno)-d -  %(message)s',
                datefmt='%Y-%m-%d %H:%M:%S')

            self.log = logging.getLogger()
            self.log.setLevel(logging.INFO)

            fileHandler = logging.FileHandler('KngineWeb.log', 'a')
            fileHandler.setFormatter(logFormatter)
            self.log.addHandler(fileHandler)
            consoleHandler = logging.StreamHandler()
            consoleHandler.setFormatter(logFormatter)
            self.log.addHandler(consoleHandler)
        except Exception as e:
            self.log.critical(str(type(e).__name__) + " : " + str(e))
            self.log.critical(self.getError())

    def getError(self):
        self.buildFailed = True
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        error = "{} {} {}".format(exc_type, fname, exc_tb.tb_lineno)
        return error


LOG = Logger()
