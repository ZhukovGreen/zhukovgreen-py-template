#!/usr/bin/env python
import asyncio
from asyncio.subprocess import PIPE, Process
from typing import Tuple


async def run(cmd) -> Tuple[str, str]:
    process: Process = await asyncio.create_subprocess_shell(
        cmd, stdout=PIPE, stderr=PIPE
    )
    stdout, stderr = await process.communicate()
    return stdout.decode(), stderr.decode()


async def print_command(cmd):
    main_sep = 79 * "*"
    sep = 40 * "- "
    print(main_sep)
    print(f"Executing command: {cmd}")
    stdout, stderr = await run(cmd)
    print(sep)
    print(f"STDOUT:\n{stdout}")
    print(sep)
    print(f"STDERR:\n{stderr}")
    print(sep)
    print(main_sep)


if __name__ == "__main__":

    async def main():
        await print_command("git init")
        await print_command("make install")
        await print_command("make bump_dependencies")

    asyncio.run(main())
