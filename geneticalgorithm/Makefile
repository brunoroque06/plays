.PHONY: prepare
prepare: 
	ln -fs ${PWD} ${HOME}/go/src/github.com/brunoroque06

.PHONY: run
run:
	go run main.go

.PHONY: test
test:
	go test ./...

.PHONY: format
format:
	gofmt -s -w .
