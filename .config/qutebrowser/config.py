# Autogenerated config.py
# Documentation:
#   qute://help/configuring.html
#   qute://help/settings.html

# Uncomment this to still load settings configured via autoconfig.yml
# config.load_autoconfig()

# Enable JavaScript.
# Type: Bool
config.set('content.javascript.enabled', True, 'file://*')

# Enable JavaScript.
# Type: Bool
config.set('content.javascript.enabled', True, 'chrome://*/*')

# Enable JavaScript.
# Type: Bool
config.set('content.javascript.enabled', True, 'qute://*/*')

# Directory to save downloads to. If unset, a sensible OS-specific
# default is used.
# Type: Directory
c.downloads.location.directory = '/home/ivar/downloads/'

# Which categories to show (in which order) in the :open completion.
# Type: FlagList
# Valid values:
#   - searchengines
#   - quickmarks
#   - bookmarks
#   - history
c.completion.open_categories = ['searchengines', 'quickmarks', 'bookmarks', 'history']

# CSS border value for hints.
# Type: String
c.hints.border = '1px solid #000000'

# Search engines which can be used via the address bar. Maps a search
# engine name (such as `DEFAULT`, or `ddg`) to a URL with a `{}`
# placeholder. The placeholder will be replaced by the search term, use
# `{{` and `}}` for literal `{`/`}` signs. The search engine named
# `DEFAULT` is used when `url.auto_search` is turned on and something
# else than a URL was entered to be opened. Other search engines can be
# used by prepending the search engine name to the search term, e.g.
# `:open google qutebrowser`.
# Type: Dict
c.url.searchengines = {'DEFAULT': 'https://duckduckgo.com/?q={}', 'git': 'https://github.com/search?q={}', 'kat': 'https://katcr.co/katsearch/page/1/{}', 'nix': 'https://nixos.org/nixos/packages.html?channel=nixos-unstable&query={}', 'proton': 'https://www.protondb.com/search?q={}', 'tweak': 'https://tweakers.net/zoeken/?keyword={}', 'yt': 'https://www.youtube.com/results?search_query={}'}

# Text color of the completion widget. May be a single color to use for
# all columns or a list of three colors, one for each column.
# Type: List of QtColor, or QtColor
c.colors.completion.fg = '#eceff4'

# Background color of the completion widget for odd rows.
# Type: QssColor
c.colors.completion.odd.bg = '#434c5e'

# Background color of the completion widget for even rows.
# Type: QssColor
c.colors.completion.even.bg = '#434c5e'

# Foreground color of completion widget category headers.
# Type: QtColor
c.colors.completion.category.fg = '#eceff4'

# Background color of the completion widget category headers.
# Type: QssColor
c.colors.completion.category.bg = '#3b4252'

# Top border color of the completion widget category headers.
# Type: QssColor
c.colors.completion.category.border.top = '#3b4252'

# Bottom border color of the completion widget category headers.
# Type: QssColor
c.colors.completion.category.border.bottom = '#3b4252'

# Foreground color of the selected completion item.
# Type: QtColor
c.colors.completion.item.selected.fg = '#eceff4'

# Background color of the selected completion item.
# Type: QssColor
c.colors.completion.item.selected.bg = '#8fbcbb'

# Top border color of the selected completion item.
# Type: QssColor
c.colors.completion.item.selected.border.top = '#8fbcbb'

# Bottom border color of the selected completion item.
# Type: QssColor
c.colors.completion.item.selected.border.bottom = '#8fbcbb'

# Foreground color of the matched text in the completion.
# Type: QtColor
c.colors.completion.match.fg = '#eee8d5'

# Color of the scrollbar handle in the completion view.
# Type: QssColor
c.colors.completion.scrollbar.fg = '#eee8d5'

# Color of the scrollbar in the completion view.
# Type: QssColor
c.colors.completion.scrollbar.bg = '#4c566a'

# Background color for the download bar.
# Type: QssColor
c.colors.downloads.bar.bg = '#3b4252'

# Color gradient start for download text.
# Type: QtColor
c.colors.downloads.start.fg = '#eceff4'

# Foreground color for downloads with errors.
# Type: QtColor
c.colors.downloads.error.fg = '#eceff4'

# Background color for downloads with errors.
# Type: QtColor
c.colors.downloads.error.bg = '#bf616a'

# Font color for hints.
# Type: QssColor
c.colors.hints.fg = '#eceff4'

# Background color for hints. Note that you can use a `rgba(...)` value
# for transparency.
# Type: QssColor
c.colors.hints.bg = '#2f343f'

# Font color for the matched part of hints.
# Type: QtColor
c.colors.hints.match.fg = '#eee8d5'

# Text color for the keyhint widget.
# Type: QssColor
c.colors.keyhint.fg = '#eceff4'

# Highlight color for keys to complete the current keychain.
# Type: QssColor
c.colors.keyhint.suffix.fg = '#ebcb8b'

# Foreground color of an error message.
# Type: QssColor
c.colors.messages.error.fg = '#eceff4'

# Background color of an error message.
# Type: QssColor
c.colors.messages.error.bg = '#bf616a'

