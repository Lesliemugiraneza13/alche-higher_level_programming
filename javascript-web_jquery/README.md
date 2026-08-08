# JavaScript - Web jQuery

DOM manipulation with vanilla JavaScript and jQuery: selecting elements,
event handling, class toggling, list manipulation, and fetching remote
data (SWAPI, fourtonfish).

## Requirements

- Files run in the browser via `<script>` tags — no shebang needed
- Code is semistandard compliant
- jQuery 3.2.1 is loaded via CDN in each corresponding `*-main.html` test file
- `0-script.js` may only use vanilla JS (`document.querySelector`, no jQuery)
- `1-script.js` through `9-script.js` must use the jQuery API only
  (no `document.querySelector`)

## Tasks

| File | Description |
| --- | --- |
| `0-script.js` | Colors `<header>` red using vanilla `document.querySelector` |
| `1-script.js` | Colors `<header>` red using jQuery |
| `2-script.js` | Colors `<header>` red on click of `DIV#red_header` |
| `3-script.js` | Adds class `red` to `<header>` on click of `DIV#red_header` |
| `4-script.js` | Toggles `<header>` class between `red`/`green` on click of `DIV#toggle_header` |
| `5-script.js` | Appends `<li>Item</li>` to `UL.my_list` on click of `DIV#add_item` |
| `6-script.js` | Updates `<header>` text on click of `DIV#update_header` |
| `7-script.js` | Fetches a Star Wars character's name and displays it in `DIV#character` |
| `8-script.js` | Fetches all Star Wars film titles and lists them in `UL#list_movies` |
| `9-script.js` | Fetches a translated "hello" and displays it in `DIV#hello` (runs on DOM ready, since loaded from `<head>`) |

Open the matching `N-main.html` file in a browser to test each task.
