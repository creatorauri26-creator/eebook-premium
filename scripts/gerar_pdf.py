#!/usr/bin/env python3
"""Valida o manifesto e gera o PDF sem modificar os arquivos editoriais."""
import argparse
import json
from pathlib import Path
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parent.parent


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verificar", action="store_true", help="validar sem gerar PDF")
    args = parser.parse_args()
    try:
        chapters = json.loads((ROOT / "scripts/capitulos.json").read_text(encoding="utf-8"))
        if not isinstance(chapters, list) or any(not isinstance(p, str) for p in chapters):
            raise ValueError("O manifesto deve ser uma lista de caminhos de capítulos.")
        if len(chapters) != len(set(chapters)):
            raise ValueError("Há capítulos duplicados no manifesto.")
        for name in chapters:
            path = (ROOT / name).resolve()
            if not path.is_relative_to(ROOT / "capitulos") or path.suffix != ".md":
                raise ValueError(f"Capítulo fora de capitulos/ ou sem extensão .md: {name}")
            if not path.is_file() or not path.read_text(encoding="utf-8").strip():
                raise ValueError(f"Capítulo ausente ou vazio: {name}")
        if args.verificar:
            print(f"Estrutura válida: {len(chapters)} capítulo(s) no manifesto.")
            return 0
        if not chapters:
            raise ValueError("Nenhum capítulo cadastrado. Estrutura inicial: PDF não gerado.")
        for tool in ("pandoc", "xelatex"):
            if not shutil.which(tool):
                raise ValueError(f"Dependência ausente: {tool}. Leia scripts/dependencias.md.")
        (ROOT / "build").mkdir(exist_ok=True)
        subprocess.run(["pandoc", "--defaults=scripts/pdf.yaml", *chapters,
                        "--output=build/ebook.pdf"], cwd=ROOT, check=True)
        print("PDF gerado em build/ebook.pdf. Revisão visual e aprovação ainda necessárias.")
        return 0
    except (OSError, ValueError, subprocess.CalledProcessError) as exc:
        print(f"Erro: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
