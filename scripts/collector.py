#!/usr/bin/env python3
"""
Collector Script for Cognitive Systems Architecture
Gathers scattered notes, dialogs, and code snippets from local paths and SourceCraft repos.
Integrates them into the main repo for RAG indexing and portfolio generation.

Usage:
    python scripts/collector.py --local-paths /path/to/notes /path/to/dialogs --sourcecraft-repo https://github.com/user/repo
"""

import os
import shutil
import argparse
import git
from pathlib import Path

class Collector:
    def __init__(self, output_dir="docs/notes"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def collect_local(self, paths):
        """Collect files from local paths."""
        for path in paths:
            src_path = Path(path)
            if src_path.exists():
                for file in src_path.rglob("*"):
                    if file.is_file() and file.suffix in [".md", ".txt", ".py", ".json"]:
                        rel_path = file.relative_to(src_path)
                        dest = self.output_dir / rel_path
                        dest.parent.mkdir(parents=True, exist_ok=True)
                        shutil.copy2(file, dest)
                        print(f"Copied: {file} -> {dest}")
            else:
                print(f"Path not found: {path}")

    def collect_sourcecraft(self, repo_url, branch="main"):
        """Clone and integrate SourceCraft repo."""
        repo_name = repo_url.split("/")[-1].replace(".git", "")
        clone_dir = self.output_dir / "sourcecraft" / repo_name
        if clone_dir.exists():
            shutil.rmtree(clone_dir)
        git.Repo.clone_from(repo_url, clone_dir, branch=branch)
        print(f"Cloned SourceCraft repo: {repo_url} -> {clone_dir}")

    def deduplicate(self):
        """Remove duplicates based on content hash."""
        # TODO: Implement deduplication
        pass

    def index_for_rag(self):
        """Prepare files for RAG indexing."""
        # TODO: Generate index
        pass

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Collect and integrate scattered artifacts.")
    parser.add_argument("--local-paths", nargs="+", help="Local paths to scan")
    parser.add_argument("--sourcecraft-repo", help="SourceCraft repo URL")
    args = parser.parse_args()

    collector = Collector()
    if args.local_paths:
        collector.collect_local(args.local_paths)
    if args.sourcecraft_repo:
        collector.collect_sourcecraft(args.sourcecraft_repo)
    collector.deduplicate()
    collector.index_for_rag()