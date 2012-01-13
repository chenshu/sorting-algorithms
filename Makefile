main: shell.o
	gcc -o main shell.o
clean:
	rm -f main shell.o
