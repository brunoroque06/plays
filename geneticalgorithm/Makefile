all: run

prepare: 
	ln -fs ${PWD} ${HOME}/go/src/github.com/brunoroque06

build:
	go build ./...

run:
	go run main.go

test:
	go test ./...

format:
	gofmt -s -w .

.PHONY: all prepare build run test format
