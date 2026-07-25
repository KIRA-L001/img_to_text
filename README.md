# img_to_text

A browser-based tool that combines **image-to-text (OCR)** extraction with a
**text translator**.

## Features

- **Extract text from images** — upload an image and get its text via the
  [API Ninjas Image-to-Text API](https://api-ninjas.com/api/imagetotext).
- **Translate text** — translate typed or extracted text between languages
  using the Google Translate endpoint, with:
  - Auto language detection
  - Swap source/target languages
  - Upload a document (`.txt`, `.pdf`, `.doc`, `.docx`) as input
  - Download the translation as a `.txt` file
  - Character counter (5000-char limit)
  - Dark mode toggle

## Project structure

| File | Purpose |
|------|---------|
| `index.html` | Main page: image upload form + translator UI |
| `transtalte.html` | Standalone translator page |
| `script.js` | Translator logic + OCR submission handler |
| `script1.js` | OCR/download logic for the standalone page |
| `languages.js` | List of supported languages for the dropdowns |
| `config.js` | Your API Ninjas key (not committed — see below) |
| `style.css`, `style1.css` | Styling |

## Setup

1. Clone the repo.
2. Create `config.js` in the project root:

   ```js
   // config.js — do NOT commit this file
   const API_NINJAS_KEY = "your-api-ninjas-key-here";
   ```

   Get a free key at [api-ninjas.com](https://api-ninjas.com/).
3. Open `index.html` in a browser.

## License

MIT — see [LICENSE](LICENSE).
