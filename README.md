# 🌳 ntree

A modern, feature-rich replacement for the classic Linux `tree` command — written in Python.

> 🎨 Colorful. 🔍 Filterable. 🗂️ Metadata-rich. 🧠 Smartly structured.


## 🚀 Features

- 📁 Visual directory structure in a tree format
- 🎨 Optional emoji indicators for files and folders
- 📦 Show file sizes in human-readable format
- 📄 Display file metadata: owner, last modified time
- 🧭 Control recursion depth (`--depth`)
- 👻 Show or hide hidden files (`--show-hidden`)
- 🧹 Filter by file extension (`-e`)
- 🧾 Output to file (`-o`)
- 🔄 Reverse order (`--ztoa`)
- 📜 Easy to use and extend


## 📦 Installation

Install it via **pip** from [PyPI](https://pypi.org/project/better-tree):

```bash
pip install better-tree
```


## 🛠️ Usage

better-tree [OPTIONS] <path>

## 🔧 Options


| Option | Description |
| :-- | :-- |
| --depth  |  N	Limit traversal to N levels deep
| --show-hidden	 | Include hidden files and folders
| -e <ext>	 | Show only files with a specific extension (e.g. py, txt)
| -o <filename> | 	Output the tree to a specified file
| --ztoa | 	List entries in reverse (Z → A)
| --meta	 | Show metadata: size, owner, last modified



## 📂 Example
```bash
better-tree ~/projects/myapp --depth 2 --meta --show-hidden -e py -o tree.txt
```
This will:
- Traverse up to 2 levels deep
- Show only .py files
- Include file metadata
- Show hidden files
- Save output to tree.txt



## 📸 Screenshot

```bash
📁 myapp/
├── 📁 src/
│   ├── 📄 main.py (3.1 KB)
│   └── 📄 utils.py (1.2 KB)
├── 📄 README.md (800 B)
└── 📁 .git/
```


## 🤝 Contributing

Pull requests and suggestions are welcome!
If you’d like to contribute, please fork the repository and use a feature branch.
Thanks for making it better. 💚



## 📜 License

MIT License.
See LICENSE file for full text.



## 🧠 Author

Built with ❤️ by Vijay Satheesh


## ⭐ Star This Repo

If you like this project, give it a ⭐ — it helps more people discover it!


