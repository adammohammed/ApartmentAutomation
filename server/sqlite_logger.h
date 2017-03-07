#ifndef  SQLITE_LOGGER_H
#define  SQLITE_LOGGER_H
#include <string>
#include <sqlite3.h>


class Logger {
    private:
        const char * dbloc;
        sqlite3* db;

    public:
        Logger(const char*  database){
            dbloc = database;
        }

        void store_value(std::string, std::string, double);
};

void Logger::store_value(std::string table, std::string field, double value) {
   sqlite3_stmt * stmt;

   std::string sqlstmnt = "INSET INTO "+table+" ("+field+") VALUES ("
                        + std::to_string(value) +");";

   if(sqlite3_open(dbloc, &db) == SQLITE_OK){
           sqlite3_prepare(db, sqlstmnt.c_str(), -1, &stmt, NULL);
           sqlite3_step(stmt);
   }
   sqlite3_finalize(stmt);
   sqlite3_close(db);
}
#endif
