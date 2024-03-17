# Crwler

Crwler is a streamlined web crawler designed to methodically map and download content starting from a base URL, efficiently capturing all downstream links in a structured, hierarchical manner.

## Features

- Hierarchical Mapping
- Content Downloading
- Link Handling
- [Still need to add - pull requests welcome!] Customizable Depth

## Installation

```bash
git clone https://github.com/vavlani/crwler.git
cd crwler
pip install -r requirements.txt
```

## Usage

```python
# Basic usage after navigating to Crwler/src/
python crwler.py --url https://example.com/baseurl_that_you_want_to_start_from/ \
    --output_dir /folder_you_want_to_download_to/
```

## Contributing

Contributions are welcome! Please see our contributing guidelines for more details.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
