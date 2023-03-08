import asyncio

import dagger


async def decisiontree():
    async with dagger.Connection() as client:
        await (
            client.container()
            .from_("mcr.microsoft.com/dotnet/sdk:7.0")
            .with_mounted_directory(
                "/app",
                client.host()
                .directory("decision-tree")
                .without_directory("bin")
                .without_directory("obj"),
            )
            .with_workdir("/app")
            .with_exec(["dotnet", "restore"])
            .with_exec(["dotnet", "tool", "restore"])
            .with_exec(["dotnet", "build"])
            .with_exec(["dotnet", "tool", "run", "fantomas", "--check", "."])
            .with_exec(
                [
                    "dotnet",
                    "tool",
                    "run",
                    "dotnet-fsharplint",
                    "lint",
                    "DecisionTree.fsproj",
                ]
            )
            .with_exec(["dotnet", "test"])
            .exit_code()
        )


async def dijkstra():
    async with dagger.Connection() as client:
        await (
            client.container()
            .from_("golang:latest")
            .with_mounted_directory("/app", client.host().directory("dijkstra"))
            .with_workdir("/app")
            .with_exec(["go", "build", "-v"])
            .with_exec(["sh", "-c", "test -z $(gofmt -l .)"])
            .with_exec(["go", "test", "-v"])
            .exit_code()
        )


async def dug():
    async with dagger.Connection() as client:
        await (
            client.container()
            .from_("python:3.11")
            .with_workdir("/app")
            .with_env_variable("PYTHONPATH", "/app")
            .with_mounted_file(
                "/app/requirements.txt",
                client.host().directory("dug").file("requirements.txt"),
            )
            .with_exec(["pip", "install", "-r", "requirements.txt"])
            .with_mounted_directory(
                "/app",
                client.host()
                .directory("dug")
                .without_directory(".pytest_cache")
                .without_directory(".streamlit")
                .without_directory("venv"),
            )
            .with_exec(["black", "--check", "."])
            .with_exec(["isort", "-c", "."])
            .with_exec(["sh", "-c", "pylint $(find . -type f -name '*.py')"])
            .with_exec(["pyright", "."])
            .with_exec(["pytest", "."])
            .exit_code()
        )


async def genetic():
    async with dagger.Connection() as client:
        await (
            client.container()
            .from_("python:3.11")
            .with_workdir("/app")
            .with_env_variable("PYTHONPATH", "/app")
            .with_mounted_file(
                "/app/requirements.txt",
                client.host().directory("genetic").file("requirements.txt"),
            )
            .with_exec(["pip", "install", "-r", "requirements.txt"])
            .with_mounted_directory(
                "/app",
                client.host()
                .directory("genetic")
                .without_directory(".pytest_cache")
                .without_directory("venv"),
            )
            .with_exec(["black", "--check", "."])
            .with_exec(["isort", "-c", "."])
            .with_exec(["pylint", "genetic", "test"])
            .with_exec(["pyright", "."])
            .with_exec(["pytest", "."])
            .exit_code()
        )


async def ci():
    await asyncio.gather(decisiontree(), dijkstra(), dug(), genetic())


asyncio.run(ci())
