.PHONY: prepare
prepare: 
	go mod init github.com/brunoroque06/geneticalgorithm

.PHONY: run
run:
	go run main.go

.PHONY: test
test:
	go test ./...

.PHONY: format
format:
	gofmt -s -w .

.PHONY: lint
lint:
	golint -set_exit_status ./...
