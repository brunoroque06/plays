package plays

import (
	"dagger.io/dagger"
	"universe.dagger.io/bash"
	"universe.dagger.io/docker"
)

dagger.#Plan & {
	client: filesystem: {
		"decision-tree": read: {
			contents: dagger.#FS
			exclude: ["bin", "obj"]
		}
		"dijkstra": read: contents: dagger.#FS
		"dug": read: {
			contents: dagger.#FS
			exclude: [
				".pytest_cache",
				".streamlit",
				"venv",
			]
		}
		"genetic": read: {
			contents: dagger.#FS
			exclude: [
				".pytest_cache",
				"venv",
			]
		}
	}

	actions: {
		decisiontree: {
			img: docker.#Build & {
				steps: [
					docker.#Pull & {
						source: "mcr.microsoft.com/dotnet/sdk:7.0"
					},
					docker.#Set & {
						config: workdir: "/app"
					},
					docker.#Copy & {
						contents: client.filesystem."decision-tree".read.contents
					},
					docker.#Run & {
						command: {
							name: "dotnet"
							args: ["restore"]
						}
					},
					docker.#Run & {
						command: {
							name: "dotnet"
							args: ["tool", "restore"]
						}
					},
				]
			}
			build: bash.#Run & {
				input: img.output
				script: contents: "dotnet build"
			}
			fmt: bash.#Run & {
				input: img.output
				script: contents: "dotnet tool run fantomas --check ."
			}
			lint: bash.#Run & {
				input: img.output
				script: contents: "dotnet tool run dotnet-fsharplint lint DecisionTree.fsproj"
			}
			test: bash.#Run & {
				input: img.output
				script: contents: "dotnet test"
			}
		}

		dijkstra: {
			img: docker.#Build & {
				steps: [
					docker.#Pull & {
						source: "golang:latest"
					},
					docker.#Set & {
						config: workdir: "/app"
					},
					docker.#Copy & {
						contents: client.filesystem."dijkstra".read.contents
					},
				]
			}
			build: bash.#Run & {
				input: img.output
				script: contents: "go build -v"
			}
			fmt: bash.#Run & {
				input: img.output
				script: contents: "test -z $(gofmt -l .)"
			}
			test: bash.#Run & {
				input: img.output
				script: contents: "go test -v"
			}
		}

		dug: {
			img: docker.#Build & {
				steps: [
					docker.#Pull & {
						source: "python:3.11"
					},
					docker.#Set & {
						config: workdir: "/app"
					},
					docker.#Set & {
						input: _
						config: env: PYTHONPATH: "/app"
					},
					docker.#Copy & {
						contents: client.filesystem."dug".read.contents
						include: ["requirements.txt"]
					},
					docker.#Run & {
						command: {
							name: "pip"
							args: ["install", "-r", "requirements.txt"]
						}
					},
					docker.#Copy & {
						contents: client.filesystem."dug".read.contents
					},
				]
			}
			fmt: bash.#Run & {
				input: img.output
				script: contents: "black --check ."
			}
			imp: bash.#Run & {
				input: img.output
				script: contents: "isort -c ."
			}
			lint: bash.#Run & {
				input: img.output
				script: contents: "pylint $(find . -type f -name '*.py') && pyright ."
			}
			test: bash.#Run & {
				input: img.output
				script: contents: "pytest ."
			}
		}

		genetic: {
			img: docker.#Build & {
				steps: [
					docker.#Pull & {
						source: "python:3.11"
					},
					docker.#Set & {
						config: workdir: "/app"
					},
					docker.#Set & {
						input: _
						config: env: PYTHONPATH: "/app"
					},
					docker.#Copy & {
						contents: client.filesystem."genetic".read.contents
						include: ["requirements.txt"]
					},
					docker.#Run & {
						command: {
							name: "pip"
							args: ["install", "-r", "requirements.txt"]
						}
					},
					docker.#Copy & {
						contents: client.filesystem."genetic".read.contents
					},
				]
			}
			fmt: bash.#Run & {
				input: img.output
				script: contents: "black --check ."
			}
			lint: bash.#Run & {
				input: img.output
				script: contents: "pylint genetic test && pyright ."
			}
			test: bash.#Run & {
				input: img.output
				script: contents: "pytest ."
			}
		}

	}
}