# Border color of an error message.
# Type: QssColor
c.colors.messages.error.border = '#bf616a'

# Foreground color of a warning message.
# Type: QssColor
c.colors.messages.warning.fg = '#eceff4'

# Background color of a warning message.
# Type: QssColor
c.colors.messages.warning.bg = '#2f3333'

# Border color of a warning message.
# Type: QssColor
c.colors.messages.warning.border = '#ebcb8b'

# Foreground color of an info message.
# Type: QssColor
c.colors.messages.info.fg = '#eceff4'

# Background color of an info message.
# Type: QssColor
c.colors.messages.info.bg = '#3b4252'

# Border color of an info message.
# Type: QssColor
c.colors.messages.info.border = '#3b4252'

# Foreground color for prompts.
# Type: QssColor
c.colors.prompts.fg = '#eceff4'

# Border used around UI elements in prompts.
# Type: String
c.colors.prompts.border = '1px solid #eceff4'

# Background color for prompts.
# Type: QssColor
c.colors.prompts.bg = '#434c5e'

# Background color for the selected item in filename prompts.
# Type: QssColor
c.colors.prompts.selected.bg = '#e5e9f0'

# Foreground color of the statusbar.
# Type: QssColor
c.colors.statusbar.normal.fg = '#eceff4'

# Background color of the statusbar.
# Type: QssColor
c.colors.statusbar.normal.bg = '#3b4252'

# Foreground color of the statusbar in insert mode.
# Type: QssColor
c.colors.statusbar.insert.fg = '#eceff4'

# Background color of the statusbar in insert mode.
# Type: QssColor
c.colors.statusbar.insert.bg = '#5e81ac'

# Foreground color of the statusbar in passthrough mode.
# Type: QssColor
c.colors.statusbar.passthrough.fg = '#eceff4'

# Background color of the statusbar in passthrough mode.
# Type: QssColor
c.colors.statusbar.passthrough.bg = '#000000'

# Foreground color of the statusbar in private browsing mode.
# Type: QssColor
c.colors.statusbar.private.fg = '#eceff4'

# Background color of the statusbar in private browsing mode.
# Type: QssColor
c.colors.statusbar.private.bg = '#e5e9f0'

# Foreground color of the statusbar in command mode.
# Type: QssColor
c.colors.statusbar.command.fg = '#eceff4'

# Background color of the statusbar in command mode.
# Type: QssColor
c.colors.statusbar.command.bg = '#3b4252'

# Foreground color of the statusbar in private browsing + command mode.
# Type: QssColor
c.colors.statusbar.command.private.fg = '#eceff4'

# Background color of the statusbar in private browsing + command mode.
# Type: QssColor
c.colors.statusbar.command.private.bg = '#e5e9f0'

# Foreground color of the statusbar in caret mode.
# Type: QssColor
c.colors.statusbar.caret.fg = '#eceff4'

# Background color of the statusbar in caret mode.
# Type: QssColor
c.colors.statusbar.caret.bg = '#5e81ac'

# Foreground color of the statusbar in caret mode with a selection.
# Type: QssColor
c.colors.statusbar.caret.selection.fg = '#eceff4'

# Background color of the statusbar in caret mode with a selection.
# Type: QssColor
c.colors.statusbar.caret.selection.bg = '#5e81ac'

# Background color of the progress bar.
# Type: QssColor
c.colors.statusbar.progress.bg = '#eceff4'

# Default foreground color of the URL in the statusbar.
# Type: QssColor
c.colors.statusbar.url.fg = '#eceff4'

# Foreground color of the URL in the statusbar on error.
# Type: QssColor
c.colors.statusbar.url.error.fg = '#bf616a'

# Foreground color of the URL in the statusbar for hovered links.
# Type: QssColor
c.colors.statusbar.url.hover.fg = '#eee8d5'

# Foreground color of the URL in the statusbar on successful load
# (http).
# Type: QssColor
c.colors.statusbar.url.success.http.fg = '#eceff4'

# Foreground color of the URL in the statusbar on successful load
# (https).
# Type: QssColor
c.colors.statusbar.url.success.https.fg = '#eceff4'

# Foreground color of the URL in the statusbar when there's a warning.
# Type: QssColor
c.colors.statusbar.url.warn.fg = '#000000'

# Color gradient start for the tab indicator.
# Type: QtColor
c.colors.tabs.indicator.start = '#8fbcbb'

# Color gradient end for the tab indicator.
# Type: QtColor
c.colors.tabs.indicator.stop = '#ebcb8b'

# Color for the tab indicator on errors.
# Type: QtColor
c.colors.tabs.indicator.error = '#bf616a'

# Background color of unselected odd tabs.
# Type: QtColor
c.colors.tabs.odd.bg = '#4b5151'

# Background color of unselected even tabs.
# Type: QtColor
c.colors.tabs.even.bg = '#4b5151'

# Background color of selected odd tabs.
# Type: QtColor
c.colors.tabs.selected.odd.bg = '#2f343f'

# Background color of selected even tabs.
# Type: QtColor
c.colors.tabs.selected.even.bg = '#2f343f'
