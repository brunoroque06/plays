all: run

build:
	go build ./...

format:
	gofmt -s -w .

run:
	go run main.go

test:
	go test -covermode=count ./...

.PHONY: all build format run test
