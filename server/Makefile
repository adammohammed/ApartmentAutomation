CFLAGS=-Wall -ggdb
LIBS=-lmosquittopp

all: home_server

home_server: main.o temperature_module.o
	${CXX} $^ -o $@ $(LIBS)

main.o: main.cpp
	${CXX} -c $^ -o $@ $(LIBS)

temperature_module.o: temperature_module.cpp
	${CXX} -c $^ -o $@ $(LIBS)

clean:
	rm -f *.o

remove:
	rm -f home_server
