#!/usr/bin/env python3
"""
Setup verification script

Run this after installing dependencies to verify your setup is correct.
"""

import sys
import os


def check_python_version():
    """Check Python version is 3.10+"""
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 10):
        print("❌ Python 3.10+ required")
        print(f"   Current version: {version.major}.{version.minor}.{version.micro}")
        return False
    print(f"✅ Python {version.major}.{version.minor}.{version.micro}")
    return True


def check_dependencies():
    """Check if required packages are installed"""
    try:
        import openai  # noqa: F401
        print("✅ openai installed")
        return True
    except ImportError:
        print("❌ openai not found")
        print("   Install with: pip install -r requirements.txt")
        return False


def check_api_key():
    """Check that an API key is set in the environment."""
    if os.environ.get("DEEPSEEK_API_KEY"):
        print("✅ DEEPSEEK_API_KEY is set")
        return True
    if os.environ.get("OPENAI_API_KEY"):
        print("✅ OPENAI_API_KEY is set (will be used as fallback)")
        return True
    print("❌ No API key found in environment")
    print("   Set DEEPSEEK_API_KEY (get one at https://platform.deepseek.com/)")
    print("   Example: export DEEPSEEK_API_KEY=sk-...")
    return False


def check_structure():
    """Check repository structure"""
    required_dirs = ["shared", "agent", "lessons"]
    all_exist = True

    for dir_name in required_dirs:
        if os.path.isdir(dir_name):
            print(f"✅ {dir_name}/ directory exists")
        else:
            print(f"❌ {dir_name}/ directory not found")
            all_exist = False

    return all_exist


def main():
    """Run all checks"""
    print("="*50)
    print("AI Agents from Scratch - Setup Verification")
    print("="*50)
    print()

    checks = [
        ("Python Version", check_python_version),
        ("Dependencies", check_dependencies),
        ("API Key", check_api_key),
        ("Repository Structure", check_structure),
    ]

    results = []

    for name, check_func in checks:
        print(f"\n{name}:")
        results.append(check_func())

    print("\n" + "="*50)
    if all(results):
        print("✅ All checks passed! You're ready to start learning.")
        print("\nNext steps:")
        print("1. Read lessons/01_basic_llm_chat.md")
        print("2. Run: python complete_example.py")
    else:
        print("⚠️  Some checks failed. Please fix the issues above.")
    print("="*50)


if __name__ == "__main__":
    main()
